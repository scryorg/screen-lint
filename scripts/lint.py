#!/usr/bin/env python3
"""Grade one screen against the rules of its type.

    python3 lint.py --type paywall --obs DIR/obs.json --img DIR/img.png --ocr DIR/ocr.json --json DIR/lint.json

The reading (obs.json, see references/read.md) says what is where; this script measures contrast, drawn size and
position from the pixels (img.png, ocr.json) and decides each rule in rules/<type>.json. It runs check_obs first and
stops if the reading does not pass. Each finding is {rule, severity, says, why, boxes (pixels), value}. Each rule
counts once, at its worst level, for the grade: A no errors and at most 1 warning; B no errors; C 1 error; D 2
errors; F 3 or more; hints never count.

Prints the answer-ready list, findings ordered error, warn, hint, numbered the way overlay.py numbers its boxes.
Exit 0 graded, 1 the reading did not pass check_obs, 2 a usage or file problem, 3 the reading says the screen is not
this type (nothing is graded: go back to the classifier).
"""
import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from check_obs import problems                                              # noqa: E402
try:
    from pixels import busy, button, glyph, pct, text_contrast, text_pt, union   # noqa: E402
except ImportError:
    print('pip install pillow numpy opencv-python-headless', file=sys.stderr)
    print('lint.py needs the packages above; run that line and try again.', file=sys.stderr)
    sys.exit(2)

SEV = {'error': 0, 'warn': 1, 'hint': 2}


def third(box):
    """Which third of the screen, top to bottom, the middle of a percent box is in."""
    y = (box[1] + box[3]) / 2
    return 'top' if y < 100 / 3 else 'mid' if y < 200 / 3 else 'bottom'


def safe(f, *a):
    """A pixel check on a strange box (off the edge, a sliver) must not stop the other checks."""
    try:
        return f(*a)
    except Exception:
        return None


def covered(boxes):
    """Share of the screen, in percent, that these percent boxes cover together."""
    import numpy as np
    m = np.zeros((100, 100), bool)
    for b in boxes:
        m[int(b[1]):int(np.ceil(b[3])), int(b[0]):int(np.ceil(b[2]))] = True
    return float(m.mean() * 100)


def grade(findings):
    worst = {}
    for f in findings:
        worst[f['rule']] = min(worst.get(f['rule'], 9), SEV[f['severity']])
    e, w = sum(v == 0 for v in worst.values()), sum(v == 1 for v in worst.values())
    h = sum(v == 2 for v in worst.values())
    return ('A' if not e and w <= 1 else 'B' if not e else 'C' if e == 1 else 'D' if e == 2 else 'F'), e, w, h


