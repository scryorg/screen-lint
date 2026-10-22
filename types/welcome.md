# This type: Welcome (`welcome`)

Also called: intro carousel, onboarding slides, value proposition screen, first-run tour, get started screen
What it is for: Tell a new person in one short line what the app does for them, then let them start.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Headline-size message | Agora uses a small label and body-size text instead. |
| 2 | Picture, illustration or product shot | Only 3 use real photos (GetYourGuide, Vimeo and Shipt). The rest are drawings, icons or app screenshots. |
| 3 | Button in the bottom third | Every button sits in the bottom third. Labels: Next, Continue, Get Started, Let's Go. |
| 4 | Body text under the headline | Usually one to three short lines. |
| 5 | Second choice under the button | Log in, I have an account, Skip, Redeem, or other sign-in options (Todoist, Hopper, Brilliant and 5 more). |
| 6 | Dark background | Neo Financial, Citizen, Rise and 4 more. |
| 7 | Brand logo or name | A logo or wordmark on Todoist, Brilliant, Stationhead and 2 more, and a small brand label on Neo Financial. |
| 8 | Page dots or progress bars | Dots on Shelf, Agora, Lake and Stationhead. Story-style bars at the top of Neo Financial. |
| 9 | Account entry (log in or sign-in buttons) | GetYourGuide, Todoist, Stationhead and 2 more. |
| 10 | Close, back or skip at the top | Neo Financial, Citizen, Hopper and Bird. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Carousel page: One page of several, with page dots or top progress bars.
- `v2` Value line with account choice: A headline and picture, with log in and sign up buttons on the same screen.
- `v3` Card or sheet over the app: The message sits in a sheet or card, or on a dimmed copy of the app.
- `v4` Message only, no button: A headline and a picture, with no visible control to move on.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. No visible control to move on. The screen shows a message and a picture only.
2. Small body text with low contrast: grey on white, or white on a mid-tone color.
3. Words run across or behind artwork: a chart line crosses the headline on Rise, and a sheet covers part of the headline on Shipt.

## What the checked screens of each subtype have (the linter expects the same)

57 checked screens of this type; screens per subtype (a screen can be more than one): v1 21, v2 12, v3 11, v4 7.

- `v1` Carousel page
  - One headline-size message with a picture or drawing
  - Page dots or progress bars that show where this page sits
  - One button in the bottom third
  - Body text under the headline on most pages
- `v2` Value line with account choice
  - A headline-size message with a picture or drawing
  - Log in or sign-in buttons in the bottom third
  - A second choice, such as a log in link, under the main button
- `v3` Card or sheet
  - A headline-size message with a picture or drawing
  - One button in the bottom third
  - No log in or sign-in buttons on the card
- `v4` Message only, no button

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
