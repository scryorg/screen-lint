# This type: Calendar (`calendar`)

Also called: date picker, time picker, schedule, agenda, booking slots, date range picker
What it is for: Lets the person pick a date or a time, or read what is planned on which day.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Title at the top, in the bar or on the sheet | Most name the task in plain words, such as Choose Dates or Select a date and time. On Freenow, Grab, Instacart and 16 more. |
| 2 | Clock time shown or picked | Wheel, slot chips, a small field, or times beside events. On Freenow, Grab, Instacart and 10 more. |
| 3 | Selected day marked with a fill or ring | A filled circle, a ring or a filled chip. On Instacart, Hyundai Card, Calendly and 6 more. |
| 4 | Filled button in the bottom third | Two of them are pale grey, so they read as not ready yet (CapWords and GetYourGuide). On Freenow, Grab, Instacart and 6 more. |
| 5 | Opens as a sheet over a dimmed screen | The date is one step of a larger task. On Grab, Instacart, Canopi and 6 more. |
| 6 | Month name as a label or heading | Plain text, a dropdown or a pair of arrows. On Hyundai Card, Calendly, Spotify and 5 more. |
| 7 | Month grid of days in 7 columns | Six have a weekday row on top. Locket uses dots to show history, not to pick a date. On Hyundai Card, Calendly, Spotify and 4 more. |
| 8 | Short sentence of rules or context near the picker | Cancel terms, time zone, or what the booking is. On Freenow, Grab, Instacart and 4 more. |
| 9 | Week strip or row of day chips | A row of days to tap, used instead of a full grid. On Instacart, Tripsy, Zendesk Support and 2 more. |
| 10 | Rows of events under dated headings | These are read, not picked. On Formula 1®, Tripsy, Google Calendar and 2 more. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Month grid: A 7-column grid of days to pick a date or a range; Locket uses a grid of dots to show a history instead.
- `v2` Wheel or slot picker: A wheel or a list of slots picks one time of day; Instacart, Zillow and GetYourGuide put the slots under a day.
- `v3` Agenda or schedule list: Rows of events under day headings that are read, not picked.
- `v4` Plain fields or a strip: The date or time sits in one or two small fields, or in a week strip, with no grid.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Wheel rows above and below the chosen time fade until they are hard to read.
2. A long block of text sits above the date control and pushes it to the bottom edge of the screen.
3. Day numbers and the figures under them are small and pale: amounts under each day on Hyundai Card, light grey numbers on Hopper.

## What the checked screens of each subtype have (the linter expects the same)

62 checked screens of this type; screens per subtype (a screen can be more than one): v1 25, v2 21, v3 17, v4 9.

- `v1` Month grid
  - A grid of days in seven columns, in the middle of the screen
  - A month name as a label or heading above the grid
  - The chosen day marked with a fill or a ring
  - A title at the top
- `v2` Wheel or slot picker
  - A clock time shown on a wheel or as slots
  - A sheet over a dimmed screen
  - One filled button pinned in the bottom third
  - A short line of rules or context near the picker
- `v3` Agenda or schedule list
  - Rows of events under dated headings
  - A title at the top
  - Clock times beside the events
- `v4` Plain fields or strip
  - A week strip or row of day chips
  - A time or date in a small field or row
  - A title at the top

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
