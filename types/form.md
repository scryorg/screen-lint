# This type: Form (`form`)

Also called: data entry screen, input form, edit sheet, details screen, add item
What it is for: Collect a few facts, choices or amounts from the person so the app can save, book, send or change something.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Title or heading that names the task | Qantas Airways and Tempo start mid-scroll with no title in view. |
| 2 | Way out (Cancel word, back arrow or X) | Cancel word on 9 (Artifact, Done, Co–Star and 6 more), back arrow on 9 (HabitMinder, Afterpay, HBX and 6 more), X alone on Toggl Track. |
| 3 | Picker, tick box, toggle, dropdown, chips or date wheel | Done, Co–Star, Toggl Track and 14 more. |
| 4 | Text or number field | Artifact, Done, Co–Star and 13 more. |
| 5 | Filled commit button at the bottom | HabitMinder, Crate & Barrel, YNAB and 10 more. |
| 6 | Label above the field | Artifact, Done, Co–Star and 5 more. On Afterpay, Shopify, Warby Parker and Lightyear the label sits inside the box. |
| 7 | Commit action in the top bar | Save, Send, Create or Next on Artifact, Done, Co–Star and 3 more. |
| 8 | Sheet with a rounded top edge | Artifact, Co–Star, Toggl Track and 3 more. |
| 9 | Optional or required mark | 'Optional' on Co–Star, Afterpay, Credit Karma and Lightyear. 'Required' on every field of Crate & Barrel. |
| 10 | Keyboard open | Artifact, Toggl Track, Afterpay and Unsplash. Co–Star shows a date wheel in its place. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Cancel and Save in the top bar: Cancel on the left, the action on the right, fields below, usually a keyboard or wheel.
- `v2` Full page with labelled fields: A stack of labelled boxes with a Back arrow and one button below or after them.
- `v3` Single question or choice: One dropdown, one yes or no, a short list of reasons or two cards to pick between, then one button.
- `v4` Amount, goal or review entry: Numbers and choices for a goal, a swap, a card offer or a withdrawal, often with a summary and one confirm button.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. No submit control is in view because the keyboard covers it or the form scrolls.
2. The commit button looks switched off and nothing says what is missing.
3. Tiny capital labels and day chips are hard to read (Done), and a block of small print comes before the question (Qantas Airways).

## What the checked screens of each subtype have (the linter expects the same)

60 checked screens of this type; screens per subtype (a screen can be more than one): v1 18, v2 21, v3 13, v4 8.

- `v1` Top bar actions
  - A way out and the commit action both sit in the top bar
  - No filled button at the bottom of the page
  - A title that names the task
  - Text fields and pickers below the bar
- `v2` Labelled field page
  - A way out and a title at the top
  - Text or number fields make up the page
  - One filled button to finish, not an action in the top bar
- `v3` Single choice
  - A way out and a title at the top
  - One question answered with a picker, tick box, toggle or list
  - Almost no typed fields
  - One filled button to confirm, usually at the bottom
- `v4` Amount or review
  - A title that names the task
  - A text or number field and a picker for the choice
  - One filled button at the bottom to confirm

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