def lint_screen(R, o, ocr, img):
    """Findings and a grade for one reading `o` of one screen: `ocr` is ocr.json, `img` its pixels (RGB array)."""
    import numpy as np
    W, H, s = ocr['W'], ocr['H'], ocr['scale']
    names = {v: R['variants'][v]['name'] for v in o['variants'] if v in R['variants']}
    res = {'id': o['id'], 'app': ocr.get('app', ''), 'type': R['type'], 'type_name': R['name'], 'is_type': o['is_type'],
           'instead': o['instead'], 'variants': o['variants'], 'subtypes': names, 'new_variant': o['new_variant'],
           'state': o['state'], 'dark': o['dark'], 'W': W, 'H': H, 'grade': None, 'findings': [], 'measured': {},
           'not_checked': R['not_checked']}
    if not o['is_type']:
        return res
    L = {ln['i']: ln for ln in ocr['lines']}
    rules = R['rules']
    m, out = res['measured'], res['findings']
    parts = o['parts']
    pres = lambda k: parts[str(k)]['present']
    pboxes = lambda k: [pct(b, W, H) for b in parts[str(k)].get('boxes', [])]
    has_test = lambda name: any(r['test'] == name for r in rules)
    exempt = {}
    for r in rules:
        if r['kind'] == 'exempt':
            for x in r['exempts']:
                exempt.setdefault(x, set()).add(r['variant'])
    dimmed = o['state'] == 'dimmed'

    def find(r, says=None, boxes=None, value=None, severity=None):
        out.append({'rule': r['id'], 'severity': severity or r['severity'], 'says': says or r['says'], 'why': r['why'],
                    'boxes': [[int(v) for v in b] for b in boxes or [] if b], 'value': value})

    # the controls, as the reader listed them, with the drawn glyph or button found from the pixels
    ctl = []
    for c in o['controls']:
        box = pct(c['box'], W, H)
        lines = [L[i] for i in c.get('lines', []) if i in L]
        d = {'role': c['role'], 'box': box, 'lines': lines, 'glyph': None}
        if c['role'] in ('close', 'back'):
            d['glyph'] = safe(glyph, img, box, s)
            if d['glyph']:
                d['box'] = d['glyph']['box']
        elif c['role'] in ('primary', 'secondary') and lines:
            d['box'] = safe(button, img, box, [ln['box'] for ln in lines], s) or box
        ctl.append(d)

    # rules decided from what the reader wrote
    for r in rules:
        test = r['test']
        if r['kind'] == 'pitfall':
            name, *a = test.split(':')
            if name == 'reader':
                q = o['pitfalls'][r['pitfall']]
                if q['seen']:
                    find(r, value=q['evidence'])
            elif name == 'part_missing':
                if not pres(a[0]):
                    find(r)
            elif name == 'part_area_over':
                if pres(a[0]):
                    area = covered(parts[a[0]]['boxes'])
                    if area > float(a[1]):
                        find(r, boxes=pboxes(a[0]), value=round(area, 1))
            elif name == 'count_over':
                if pres(a[0]) and len(parts[a[0]]['boxes']) > int(a[1]):
                    find(r, boxes=pboxes(a[0]), value=len(parts[a[0]]['boxes']))
            elif name == 'faint_control' and not dimmed:
                for c in ctl:
                    if c['role'] in ('close', 'back') and c['glyph'] and c['glyph']['contrast'] < 3:
                        find(r, boxes=[c['box']], value=round(c['glyph']['contrast'], 1))
            elif name == 'low_label' and not dimmed:
                for c in ctl:
                    if c['role'] == 'primary':
                        for ln in c['lines']:
                            v = safe(text_contrast, img, ln['box'], s)
                            if v is not None and v < 3 and not safe(busy, img, ln['box'], s):
                                find(r, boxes=[ln['box']], value=round(v, 1))
        elif r['kind'] in ('convention', 'variant'):
            k = r.get('part')
            skip = bool(set(o['variants']) & exempt.get(r['id'], set()))
            if test == 'presence' and not pres(k) and not skip:
                find(r)
            elif test == 'v_presence' and r['variant'] in o['variants'] and not pres(k):
                find(r)
            elif test == 'position' and pres(k) and not skip:
                th = third(parts[str(k)]['boxes'][0])
                if th != r['third']:
                    find(r, boxes=pboxes(k)[:1], value=th)
            elif test == 'count' and pres(k) and len(parts[str(k)]['boxes']) > 1:
                find(r, boxes=pboxes(k), value=len(parts[str(k)]['boxes']))
    # a pitfall that says a part is missing already says it: drop the plain presence finding for that part
    gone = {r['test'].split(':')[1] for r in rules if r['kind'] == 'pitfall' and r['test'].startswith('part_missing')
            and any(f['rule'] == r['id'] for f in out)}
    byid = {r['id']: r for r in rules}
    out[:] = [f for f in out if not (byid[f['rule']]['kind'] in ('convention', 'variant') and byid[f['rule']]['test'] in ('presence', 'v_presence')
                                      and str(byid[f['rule']]['part']) in gone)]

    # platform rules, from the pixels
    P = {r['test']: r for r in rules if r['kind'] == 'platform'}
    keyed = []   # (name, [ocr lines]) for the parts whose text has to be readable
    for k in R['key_text']:
        if pres(k):
            keyed.append((R['parts'][str(k)]['name'], [L[i] for i in parts[str(k)].get('lines', []) if i in L]))

    def groups(lines):
        # a part with a few lines is judged line by line, a paragraph by its typical line
        return [[ln] for ln in lines] if len(lines) <= 3 else [lines]

    if 'text_contrast' in P and not dimmed:
        r = P['text_contrast']
        items = []
        for c in ctl:
            if c['role'] in ('primary', 'secondary'):
                items += [(f'{c["role"]} button label', [ln], c['role'] == 'primary') for ln in c['lines']]
        for name, lines in keyed:
            items += [(name, g, False) for g in groups(lines)]
        judged = set()   # each OCR line is judged once: as a control label first, then as part text
        for what, g, bold in items:
            g = [ln for ln in g if ln['i'] not in judged]
            judged.update(ln['i'] for ln in g)
            if not g:
                continue
            if any(safe(busy, img, ln['box'], s) for ln in g):
                m[f'{what}'] = 'busy background'
                continue
            vals = [safe(text_contrast, img, ln['box'], s) for ln in g]
            vals = [v for v in vals if v is not None]
            if not vals:
                continue
            v = round(float(np.median(vals)), 1)
            ln = g[0] if len(g) == 1 else None
            pt = text_pt(g[0], s) if len(g) == 1 else float(np.median([text_pt(x, s) for x in g]))
            large = pt >= 18 or (bold and pt >= 14)
            label = f'"{ln["text"]}"' if ln else 'the typical line'
            m[f'{what} {label}'] = v
            box = union([x['box'] for x in g])
            own = bold and has_test('low_label')
            if v < 3 and not own:
                find(r, f'The {what} {label} is {v}:1 against its background, under 3:1, the floor even for large text.', [box], v, 'error')
            elif 3 <= v < 4.5 and not large:
                find(r, f'The {what} {label} is {v}:1 against its background; text this size needs 4.5:1.', [box], v, 'warn')
        if not has_test('faint_control'):
            for c in ctl:
                if c['role'] in ('close', 'back') and c['glyph'] and c['glyph']['contrast'] < 3:
                    v = round(c['glyph']['contrast'], 1)
                    find(r, f'The {c["role"]} control is {v}:1 against what is behind it. Controls need 3:1.', [c['box']], v, 'error')
        for c in ctl:
            if c['role'] in ('close', 'back') and c['glyph']:
                m[f'{c["role"]} glyph contrast'] = round(c['glyph']['contrast'], 1)
    if 'text_size' in P:
        r = P['text_size']
        for name, lines in keyed:
            for g in groups(lines):
                pt = float(np.median([text_pt(x, s) for x in g]))
                if len(g) == 1:
                    pt = text_pt(g[0], s)
                m[f'{name} pt'] = round(pt, 1)
                if pt < 10.5:
                    find(r, f'The text of "{name}" is about {pt:.0f} pt; Apple\'s smallest text is 11 pt.', [union([x['box'] for x in g])], round(pt, 1))
    if 'safe_area' in P:
        r = P['safe_area']
        clock = next((ln['box'] for ln in ocr['lines'] if re.fullmatch(r'\d{1,2}:\d{2}( ?[AP]M)?', ln['text'].strip())
                      and ln['box'][3] < 0.08 * H), None)
        tall = H / W > 2   # a phone with a home indicator, not a home button
        for c in ctl:
            if c['role'] == 'field':
                continue
            b = c['box']
            if clock and b[1] < clock[3] and b[3] > clock[1]:
                find(r, f'The {c["role"]} control sits in the status bar row.', [b], 'status bar')
            elif tall and b[3] > H - 17 * s:
                find(r, f'The {c["role"]} control comes to {max(0, (H - b[3]) / s):.0f} pt from the bottom edge, over the home indicator.',
                     [b], round(max(0, (H - b[3]) / s), 1))
    if 'target_size' in P:
        r = P['target_size']
        for c in ctl:
            if c['role'] in ('close', 'back') and c['glyph']:
                g = c['glyph']['box']
                size = max(g[2] - g[0], g[3] - g[1]) / s
                m[f'{c["role"]} glyph pt'] = round(size, 1)
                if size < 13:
                    find(r, f'The {c["role"]} control is drawn {size:.0f} pt across, smaller than a standard bar X. '
                         'The tap area may be bigger; Apple asks for 44 pt.', [g], round(size, 1))

    out.sort(key=lambda f: SEV[f['severity']])
    res['grade'], res['errors'], res['warnings'], res['hints'] = grade(out)
    return res


