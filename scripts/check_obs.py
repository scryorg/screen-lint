#!/usr/bin/env python3
"""Check a reading of one screen (obs.json) against the schema in references/read.md.

    python3 check_obs.py DIR/obs.json --ocr DIR/ocr.json      # prints OK, or BAD and the problems; exit 1 on BAD

The reading names its type (`type`); the parts, variants and pitfalls it must cover come from rules/<type>.json.
Run it until it prints OK: lint.py refuses a reading that does not pass.
"""
import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
RULES = HERE.parent / 'rules'

STATES = ('normal', 'empty', 'loading', 'error', 'dimmed')
ROLES = ('primary', 'secondary', 'close', 'back', 'field')
KEYS = ('id', 'type', 'is_type', 'instead', 'variants', 'new_variant', 'state', 'dark', 'parts', 'controls',
        'pitfalls', 'extra', 'notes')
MARKS = ('inactive', 'placeholder')   # OCR lines of greyed-out control labels, and of placeholder text


def load_rules(t):
    """rules/<t>.json as a dict, or None when t is not one of the 35 types."""
    p = RULES / f'{t}.json'
    if not isinstance(t, str) or not p.is_file():
        return None
    return json.loads(p.read_text())


def type_keys():
    """The 35 type keys, from any rules file's shape block."""
    for p in sorted(RULES.glob('*.json')):
        return json.loads(p.read_text())['shape']['type_keys']
    return []


def box_ok(b):
    return (isinstance(b, list) and len(b) == 4 and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in b)
            and 0 <= b[0] < b[2] <= 100 and 0 <= b[1] < b[3] <= 100)


