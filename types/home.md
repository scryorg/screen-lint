# This type: Home (`home`)

Also called: dashboard, landing screen, start screen, today view, main tab, hub
What it is for: Show a person what is new and what needs attention, then give them a short way into the thing they came to do.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Bottom tab bar | The two without one are Meituan Takeaway, a service page inside a larger app, and Monese, where a Face ID card covers the screen. Lightyear and Pillow show icons with no words. |
| 2 | Short heading above each block of content | Examples: 'Popular on Calm' on Calm, 'Featured Stories' on The Atlantic Magazine, 'Made for you' on Insight Timer. |
| 3 | Large photo or illustration block | Hero cards on Fiverr and Disney, a full-bleed photo on Calm, illustrated promo cards on Jobber and Monese. |
| 4 | Row that scrolls sideways, cut off at the right edge | Seen on Lightyear, GIPHY, Fiverr and 7 more. |
| 5 | Icons for account, alerts or settings in the top bar | Bell on Jobber and Insight Timer, gear on Pillow, avatar on Lightyear, The Atlantic Magazine, Fabulous and 2 more. |
| 6 | Number, ring or status summary near the top | Cash balance on Lightyear, streak ring on Calm, fasting ring on Zero, balance on Monese, sleep ring on Pillow, score strip on The Athletic, member count on Insight Timer. |
| 7 | 'See all', 'View all' or chevron link on a heading | Calm, GIPHY, Fiverr and 4 more. |
| 8 | Search field or search icon on the page itself | Meituan Takeaway, GIPHY, Fiverr and 3 more. Four more (The Atlantic Magazine, Jobber, Disney and Apple Games) have search only as a tab. |
| 9 | Greeting or date line at the top | The Atlantic Magazine, Jobber, Pillow and Insight Timer. |
| 10 | Promo card with a close (x) button | Jobber, Monese and Pillow. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Status first: A balance, ring or streak leads the page and one action sits under it, as on Lightyear, Zero and Monese.
- `v2` Shelves of content: Rows of tiles or posters stack down the page, each with its own heading, as on Disney and Apple Games.
- `v3` Photo-led front page: Large photos with headlines or event names, under a chip row or score strip on TickPick and The Athletic.
- `v4` Greeting plus cards: A greeting or daily prompt, then cards for tips, tasks and check-ins, as on Jobber and Insight Timer.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Tab bar icons come with no words, so the person has to guess what each one opens: Lightyear has three icons and Pillow has six.
2. Inactive tabs are drawn very pale, close to the background colour.
3. ClickUp shows one dashboard row and then blank space down to the tab bar.

## What the checked screens of each subtype have (the linter expects the same)

54 checked screens of this type; screens per subtype (a screen can be more than one): v1 12, v2 23, v3 7, v4 12.

- `v1` Status first
  - A number, ring or status summary near the top, on every screen
  - Short headings above the blocks under it
  - A bottom tab bar
- `v2` Shelves of content
  - A short heading above every shelf
  - A row that scrolls sideways and is cut off at the right edge
  - A large photo or illustration block on most screens
  - A bottom tab bar
- `v3` Photo-led front page
- `v4` Greeting plus cards
  - A greeting or date line at the top
  - Account or alert icons in the top bar
  - Short headings above the cards
  - A bottom tab bar

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