def show(res):
    """The numbered list the answer is made from. Numbers match the boxes overlay.py draws."""
    mark = {'error': 'ERROR', 'warn': 'WARN ', 'hint': 'HINT '}
    sub = ', '.join(res['subtypes'].values())
    sub = f'subtype: {sub}' if sub else f"new subtype: {res['new_variant']}" if res['new_variant'] else 'subtype: none fits'
    label = f" ({res['app']})" if res['app'] else ''
    print(f"Screen {res['id']}{label}: {res['type_name']} ({sub}), state {res['state']}, {'dark' if res['dark'] else 'light'}")
    if res['grade'] is None:
        print(f"Not graded: the reading says this is not {res['type_name']} but {res['instead']}. Go back to the classifier.")
        return
    n = lambda k, w: f"{res[k]} {w}{'' if res[k] == 1 else 's'}"
    print(f"Grade: {res['grade']} ({n('errors', 'error')}, {n('warnings', 'warning')}, {n('hints', 'hint')})")
    first = {}
    for i, f in enumerate(res['findings'], 1):
        v = f' [{f["value"]}]' if f['value'] not in (None, '') and str(f['value']) not in f['says'] else ''
        print(f" {i}. {mark[f['severity']]}  {f['rule']:<22} {f['says']}{v}")
        if f['rule'] in first:
            print(f"{'':12}Why: as in {first[f['rule']]}")
        else:
            first[f['rule']] = i
            print(f"{'':12}Why: {f['why']}")
    if not res['findings']:
        print(' No findings.')
    elif len(first) < len(res['findings']):
        print('The grade counts each rule once, however many places it fires.')
    if res['state'] == 'dimmed':
        print('Note: the screen is dimmed (a sheet or alert is over it), so contrast was not judged.')
    print('Not checked:')
    for x in res['not_checked']:
        print(f' - {x}')


