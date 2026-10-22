#!/usr/bin/env python3
"""Mark the findings on the screenshot.

    python3 overlay.py DIR            # reads DIR/img.png and DIR/lint.json, writes DIR/overlay.png

Every finding with a place on the screen gets a coral box (or several) and its number, the same number lint.py
prints and the answer uses. A finding with no place, such as a part that is missing, is listed in a band under the
picture. Needs: pip install pillow. Exit 0 written, 2 a missing file or package, 3 nothing was graded.
"""
import argparse
import json
import pathlib
import sys

FONTS = ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
         '/Library/Fonts/Arial.ttf', '/System/Library/Fonts/Supplemental/Arial.ttf',
         '/System/Library/Fonts/Helvetica.ttc', 'C:/Windows/Fonts/arial.ttf']
CORAL = {True: (255, 107, 107), False: (217, 58, 50)}   # #ff6b6b on a dark screen, #d93a32 on a light one
MARK = {'error': 'ERROR', 'warn': 'WARN', 'hint': 'HINT'}


def font(size):
    from PIL import ImageFont
    for p in FONTS:
        if pathlib.Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                pass
    try:
        return ImageFont.load_default(size)
    except TypeError:
        return ImageFont.load_default()


def wrap(d, text, f, width):
    """Break text into lines no wider than width pixels."""
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if cur and d.textlength(t, font=f) > width:
            lines.append(cur)
            cur = w
        else:
            cur = t
    return lines + [cur] if cur else lines


def main():
    ap = argparse.ArgumentParser(description='Mark the findings of lint.json on img.png.')
    ap.add_argument('dir', help='the work folder with img.png and lint.json')
    a = ap.parse_args()
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print('pip install pillow', file=sys.stderr)
        return 2
    d = pathlib.Path(a.dir).expanduser()
    try:
        lint = json.loads((d / 'lint.json').read_text())
        im = Image.open(d / 'img.png').convert('RGB')
    except (OSError, ValueError) as e:
        print(f'overlay.py: {e}', file=sys.stderr)
        return 2
    if lint.get('grade') is None:
        print('overlay.py: lint.json has no grade (the reading said the screen is not this type); nothing to mark')
        return 3
    W, H = im.size
    color = CORAL[bool(lint.get('dark'))]
    d0 = ImageDraw.Draw(im)
    f = font(max(14, W // 38))
    width = max(2, W // 200)
    loose, drawn, tags = [], [], []
    for n, fd in enumerate(lint['findings'], 1):
        if not fd['boxes']:
            loose.append((n, fd))
            continue
        for x0, y0, x1, y1 in fd['boxes']:
            pad = width
            box = [max(0, x0 - pad), max(0, y0 - pad), min(W - 1, x1 + pad), min(H - 1, y1 + pad)]
            drawn.append(box)
            tw, th = d0.textlength(str(n), font=f) + 10, f.size + 6
            # the number sits above the box's top left; a number already there pushes this one to the right
            tx, ty = min(max(0, box[0]), max(0, W - tw)), box[1] - th if box[1] - th >= 0 else box[1]
            for _ in range(8):
                hit = next((t for t in tags if tx < t[2] and t[0] < tx + tw and ty < t[3] and t[1] < ty + th), None)
                if not hit:
                    break
                tx = hit[2] + 2
                if tx + tw > W:
                    tx, ty = max(0, W - tw), ty + th + 2
            tags.append([tx, ty, tx + tw, ty + th, n])
    # worst findings come first in lint.json, so draw the boxes last-to-first and a faint hint never covers an error
    for box in reversed(drawn):
        d0.rectangle(box, outline=color, width=width)
    for x0, y0, x1, y1, n in tags:
        d0.rectangle([x0, y0, x1, y1], fill=color)
        d0.text((x0 + 5, y0 + 2), str(n), font=f, fill=(0, 0, 0) if lint.get('dark') else (255, 255, 255))
    if loose:
        small = font(max(12, W // 48))
        probe = ImageDraw.Draw(Image.new('RGB', (8, 8)))
        margin = max(10, W // 40)
        rows = []
        for n, fd in loose:
            text = f"{n}. {MARK[fd['severity']]} {fd['rule']}: {fd['says']}"
            rows.append(wrap(probe, text, small, W - 2 * margin))
        lh = small.size + 6
        bar = margin + lh + sum(len(r) * lh + 8 for r in rows) + margin
        out = Image.new('RGB', (W, H + bar), (28, 28, 30))
        out.paste(im, (0, 0))
        dd = ImageDraw.Draw(out)
        y = H + margin
        dd.text((margin, y), 'Not on the picture:', font=small, fill=color)
        y += lh
        for r in rows:
            for line in r:
                dd.text((margin, y), line, font=small, fill=(235, 235, 240))
                y += lh
            y += 8
        im = out
    im.save(d / 'overlay.png')
    print(f"{d / 'overlay.png'}: {sum(len(x['boxes']) for x in lint['findings'])} boxes, {len(loose)} findings without a place")
    return 0


if __name__ == '__main__':
    sys.exit(main())
