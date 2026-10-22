#!/usr/bin/env python3
"""Prepare one screenshot for the screen linter: clean pixels, the text lines on it, and a gridded copy to read from.

    python3 prep.py <image> --out DIR [--scale N]

Writes, in DIR (made if it does not exist):
- img.png   the screenshot flattened to RGB (a transparent corner becomes white)
- ocr.json  {id, W, H, scale, lines}: every text line RapidOCR finds (local, free), {i, text, conf, box} with the
            box in pixels
- grid.jpg  the screen at 640 px wide with a teal grid every 5% (numbers every 10%) and an orange box with the
            line number i on every text line, so you can read positions in percent and cite lines by number

`scale` is points-to-pixels: 1 for a 1x export (Figma, 390 px wide), 2 for 600 to 1079 px (750, 828), 3 for 1080 px and up.
It comes from the width (see scale()) unless --scale says otherwise. Needs: pip install pillow numpy
opencv-python-headless rapidocr_onnxruntime (exit 2 and the line to run when one is missing).
"""
import argparse
import json
import pathlib
import re
import sys

NEED = {'PIL': 'pillow', 'numpy': 'numpy', 'cv2': 'opencv-python-headless', 'rapidocr_onnxruntime': 'rapidocr_onnxruntime'}
FONTS = ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/Library/Fonts/Arial.ttf',
         '/System/Library/Fonts/Supplemental/Arial.ttf', '/System/Library/Fonts/Helvetica.ttc',
         'C:/Windows/Fonts/arial.ttf']


def need(*mods):
    missing = []
    for m in mods:
        try:
            __import__(m)
        except ImportError:
            missing.append(NEED[m])
    if missing:
        print('pip install ' + ' '.join(missing), file=sys.stderr)
        print('prep.py needs the packages above; run that line and try again.', file=sys.stderr)
        sys.exit(2)


def scale(w):
    """Points to pixels from the screenshot's width: under 600 -> 1 (a 1x export), 600 to 1079 -> 2, 1080 and up -> 3.

    This is min(3, max(1, round(w / 400))) except that the 2x/3x boundary stays at 1080 (as in the pipeline that
    made the rules): the plain rounding would call a 1023 px wide screenshot 3x.
    """
    return 1 if w < 600 else 2 if w < 1080 else 3


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


def load(path):
    """The image as RGB. A picture with transparency is laid on white; a phone's rotation tag is applied."""
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(path))
    if im.mode in ('RGBA', 'LA', 'PA') or (im.mode == 'P' and 'transparency' in im.info):
        im = im.convert('RGBA')
        bg = Image.new('RGBA', im.size, (255, 255, 255, 255))
        bg.alpha_composite(im)
        im = bg
    return im.convert('RGB')


def read_lines(path):
    from rapidocr_onnxruntime import RapidOCR
    res, _ = RapidOCR(intra_op_num_threads=2)(str(path))
    lines = []
    for i, (q, text, conf) in enumerate(res or [], 1):
        xs, ys = [p[0] for p in q], [p[1] for p in q]
        lines.append({'i': i, 'text': text, 'conf': round(float(conf), 2),
                      'box': [int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys))]})
    return lines


def grid(im, ocr, dest):
    from PIL import Image, ImageDraw
    W, H = im.size
    k = 640 / W
    g = im.resize((640, round(H * k)), Image.LANCZOS).convert('RGBA')
    over = Image.new('RGBA', g.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    f = font(13)
    gw, gh = g.size
    for p in range(5, 100, 5):
        a = 150 if p % 10 == 0 else 70
        d.line([(gw * p / 100, 0), (gw * p / 100, gh)], fill=(0, 200, 190, a), width=1)
        d.line([(0, gh * p / 100), (gw, gh * p / 100)], fill=(0, 200, 190, a), width=1)
        if p % 10 == 0:
            for x, y in ((gw * p / 100 + 2, 2), (2, gh * p / 100 + 1)):
                d.rectangle([x - 1, y, x + 20, y + 14], fill=(0, 0, 0, 170))
                d.text((x, y), str(p), font=f, fill=(255, 255, 255, 255))
    for ln in ocr['lines']:
        x0, y0, x1, y1 = [v * k for v in ln['box']]
        d.rectangle([x0, y0, x1, y1], outline=(255, 140, 0, 200), width=1)
        tag = str(ln['i'])
        d.rectangle([x0 - 2, y0 - 13, x0 + 8 * len(tag) + 2, y0], fill=(255, 140, 0, 230))
        d.text((x0, y0 - 14), tag, font=f, fill=(0, 0, 0, 255))
    Image.alpha_composite(g, over).convert('RGB').save(dest, quality=88)


def main():
    ap = argparse.ArgumentParser(description='Prepare one screenshot for the screen linter.')
    ap.add_argument('image', help='path to the screenshot (png, jpg, webp)')
    ap.add_argument('--out', required=True, help='folder for img.png, ocr.json, grid.jpg')
    ap.add_argument('--scale', type=int, choices=(1, 2, 3), help='points-to-pixels; default from the width')
    a = ap.parse_args()
    need('PIL', 'numpy', 'cv2', 'rapidocr_onnxruntime')
    src = pathlib.Path(a.image).expanduser()
    if not src.is_file():
        sys.exit(f'prep.py: {src} is not a file')
    out = pathlib.Path(a.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    im = load(src)
    W, H = im.size
    im.save(out / 'img.png')
    ocr = {'id': re.sub(r'[^a-z0-9]+', '-', src.stem.lower()).strip('-') or 'screen', 'W': W, 'H': H,
           'scale': a.scale or scale(W), 'lines': read_lines(out / 'img.png')}
    (out / 'ocr.json').write_text(json.dumps(ocr, indent=1) + '\n')
    grid(im, ocr, out / 'grid.jpg')
    print(f"{out}: {W}x{H} px, scale {ocr['scale']}, {len(ocr['lines'])} text lines (img.png, ocr.json, grid.jpg)")
    if not 1.5 <= H / W <= 2.6:
        print(f'note: {W}x{H} is not a phone screenshot shape (height/width {H / W:.2f}); '
              'the rules are for iPhone app screens, so check that it is one before going on')
    if not 380 <= W <= 1300:
        print(f'note: {W} px wide is outside the iPhone range (390 to 1290)')


if __name__ == '__main__':
    main()