def main():
    ap = argparse.ArgumentParser(description='Grade one screen against the rules of its type.')
    ap.add_argument('--type', help='the type key; default is the reading\'s own "type"')
    ap.add_argument('--obs', required=True, help='the reading, DIR/obs.json')
    ap.add_argument('--img', required=True, help='DIR/img.png')
    ap.add_argument('--ocr', required=True, help='DIR/ocr.json')
    ap.add_argument('--rules', help='a rules file; default rules/<type>.json next to scripts/')
    ap.add_argument('--json', help='write the result here (DIR/lint.json)')
    a = ap.parse_args()
    try:
        import numpy
        from PIL import Image
    except ImportError:
        print('pip install pillow numpy opencv-python-headless', file=sys.stderr)
        return 2
    bad = problems(a.obs, a.ocr)
    if bad:
        print(f'lint.py: the reading does not pass check_obs.py ({len(bad)} problem{"s" if len(bad) > 1 else ""}); fix obs.json first')
        for b in bad:
            print(f'  - {b}')
        return 1
    try:
        o = json.loads(pathlib.Path(a.obs).read_text())
        ocr = json.loads(pathlib.Path(a.ocr).read_text())
        t = a.type or o['type']
        if t != o['type']:
            print(f'lint.py: --type is {t} but the reading is of type {o["type"]}', file=sys.stderr)
            return 2
        rp = pathlib.Path(a.rules) if a.rules else HERE.parent / 'rules' / f'{t}.json'
        R = json.loads(rp.read_text())
        img = numpy.asarray(Image.open(a.img).convert('RGB'))
    except (OSError, ValueError) as e:
        print(f'lint.py: {e}', file=sys.stderr)
        return 2
    if img.shape[1] != ocr['W'] or img.shape[0] != ocr['H']:
        print(f'lint.py: img.png is {img.shape[1]}x{img.shape[0]} but ocr.json says {ocr["W"]}x{ocr["H"]}; run prep.py again', file=sys.stderr)
        return 2
    res = lint_screen(R, o, ocr, img)
    show(res)
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(res, indent=1) + '\n')
    return 0 if res['grade'] else 3


if __name__ == '__main__':
    sys.exit(main())
