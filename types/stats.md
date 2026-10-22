# This type: Stats (`stats`)

Also called: dashboard, insights, progress, summary, analytics, leaderboard, recap
What it is for: Shows the person how they are doing, in a few figures or one drawing, over a stretch of time.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Chart, gauge, ring or other drawn graphic | Bars, lines, sparklines, a radar, a ring, a dot grid or a body figure. On Bloomberg, Alan Mind, Equinox and 10 more. |
| 2 | Time period named or switchable | Six have a switch (Rarible, Alan Mind, Eight Sleep and 3 more); the rest print the period as a label. On Rakuten, Rarible, Alan Mind and 9 more. |
| 3 | Short headings that split the blocks | Section labels such as Breakdown, Overview, Bills due or Tracker. On Rarible, Alan Mind, Eight Sleep and 8 more. |
| 4 | Bottom tab bar | The screen sits inside the app's main navigation. On Bloomberg, Rarible, Eight Sleep and 8 more. |
| 5 | One large headline number or score | A total, a score, a duration or a percent in display-size type. On Rakuten, Alan Mind, Wealthfront and 7 more. |
| 6 | Rows of a label and a right-aligned value | Prices, balances, shares of a total or ranked amounts. On Bloomberg, Rarible, Alan Mind and 7 more. |
| 7 | One plain sentence that reads the numbers | For example a tip, a verdict or a prompt to start. On Wealthfront, Equinox, Gentler Streak and 4 more. |
| 8 | Zeros or an empty message where figures would go | The captures were made on new accounts, so some screens show no data. On Rakuten, Ubank Money App, MyFitnessPal and 3 more. |
| 9 | Filled button in the bottom third | Got it, Done, Share, Finish or a pale Tap to sync. On Rakuten, Wealthfront, Gentler Streak and 2 more. |
| 10 | Opens as a sheet over a dimmed screen | Used for a status or a short explanation. On Rakuten, komoot and Bevel. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Chart over a period: Bars or sparklines for one period, often with a day, week or month switch (Eight Sleep and Done).
- `v2` Score or gauge: One score or percent in a ring or gauge, with rows below that explain it.
- `v3` Table of figures: Rows of labels and amounts are the main content, such as market prices (Bloomberg), balances (Kakao Pay) or spending (Cleo).
- `v4` Ranking: Names with avatars and amounts, ordered from first place down.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Axis and column labels are set very small and in pale grey.
2. A row of cards is cut at the right edge with no sign of how many more there are.
3. A no-data message gives no reason and no next step: No Data Available above an empty chart area.

## What the checked screens of each subtype have (the linter expects the same)

56 checked screens of this type; screens per subtype (a screen can be more than one): v1 24, v2 12, v3 10, v4 7.

- `v1` Chart over a period
  - One chart or drawn graphic, most often a single one near the middle of the screen
  - The period it covers is named or switchable, usually near the top
  - Short headings split the screen into blocks
- `v2` Score or gauge
  - A ring, gauge or other drawing that carries the score
  - One large score or percent in display-size type
  - Short headings split the rows that explain the score
- `v3` Table of figures
  - Rows of a label and a right-aligned value are the main content
  - The period is named or switchable, usually near the top
  - Short headings split the rows into blocks
- `v4` Ranking

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
