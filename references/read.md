# Reading one screen: how to write obs.json

The linter grades a screen against rules made from many checked screens of its type. It needs one thing a script
cannot do well: say what is on the screen. You write that down as one JSON file, `DIR/obs.json`. You describe;
you do not judge. The scripts do the measuring (contrast, sizes, positions) and the grading from what you write.

`DIR` is the work folder `prep.py` filled. `SK` below is the skill folder, `~/.claude/skills/screen-lint`. Read
`SK/types/<t>.md` first: it names the type's parts, subtypes and pitfalls, with the part keys you fill in.

## Steps

1. Look at `DIR/img.png`, the clean screenshot. Judge what things are from this one.
2. Look at `DIR/grid.jpg`: the same screen at 640 px wide with a teal grid every 5% (numbers every 10%, along the
   top and left edges) and an orange box with a number on every text line the OCR found. Use it to read positions in
   percent and line numbers.
3. Read `DIR/ocr.json` for each line's number (`i`) and text. The OCR can misread or merge lines; cite the
   number of the line that covers the thing and say so in `notes`.
4. Write `DIR/obs.json` (schema below), then run
   `python3 SK/scripts/check_obs.py DIR/obs.json --ocr DIR/ocr.json` until it prints `OK`.

## Schema

```json
{
  "id": "<name of the image>",
  "type": "<t>",
  "is_type": true,
  "instead": "",
  "variants": ["v2"],
  "new_variant": "",
  "state": "normal",
  "dark": false,
  "parts": {
    "1": {"present": true, "boxes": [[6, 86, 94, 92]], "lines": [14]},
    "2": {"present": false}
  },
  "controls": [{"role": "primary", "box": [6, 86, 94, 92], "lines": [14]}],
  "pitfalls": {"1": {"seen": false, "evidence": ""}},
  "inactive": [],
  "placeholder": [],
  "extra": [],
  "notes": ""
}
```

`parts` and `pitfalls` hold every key `types/<t>.md` lists (two are shown). Boxes are `[x0, y0, x1, y1]` in
percent of the whole screen's width and height (0 to 100), read off the grid, tight around the drawn thing.
`lines` are OCR line numbers `i`; `[]` when the OCR missed the text.

- **is_type**: true when the screen does the job the type section gives under "What it is for". The type came
  from a look at the picture, so check it now. False when it is another type: `instead` is the best key from
  `references/types.md` (or `other`), and every other field keeps its empty value: `variants` `[]`, `new_variant`
  `""`, `state` `"normal"`, `dark` false, `parts` `{}`, `controls` `[]`, `pitfalls` `{}`, `inactive` `[]`,
  `placeholder` `[]`, `extra` `[]`. `notes` may say why.
  When true, `instead` is `""`. `lint.py` grades nothing for a false and exits 3: go back to the classifier with
  the type you named.
- **variants**: every listed subtype (`v1`, `v2`, ...) the screen is: usually one, several when they combine.
  **new_variant**: when none of the listed subtypes fits, 2 to 5 words naming what this screen is (and `variants`
  is `[]`); else `""`.
- **state**: `normal`; `empty` (nothing to show yet: no results, no items); `loading` (a spinner, skeleton or
  placeholder stands where content will be); `error` (an error message or a failed load is the main thing);
  `dimmed` (an alert, a spinner layer or another sheet's dark layer covers the screen; contrast is not measured
  then). A sheet that is itself the screen, with its dark layer behind it, is not dimmed.
- **dark**: true when the screen is dark by design (dark mode, or a dark brand colour), false when light. A
  dimming layer does not make it dark.
- **parts**: one entry for every part in the type section's table, keyed by its number as text. Present when you
  can see it, even if small or faint; `{"present": false}` when it is not on the screen. Present: one box per
  instance (a list of rows gives one box per visible row, up to 12), in reading order, so the first box is the
  topmost; `lines` are the OCR lines of the part's text, all instances together. A part that names a lack or
  covers the whole screen ("Nothing to tap", "Flat colour fills the screen") is present when it holds, and its box
  is the whole screen, `[0, 0, 100, 100]`.
- **controls**: the tappable things the platform checks need, each `{role, box, lines}`. Roles: `primary` (the
  main filled action), `secondary` (other buttons, and text buttons such as Not Now or Skip), `close` (an X
  glyph), `back` (a back chevron or arrow), `field` (a text input). For `close` and `back` the box is tight around
  the drawn glyph, with its circle if it has one. Leave out list rows, tab bars, keyboards and the home
  indicator. `[]` when there are none.
- **pitfalls**: every pitfall in the type section, by its number: `seen` true only when the screen clearly shows
  it, with `evidence` one short sentence naming what you see; else `{"seen": false, "evidence": ""}`.
- **inactive**: OCR line numbers of the labels of greyed-out controls, ones that cannot be tapped yet (a Continue
  button pale until a field is filled, a dimmed Send). Their contrast is not measured: accessibility guidelines leave
  out controls that cannot be used. Only when the screen clearly shows the control is off; `[]` otherwise.
- **placeholder**: OCR line numbers of placeholder text, the grey prompt inside an empty field that goes away when
  typing starts ("Email", "Search", "Write a message"). Its contrast is a hint only. Not a field's label above it,
  not text someone has typed. `[]` when none.
- **extra**: up to 3 short phrases (12 words at most) for notable things the parts table has no row for, a habit
  of this screen. `[]` when none.
- **notes**: one sentence when something was hard to decide or the OCR misread a line you used; `""` otherwise.
  If an OCR line merges two things, use its number when it covers the thing and say so here.

Describe, do not judge: say what is on the screen, not whether it is good, and do not guess what is outside the
screenshot. When you cannot tell, write what you see and put the doubt in `notes`.

## When check_obs.py says BAD

It prints one problem per line and exits 1. The usual ones: a part or pitfall key missing (every key must be
there), a box that is not four numbers in 0 to 100 with x1 > x0 and y1 > y0, a line number the OCR did not
find, `variants` and `new_variant` both set or both empty, a present part with no box, a `seen` pitfall with
no evidence. Fix the file and run it again; do not run `lint.py` on a reading that is not OK.
