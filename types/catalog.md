# This type: Catalog (`catalog`)

Also called: browse screen, listing, product grid, collection, explore, shop
What it is for: Show many things of one kind, such as products, meals, songs or places, so the person can scan them and pick one.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Photo or cover art leading each item | The 4 without are ESPN, Airtable, KakaoBank and Deel, which use logos or small icons in rows. |
| 2 | Bottom tab bar | The 6 without one (Birchbox, Airtable, Zomato and 3 more) all have a back arrow instead. |
| 3 | Short section headings | 'Popular' on Fancy, 'New In' on Mucho, 'Recommended For You' on Strava, 'Featured Stations' on ESPN. |
| 4 | Tabs or chips to pick a category or view | All / Restaurants / Grocery on Uber Eats, Salads / Sandwiches on Panera Bread, All / Tops / Bottoms on Hollister Co. |
| 5 | One-column list or stacked cards | Uber Eats, ESPN, Airtable and 7 more. |
| 6 | Filter, sort or refine control | A Sort and Filter row on Hollister Co and Vinted, a Refine button on Birchbox, a Filters chip on Zomato. |
| 7 | Search field or search icon | A field on Uber Eats, Fancy, Mucho and Vinted, a query in the top bar of Missguided, an icon on Strava, Waking Up and Hollister Co. |
| 8 | Price or cost on the item | HBX, Missguided, Birchbox and 5 more. |
| 9 | Two-column grid | TIDE, HBX, Missguided and 4 more. |
| 10 | Result count | '383 results' on Uber Eats, '3033 items' on Missguided, '500+ results' on Vinted, '299 results' on Hollister Co, '4/4 Products' on Birchbox. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Product grid: Two photos per row with a name and a price under each, as on Hollister Co and Vinted.
- `v2` Rows with a thumbnail: One item per row with a small image or logo and a line or two of text, as on Panera Bread and WAV.
- `v3` Shelves: Several sideways rows, each under its own heading, as on TIDAL.
- `v4` Big photo cards: One large card per item that fills the width, as on Zomato where each card has an offer and a rating.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The floating tab bar on TIDE sits over the next row of content.
2. On Missguided the sort options are small light grey text over a faded grid, so they are hard to read.
3. On HBX a small 'Refine' label sits on top of a product photo.

## What the checked screens of each subtype have (the linter expects the same)

58 checked screens of this type; screens per subtype (a screen can be more than one): v1 16, v2 16, v3 9, v4 14.

- `v1` Product grid
  - A photo on every item, two to a row
  - A name and a price under most photos
  - A bottom tab bar under the grid on most screens
- `v2` Rows with thumbnail
  - One item per row in a single column
  - The list starts in the top third of the screen
  - A small picture or logo leading the rows on most screens
- `v3` Shelves
  - A short heading over the shelves
  - A cover or photo on every item
  - Several covers showing at once in a row
- `v4` Big photo cards
  - A large photo on every card
  - Cards stacked in a single column
  - Tabs or chips in the top third on most screens

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
