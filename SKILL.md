---
name: screen-lint
description: Classify an iPhone app screen into one of 35 screen types (splash, welcome, sign-in, verify, permission, setup, home, feed, catalog, search, filter, map, detail, article, player, gallery, profile, chat, inbox, compose, camera, form, share, calendar, stats, activity, list, notifications, settings, account, help, menu, paywall, checkout, confirmation) and lint it against rules mined from many checked screens of that type - missing parts, known pitfalls, contrast, tap-target size and position - then give a grade A to F, numbered findings, and a marked-up copy of the screenshot. Use when the user says "lint this screen", "grade this screen", "review / critique this screenshot", "audit this app screen", "what type of screen is this", "does this paywall / sign-in / onboarding / settings screen follow conventions", "is this missing anything", "check this app screen for contrast or tap targets", shares or `/ss` snips an iPhone app screen or Figma iPhone frame export and wants it judged, or asks for a batch of screens to be graded. Rules are for iPhone app screens only, not web pages, desktop apps, iPad or photos (say so and stop). Not for pixel diffs against Figma (Design Sync) or for timing and flicker (visual-smells).
---

# screen-lint

A screen belongs to one of 35 types, and most good screens of a type share the same parts: a paywall shows a
price, a sign-in has a way back, a settings list groups its rows. This skill finds the type of an iPhone screenshot,
reads what is on it, and checks it against what the checked screens of that type have in common (64 read per type,
1,939 of them really that type), plus Apple's size and contrast rules measured from the pixels. It answers with a grade, numbered findings and a marked-up copy.

The grade measures how closely the screen follows what most checked screens of its type do, and Apple's size and
contrast rules. It is not a measure of quality or of what users prefer. Say that once in every answer.

Two halves: you look and describe (type, parts, controls, pitfalls); the scripts measure and decide. You never
grade by eye. A reading that does not pass `check_obs.py` is never linted.

## Files

| Path | What |
|---|---|
| `references/types.md` | the classifier: the 35 types in 7 families, what each is for, how to tell it, what it is confused with |
| `references/read.md` | how to write `obs.json` for one screen: the schema and the rule for each field |
| `types/<t>.md` | the reader's section for type `t`: its parts, subtypes and pitfalls, and what each subtype has (35 files) |
| `rules/<t>.json` | the rules the linter applies for type `t`, with the grade table and the shape `check_obs.py` checks (35 files) |
| `scripts/prep.py` | `prep.py <image> --out DIR [--scale N]` writes `DIR/img.png`, `DIR/ocr.json`, `DIR/grid.jpg` |
| `scripts/check_obs.py` | `check_obs.py DIR/obs.json --ocr DIR/ocr.json` prints `OK`, or `BAD` and the problems (exit 1) |
| `scripts/lint.py` | `lint.py --type T --obs DIR/obs.json --img DIR/img.png --ocr DIR/ocr.json --json DIR/lint.json` grades and prints the findings |
| `scripts/overlay.py` | `overlay.py DIR` writes `DIR/overlay.png`: finding boxes in coral, numbered as in the answer |
| `scripts/pixels.py` | contrast, glyph, button and text-size measurements `lint.py` uses |

The scripts need Python 3.8 or newer and run locally and free, with no network and no paid API. If one reports a
missing package, run the single line it prints, normally
`pip install pillow numpy opencv-python-headless rapidocr_onnxruntime`, then rerun the same command (exit 2).

## Workflow

1. **Get the image.** A file path: use it. `/ss`, "this snip" or "my latest screenshot": follow the `ss` skill,
   Scry MCP `latest_capture` (or `get_capture` for an id), then download its "Original, full resolution" link with
   `curl -4 -o DIR/in.png <link>`; the inline picture is downscaled and too small to lint. An image URL: download it
   the same way. Work folder `DIR`: the session scratchpad plus the image name if there is one, else
   `./screen-lint-out/<name>/`. One folder per screen.
2. **Prep.** `python3 ~/.claude/skills/screen-lint/scripts/prep.py <image> --out DIR`. It makes the clean
   `img.png`, the OCR lines in `ocr.json`, and `grid.jpg` (a percent grid with every text line numbered). It prints
   a note if the shape is not a phone's. A 1x Figma export (390 px wide) and a 2x or 3x screenshot all work.
