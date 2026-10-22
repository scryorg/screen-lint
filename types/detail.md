# This type: Detail (`detail`)

Also called: item page, product page, listing page, details screen, record view, single-item page
What it is for: Show everything about one thing the person picked, and put the next step within reach.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Back, close or down arrow at the top | Top-left on all but Apple Maps, which puts the X at the top right of the photo. Missing on Apple Home, Particle News and Formula 1®. |
| 2 | Item name as a large heading | Set over the photo on Apple Maps, SIX, IHG Hotels & Rewards and Apple Fitness. |
| 3 | Block of description text | Coinbase, HBO Max, Apple Maps and 8 more. Withings Health Mate and Apple Fitness cut it short with Show more or MORE. |
| 4 | Key fact next to the name (price, date, length, status) | Price on Baemin, SIX, Apple Home and 2 more. Date or time on SiriusXM, Jobber, Starling Bank and Apple Fitness. Length or duration on HBO Max and Withings Health Mate. |
| 5 | Large photo or video at the top | Apple Maps, Air NZ, Peloton Strength and 8 more. |
| 6 | Icons at the top right (share, favorite, search, bag) | Coinbase, Baemin, SIX and 8 more. |
| 7 | Bottom tab bar still visible | Coinbase, HBO Max, Peloton Strength and 6 more. |
| 8 | Rail or link list of related items below | HBO Max, SiriusXM, Apple Home and 5 more. |
| 9 | Filled button in the bottom third | Pinned above the home bar on Coinbase, Baemin, Withings Health Mate and 3 more. On IHG Hotels & Rewards and Tangerine the button sits low in the page instead. |
| 10 | Action rows with an icon or chevron | Air NZ, Jobber, Apple Home and 2 more. Used for small jobs such as add note, share or get help. |

## Variants (`v1` to `v3` in `variants`)

- `v1` Photo first: A large photo opens the page, then the name, key facts and short text, with one main button low on the screen.
- `v2` Program, episode or recipe page: Facts about the item, then a start, play, join or cook button or a list of parts, with related items below.
- `v3` Data record: A name, an amount or status, then rows of facts and small actions, with no photo.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The sticky header text sits on top of the faded page title, so neither is easy to read.
2. A floating button or pop-up covers page content: the round plus button cuts into the end of a line item on Jobber, and the confirm pop-up hides the start of the title on Apple Fitness.
3. Footnotes are set in very small light-grey type that is hard to read.

## What the checked screens of each subtype have (the linter expects the same)

49 checked screens of this type; screens per subtype (a screen can be more than one): v1 20, v2 14, v3 13.

- `v1` Photo first
  - A large photo or video at the top of the page
  - A back, close or down arrow at the top
  - The item name as a large heading
  - A price or other key fact next to the name
- `v2` Program or recipe page
  - A back, close or down arrow at the top
  - The item name as a large heading
  - A block of description text
  - A length, date or other key fact near the name
- `v3` Data record
  - A back, close or down arrow at the top
  - A key fact such as an amount or status near the top
  - No large photo; the page opens on text and numbers

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
