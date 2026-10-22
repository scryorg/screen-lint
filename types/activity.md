# This type: Activity (`activity`)

Also called: in-progress screen, lesson step, quiz question, timer, live session, game screen
What it is for: Holds the person on one task while it runs, with one clear control to move on or stop.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 9 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Main control in the bottom third | A wide button (Next, Continue, Check, Run) or one round button (stop, spin). On Ahead, Wish, HQ Trivia and 11 more. |
| 2 | Close X or back arrow at the top | Citizen has an End button at the top instead. On Ahead, Wish, HelloFresh and 11 more. |
| 3 | Progress or live readout | A bar, dots, a step count, a timer, a ring or a percent. On Ahead, HelloFresh, Uxcel Go and 9 more. |
| 4 | Full-bleed color, dark or art background | Pink, green, navy, black, a game scene or a dark map. The rest are white or a map. On Ahead, Wish, HQ Trivia and 9 more. |
| 5 | One question or instruction line | Short plain text above the work area. On Ahead, HelloFresh, Uxcel Go and 5 more. |
| 6 | Answer area under the question | Tiles, bubbles, a number grid or a keypad. Not Boring Calculator is a calculator keypad with no question. On Uxcel Go, Brilliant, Duolingo Math and 4 more. |
| 7 | Stop or finish control named with a verb | Finish Early, End, STOP CHARGING, Stop playing, finish yap. On pillowtalk, Brightmind, Citizen and 2 more. |
| 8 | Map behind the task | A trip or an order shown on a map. On Uber Eats, inDrive, Citizen and Beat Passenger. |
| 9 | Panel, sheet or alert layered at the bottom | Feedback panel on Brilliant, action sheet on inDrive and Tribe. On Brilliant, inDrive and Tribe. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Lesson or quiz step: One question or task at a time, a progress mark at the top and one button to move on.
- `v2` Timer or live tool: A timer, a voice session, a charge or a calculator fills the screen around one big readout or one control.
- `v3` Game: Full-screen game art with one tap target such as Spin, Start or a pause sheet.
- `v4` Trip or order on a map: A map with status, a route or a driver, and a card or sheet of actions.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Faint grey buttons at the bottom are easy to miss: Continue on Uxcel Go and Cancel on Uber Eats.
2. The instruction is small and pale next to the artwork.
3. Dense small type or tiny numbers sit in the screen while the person is busy with a task.

## What the checked screens of each subtype have (the linter expects the same)

50 checked screens of this type; screens per subtype (a screen can be more than one): v1 13, v2 14, v3 7, v4 9.

- `v1` Lesson or quiz step
  - A progress mark and one question or instruction line near the top
  - An answer area of tiles, bubbles or a keypad right under the question
  - A close X or back arrow at the top and one main button in the bottom third
- `v2` Timer or live tool
  - A full-bleed color or dark background that takes over the screen
  - One big readout, such as a timer, a ring or a percent
  - One main control low on the screen
- `v3` Game
- `v4` Trip or order map
  - A map behind the task
  - A status readout, a stop or cancel control, or a sheet layered over the map
  - No answer tiles: the task is a status, not a question

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