def problems(obs_path, ocr_path):
    """The list of problems with this reading; empty when it is good."""
    try:
        o = json.loads(pathlib.Path(obs_path).read_text())
    except OSError as e:
        return [f'cannot read {obs_path}: {e}']
    except ValueError as e:
        return [f'not JSON: {e}']
    if not isinstance(o, dict):
        return ['the file must hold one JSON object']
    bad = [f'missing "{k}"' for k in KEYS if k not in o]
    if bad:
        return bad
    bad += [f'unknown key "{k}"' for k in o if k not in KEYS + MARKS]
    R = load_rules(o['type'])
    if R is None:
        return bad + [f'type is {o["type"]!r}, which is not one of the 35 type keys in references/types.md']
    t, sh = o['type'], R['shape']
    try:
        ocr = json.loads(pathlib.Path(ocr_path).read_text())
    except (OSError, ValueError) as e:
        return bad + [f'cannot read the OCR file {ocr_path}: {e}']
    lines = {ln['i'] for ln in ocr['lines']}

    def refs(where, xs):
        if not isinstance(xs, list) or not all(isinstance(i, int) and not isinstance(i, bool) for i in xs):
            bad.append(f'{where}.lines must be a list of OCR line numbers')
            return
        bad.extend(f'{where} names line {i}, which ocr.json does not have' for i in xs if i not in lines)

    if not isinstance(o['id'], str) or not o['id']:
        bad.append('"id" must be text (the image name)')
    for k in ('is_type', 'dark'):
        if not isinstance(o[k], bool):
            bad.append(f'"{k}" must be true or false')
    if o['state'] not in STATES:
        bad.append('state must be ' + ', '.join(STATES))
    for k in ('instead', 'new_variant', 'notes'):
        if not isinstance(o[k], str):
            bad.append(f'"{k}" must be text')
    for k, kind in (('variants', list), ('controls', list), ('extra', list), ('parts', dict), ('pitfalls', dict)):
        if not isinstance(o[k], kind):
            bad.append(f'"{k}" must be a {"list" if kind is list else "dict"}')
    if bad:
        return bad
    if not o['is_type']:
        keys = sh['type_keys'] + ['other']
        if o['instead'] not in keys or o['instead'] == t:
            bad.append(f'is_type is false: "instead" must be one of the other type keys or "other", not {o["instead"]!r}')
        for k in ('variants', 'controls', 'extra', 'parts', 'pitfalls') + MARKS:
            if o.get(k):
                bad.append(f'is_type is false: "{k}" must stay empty')
        if o['new_variant']:
            bad.append('is_type is false: "new_variant" must stay ""')
        return bad
    if o['instead']:
        bad.append('"instead" must be "" when is_type is true')
    # variants
    vs = sh['variants']
    bad += [f'variants has {v!r}; the listed ones are {", ".join(vs)}' for v in o['variants'] if v not in vs]
    if len(set(o['variants'])) != len(o['variants']):
        bad.append('variants lists one twice')
    if bool(o['variants']) == bool(o['new_variant']):
        bad.append('give variants (one or more of the listed) or new_variant (2 to 5 words), not both and not neither')
    if o['new_variant'] and not 2 <= len(o['new_variant'].split()) <= 5:
        bad.append('new_variant must be 2 to 5 words')
    # parts
    ks = sh['parts']
    if set(o['parts']) != set(ks):
        bad.append(f'parts must have exactly the keys {", ".join(ks)}; missing {sorted(set(ks) - set(o["parts"]))}, '
                   f'extra {sorted(set(o["parts"]) - set(ks))}')
    for k in ks:
        q = o['parts'].get(k)
        if not isinstance(q, dict) or not isinstance(q.get('present'), bool):
            bad.append(f'parts["{k}"] needs "present": true or false')
        elif q['present']:
            boxes = q.get('boxes')
            if not isinstance(boxes, list) or not 1 <= len(boxes) <= 12 or not all(box_ok(b) for b in boxes):
                bad.append(f'parts["{k}"] is present: it needs "boxes", 1 to 12 boxes [x0, y0, x1, y1] in percent, x1 > x0 and y1 > y0')
            refs(f'parts["{k}"]', q.get('lines', []))
        elif q.get('boxes') or q.get('lines'):
            bad.append(f'parts["{k}"] is not present: leave out boxes and lines')
    # controls
    for j, c in enumerate(o['controls']):
        if not isinstance(c, dict) or c.get('role') not in ROLES:
            bad.append(f'controls[{j}].role must be ' + ', '.join(ROLES))
            continue
        if not box_ok(c.get('box')):
            bad.append(f'controls[{j}] needs a box [x0, y0, x1, y1] in percent')
        refs(f'controls[{j}]', c.get('lines', []))
    # pitfalls
    pits = sh['pitfalls']
    if set(o['pitfalls']) != set(pits):
        bad.append(f'pitfalls must have exactly the keys {", ".join(pits)}')
    for i in pits:
        q = o['pitfalls'].get(i)
        if not isinstance(q, dict) or not isinstance(q.get('seen'), bool) or not isinstance(q.get('evidence', ''), str):
            bad.append(f'pitfalls["{i}"] needs "seen": true or false and "evidence": text')
        elif q['seen'] and not q.get('evidence'):
            bad.append(f'pitfalls["{i}"] is seen: say in "evidence" what shows it')
    # greyed-out labels and placeholder text, by OCR line
    for k in MARKS:
        refs(k, o.get(k, []))
    if set(o.get('inactive', [])) & set(o.get('placeholder', [])):
        bad.append('a line is either a greyed-out label (inactive) or placeholder text, not both')
    # extra
    if len(o['extra']) > 3 or not all(isinstance(x, str) and x and len(x.split()) <= 12 for x in o['extra']):
        bad.append('extra holds up to 3 short phrases (12 words at most each)')
    return bad


def main():
    ap = argparse.ArgumentParser(description='Check an obs.json against the schema in references/read.md.')
    ap.add_argument('obs', help='the reading, DIR/obs.json')
    ap.add_argument('--ocr', required=True, help='the OCR file prep.py wrote, DIR/ocr.json')
    a = ap.parse_args()
    bad = problems(a.obs, a.ocr)
    if not bad:
        print('OK')
        return 0
    print(f'BAD: {len(bad)} problem{"s" if len(bad) > 1 else ""} in {a.obs}')
    for b in bad:
        print(f'  - {b}')
    return 1


if __name__ == '__main__':
    sys.exit(main())
