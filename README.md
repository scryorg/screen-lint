# screen-lint

A Claude Code skill that finds the type of an iPhone app screen and lints it against what screens of that type
usually have.

Give it a screenshot (or a 1x Figma frame export). It picks one of 35 screen types, writes down what is on the
screen, checks that against rules mined from many checked screens of the same type, measures contrast, text size,
tap-target size and safe-area position from the pixels, and answers with a grade A to F, numbered findings and a
marked-up copy of the screenshot.

```
Screen type: Permission (subtype: App asks first + Several asks on one screen). Runner-up: Setup, because it is also a step before the app opens.
Grade: B (0 errors, 2 warnings, 0 hints)
 1. WARN   presence/3            No picture or icon on the screen.
           Why: 39 of 58 checked screens have "Picture or icon".
 2. WARN   platform/text-contrast  The typical line of the Reason written in the app's own words is 4.2:1 against
                                 its background; text this size needs 4.5:1.
Not checked: what happens after the tap (the phone's own dialog comes next) ...
Marked-up copy: DIR/overlay.png
```

The grade measures how closely a screen follows what most checked screens of its type do, plus Apple's size and
contrast rules. It is not a measure of quality or of what users prefer.

## The 35 types

| Family | Types |
|---|---|
| Getting in | splash, welcome, sign-in, verify, permission, setup |
| Finding | home, feed, catalog, search, filter, map |
| Viewing | detail, article, player, gallery, profile |
| Making and talking | chat, inbox, compose, camera, form, share |
| Tracking | calendar, stats, activity, list, notifications |
| Managing | settings, account, help, menu |
| Paying | paywall, checkout, confirmation |

`references/types.md` says what each type is for, how to tell it and what it is confused with.

## Install

```
git clone https://github.com/scryorg/screen-lint ~/.claude/skills/screen-lint
pip install pillow numpy opencv-python-headless rapidocr_onnxruntime
```

Python 3.8 or newer. The scripts run locally, with no network and no paid API; the looking (type, parts, pitfalls)
is done by Claude in your session.

## Use

In Claude Code: "lint this screen: ~/Desktop/shot.png", "grade these three screenshots", "what type of screen is
this", or `/screen-lint <path>`. A folder of screenshots is fine; past 8 screens the skill fans out subagents.

`SKILL.md` has the full workflow. The scripts can also be run by hand:

```
S=~/.claude/skills/screen-lint/scripts
python3 $S/prep.py shot.png --out out/shot            # img.png, ocr.json, grid.jpg
# write out/shot/obs.json as references/read.md says (this is the step Claude does)
python3 $S/check_obs.py out/shot/obs.json --ocr out/shot/ocr.json
python3 $S/lint.py --type paywall --obs out/shot/obs.json --img out/shot/img.png --ocr out/shot/ocr.json --json out/shot/lint.json
python3 $S/overlay.py out/shot                         # out/shot/overlay.png
```

## How the rules were made

For each type, 64 checked screens were read the same way the skill reads yours (1,939 of the 2,240 were really that
type), and a second blind reading measured how well readers agree. From those readings:

- **Conventions** (warnings): a part most screens of the type have, such as a price on a paywall. A rule fires only
  when the lower bound of its share across checked screens is high enough, and subtypes with 8 or more screens get
  their own expectations and exemptions.
- **Pitfalls** (errors): known mistakes for the type, each with a test the script can run.
- **Platform** (errors or warnings): text contrast 4.5:1 (3:1 for large text), controls 3:1, text size, 44 pt tap
  targets, and nothing under the status bar or home indicator. Contrast is not measured on a dimmed screen, over a
  photo, or on the label of a greyed-out button; faint placeholder text in an empty field is only a hint.

Grades: A is no errors and at most 1 warning, B no errors, C one error, D two, F three or more. Each rule counts
once however many places it fires; hints never count.

## How well it works

Tested on 280 held-out screens the rules never saw, with Claude Sonnet following `SKILL.md`:

- Type: 193 of 280 match an earlier model label; a model judge sided with the skill on 78 of the other 87. The
  judge reads the same type guide, so that is generous; an eye check of 36 of those puts the real rate at about
  85 to 90%. Sheets and popups are typed by the sheet, so `list`, `form` and `menu` come up often.
- Linted 273 (7 were not app screens of any type). Grades A150, B52, C60, D10, F1.
- Run twice on 35 screens: the same type on 34, the same grade on 31 of 34, and 75% of findings the same.

Rules are for iPhone app screens only, not web pages, iPad or desktop apps.

## Files

| Path | What |
|---|---|
| `SKILL.md` | the workflow Claude follows |
| `references/types.md` | the classifier: 35 types in 7 families |
| `references/read.md` | how to write `obs.json` for one screen |
| `types/<t>.md` | each type's parts, subtypes and pitfalls |
| `rules/<t>.json` | the rules the linter applies for each type |
| `scripts/` | `prep.py`, `check_obs.py`, `lint.py`, `overlay.py`, `pixels.py` |

## License

MIT. See `LICENSE`.
