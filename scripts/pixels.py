#!/usr/bin/env python3
"""Pixel measuring for the screen linter: contrast, drawn size and position, from a screenshot and a box.

    from pixels import lum, ratio, text_contrast, glyph, button, text_pt, pct, union, blocks, busy

The first eight functions are copied unchanged from lint.py (Paywall v1); `pct`, `union` and `blocks` are the
small helpers lint.py keeps beside them. `busy` is new: it says when the colour around a line is a photo or a
pattern, where a text contrast cannot be measured. Boxes are pixels [x0, y0, x1, y1]; `s` is the screen's scale
(2 or 3, from out/ocr/<id>.json).
"""
import cv2
import numpy as np


# ---------- measuring ----------

def lum(rgb):
    c = np.asarray(rgb, float) / 255
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return float(c @ [0.2126, 0.7152, 0.0722])


def ratio(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def ring(a, t=2):
    t = max(1, min(t, a.shape[0] // 3, a.shape[1] // 3))
    return np.concatenate([a[:t].reshape(-1, 3), a[-t:].reshape(-1, 3), a[:, :t].reshape(-1, 3), a[:, -t:].reshape(-1, 3)])


def crop(img, box, pad=0):
    H, W = img.shape[:2]
    x0, y0 = max(0, int(box[0] - pad)), max(0, int(box[1] - pad))
    x1, y1 = min(W, int(box[2] + pad)), min(H, int(box[3] + pad))
    return img[y0:y1, x0:x1], (x0, y0, x1, y1)


def text_contrast(img, box, s):
    """Text against what is behind it: the background is the colour around the line, the text is the 5% of
    pixels that differ from it most (the cores of the strokes, past the anti-aliasing)."""
    a, _ = crop(img, box, pad=2 * s)
    bg = np.median(ring(a, s), axis=0)
    px = a.reshape(-1, 3).astype(float)
    d = np.linalg.norm(px - bg, axis=1)
    return ratio(bg, px[d >= np.quantile(d, 0.95)].mean(axis=0))


def glyph(img, box, s):
    """The drawn close or back control near the detector's box: its tight box and its contrast."""
    m = max(box[2] - box[0], box[3] - box[1]) * 0.25 + 2 * s
    a, (ox, oy, _, _) = crop(img, box, pad=m)
    bg = np.median(ring(a, s), axis=0)
    d = np.linalg.norm(a.astype(float) - bg, axis=2)
    # the strongest edge inside the detector's own box, so a photo or card next to the control does not set it
    hi = np.quantile(d[int(box[1] - oy):int(box[3] - oy), int(box[0] - ox):int(box[2] - ox)], 0.99)
    if hi < 8:
        return None
    n, lab, st, _ = cv2.connectedComponentsWithStats((d > 0.5 * hi).astype(np.uint8), connectivity=8)
    cx, cy = (box[0] + box[2]) / 2 - ox, (box[1] + box[3]) / 2 - oy
    best = None
    for i in range(1, n):
        x, y, w, h, area = st[i]
        if area < (2 * s) ** 2:
            continue
        gap = np.hypot(max(x - cx, 0, cx - x - w), max(y - cy, 0, cy - y - h))
        if best is None or (gap, -area) < best[:2]:
            best = (gap, -area, i)
    if best is None:
        return None
    i = best[2]
    x, y, w, h, area = st[i]
    comp = lab == i
    fg = a[comp].astype(float)
    df = np.linalg.norm(fg - bg, axis=1)
    r = ratio(bg, fg[df >= np.median(df)].mean(axis=0))
    if area / (w * h) > 0.6:
        # a filled circle or square with the glyph inside it: the glyph against the shape counts too
        inner = a[y:y + h, x:x + w].astype(float)
        shape = np.median(inner[comp[y:y + h, x:x + w]], axis=0)
        di = np.linalg.norm(inner - shape, axis=2)
        if np.quantile(di, 0.98) > 8:
            r = max(r, ratio(shape, inner[di >= np.quantile(di, 0.98)].mean(axis=0)))
    return {'box': [int(ox + x), int(oy + y), int(ox + x + w), int(oy + y + h)], 'contrast': r}


def button(img, box, labels, s):
    """A main button's filled shape, found from the colour just around its label. None when it is not filled."""
    H, W = img.shape[:2]
    if not labels:
        return None
    lab_box = [min(b[0] for b in labels), min(b[1] for b in labels), max(b[2] for b in labels), max(b[3] for b in labels)]
    around, _ = crop(img, lab_box, pad=4 * s)
    fill = np.median(ring(around, 2 * s), axis=0)
    a, (ox, oy, _, _) = crop(img, box, pad=3 * s + 0.03 * W)
    d = np.linalg.norm(a.astype(float) - fill, axis=2)
    n, lab, st, _ = cv2.connectedComponentsWithStats((d < 40).astype(np.uint8), connectivity=4)
    r, (rx0, ry0, _, _) = crop(lab, [lab_box[0] - ox, lab_box[1] - oy, lab_box[2] - ox, lab_box[3] - oy], pad=4 * s)
    ids = ring(np.repeat(r[..., None], 3, axis=2), 2 * s)[:, 0]
    ids = ids[ids > 0]
    if not len(ids):
        return None
    i = np.bincount(ids).argmax()
    x, y, w, h, _ = st[i]
    if h > 0.3 * H or h < 20 * s:
        return None   # the label sits on the page itself, not on a button of its own
    return [int(ox + x), int(oy + y), int(ox + x + w), int(oy + y + h)]


def pct(b, W, H):
    return [b[0] * W / 100, b[1] * H / 100, b[2] * W / 100, b[3] * H / 100]


def union(bs):
    return [min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)] if bs else None


def text_pt(ln, s):
    # RapidOCR's line box comes out close to the font size; checked on the status bar clock (17 pt) and on line pitch
    return (ln['box'][3] - ln['box'][1]) / s


def blocks(lines):
    """Runs of lines that sit one under the other, as one paragraph each."""
    out = []
    for ln in sorted(lines, key=lambda l: l['box'][1]):
        h = ln['box'][3] - ln['box'][1]
        if out and ln['box'][1] - out[-1][-1]['box'][3] < 1.5 * h:
            out[-1].append(ln)
        else:
            out.append([ln])
    return out


def busy(img, box, s):
    """True when the colour around a line is not one flat colour or a soft gradient (a photo, a pattern, a
    video frame). The ring that text_contrast takes its background from is read; neighbouring text can spoil a
    few pixels of it, so the spread is taken between the 10th and 90th percentile, not the extremes."""
    a, _ = crop(img, box, pad=2 * s)
    g = ring(a, s).astype(float) @ [0.299, 0.587, 0.114] / 255
    return bool(np.quantile(g, 0.9) - np.quantile(g, 0.1) > 0.15)