3. **Classify.** Read `references/types.md`, look at `DIR/img.png` and `DIR/grid.jpg`, and pick the type and a
   runner-up, each with one sentence saying what on the screen decides it. Use the "Tell it by" and "Mistaken for"
   lines. Two cases end the run:
   - Not an iPhone app screen (a web page, an iPad or desktop app, a photo, a chart on its own): say so, say the
     rules are for iPhone app screens, and stop.
   - A phone screen that fits no type (`other`: a system alert on its own, a lock screen, a home-screen widget):
     say which type is closest and that no rules fit; stop.
4. **Read.** Read `references/read.md` and `types/<t>.md` for the type you picked. Write `DIR/obs.json`, then run
   `python3 ~/.claude/skills/screen-lint/scripts/check_obs.py DIR/obs.json --ocr DIR/ocr.json` and fix what it lists
   until it prints `OK`. If looking closely shows the screen does something else, write `is_type` false with
   `instead` (the better key, or `other`), and go back to step 3 with that type; do not lint a screen against a
   type it is not.
5. **Lint and mark up.**
   ```
   S=~/.claude/skills/screen-lint/scripts
   python3 $S/lint.py --type T --obs DIR/obs.json --img DIR/img.png --ocr DIR/ocr.json --json DIR/lint.json
   python3 $S/overlay.py DIR
   ```
   `lint.py` exits 0 graded, 1 the reading failed `check_obs.py`, 2 a missing file or package, 3 the reading says
   the screen is not type T (nothing graded; go back to step 3). Then look at `DIR/overlay.png` once: the boxes
   should sit on the things the findings name. A finding whose box is on the wrong thing means the reading's box
   or line number is off: fix `obs.json`, check it, and run both scripts again.
6. **Answer** in this shape, one block per screen:
   ```
   Screen type: Paywall (subtype: Plan picker). Runner-up: Account, because it also lists the current plan.
   Grade: C (1 error, 2 warnings, 1 hint)
    1. ERROR  pitfall/1   <says>
              Why: <why>
    2. WARN   presence/3  <says>
              Why: <why>
   Not checked: <the list lint.py prints>
   Marked-up copy: DIR/overlay.png
   ```
   Findings in the order `lint.py` prints them (errors, then warnings, then hints) and with its numbers, so they
   match the boxes on the overlay. Use each finding's `says` and `why` as given; do not reword them into advice of
   your own, and add a fix only when the user asks. A subtype that is `new_variant` is stated as "a subtype the
   checked screens do not list: <name>", and the subtype expectations are then not applied. Give the caveat above
   once, in a line at the end. For grade A with no findings, say what was checked and that nothing fired.
7. **Several screens.** Do steps 2 to 6 for each, one `DIR` per screen, and end with a table of screen, type, grade
   and number of errors. More than 8 screens: fan out subagents, 4 screens each, each following steps 2 to 5 and
   returning the paths of its `lint.json` and `overlay.png`; then write the table and the per-screen answers from
   those files yourself.

## Gotchas

- The grade counts each rule once, however many places it fires: A is no errors and at most 1 warning, B no errors,
  C one error, D two, F three or more. Hints never count. Do not recompute it.
- Look at the picture to decide what a thing is; use `grid.jpg` only for positions in percent and line numbers.
  The OCR can split or merge lines: cite the line that covers the thing and put the doubt in `notes`.
- A dimmed screen (an alert, a sheet's dark layer, a spinner layer over everything) is `state: "dimmed"`; contrast
  is then not measured. A screen that is dark by design is `dark: true`.
- Describe, do not judge: the reading says what is on the screen; the rules say whether it is enough. Do not set a
  pitfall `seen` to be safe, and do not leave a present part out to avoid a finding.
- A new subtype or a screen that is more than one subtype is fine; say so in the answer.
- One screenshot is one screen. A tall scrolling capture, or several phones in one image, is read for the part in
  view; say what was left out, and ask for the screens one by one when it matters.
- Nothing here names or relies on any outside screenshot library. Say "checked screens" when you cite the evidence
  behind a rule.
- Never grade a screen against the rules of a type it was not read as. The type in `obs.json` and the `--type` of
  `lint.py` must be the same.
