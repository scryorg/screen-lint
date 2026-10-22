# This type: Filter (`filter`)

Also called: refine, sort and filter, filter sheet, facets, view options
What it is for: Let a person narrow a long list by setting a few choices, then go back to a shorter list.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Close, back, cancel or done control in the header | An x on Monarch, Rakuten, On and 4 more, a back arrow on Peerspace, Zillow, Shopify and 5 more, Cancel on Facebook Local and Shift, Done on Airtable, the word Close on Starling Bank and Baemin. None on Linear, DoorDash, Polywork and ZARA. |
| 2 | Main button pinned at the bottom | Apply on Monarch, Rakuten, Quizlet and 2 more, a results button on Peerspace, Zillow, On and 7 more, Save on Starling Bank and Peloton Strength. It is greyed out on Baemin and Peloton Strength and outlined on ZARA. |
| 3 | Reset or clear control | Reset at the top right on Zillow, Quizlet, Shopify and Audible, Clear at the top right on Peloton Strength, Clear all at the bottom on Monarch, Peerspace and On, Reset or Clear Filters beside or under the main button on Rakuten, DoorDash and GetYourGuide. |
| 4 | Short heading over each group of controls | 'Price' on Rakuten, 'Sizes' on On, 'Interests' on GetYourGuide, 'Days available' on Preply, 'ACTIONS' on Airtable, 'COLOUR' and 'SIZE' on ZARA. |
| 5 | Shown as a sheet or popover over the previous screen | Sheets on Monarch, Peerspace, Linear and 9 more, popovers on Polywork and Credit Karma. The other 10 are full screens. |
| 6 | Checkboxes or radio buttons | Checkboxes on Peerspace, Artsy, Fanatics Live and 2 more, radio buttons on On and Audible, both on Rakuten, checkmarks beside the chosen row on Quizlet, one selected marker on The Atlantic Magazine. |
| 7 | Chips or tiles that toggle | Size tiles on On, cuisine icons on DoorDash, time tiles on Preply, chips on Credit Karma, Baemin and GetYourGuide, row-property tiles on Linear, muscle chips on Peloton Strength. |
| 8 | Rows that open a dropdown or sub-list | Chevron rows on Monarch, Facebook Local, Audible and Shift, dropdown or picker rows on Linear, Zillow and Polywork. |
| 9 | Number in the button label | 'View 12 Spaces' on Peerspace, 'See 3 results' on Zillow, 'View results (74)' on On, 'See 2381 cars' on Shift, 'View 68 tutors' on Preply. Rakuten shows a filter count ('Apply 1 Filter'). |
| 10 | Search field inside the filter | Shopify, Polywork and Starling Bank. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Sheet over the results: A rounded sheet rises over the list with groups of choices and a button at the bottom, as on On and GetYourGuide.
- `v2` Full screen of grouped options: A full page with a back or close control and several groups, as on Zillow and Audible.
- `v3` One facet at a time: A single list to pick from, such as one team or artist list, as on Artsy and Fanatics Live.
- `v4` Small popover: A box floats over the page with a few chips or checkboxes and Apply or Reset, as on Polywork and Credit Karma.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The main button is greyed out, so it looks disabled while the person is still choosing.
2. A floating button or bar sits on top of the last row, which is cut off beneath it.
3. A short list leaves a large blank area under it.

## What the checked screens of each subtype have (the linter expects the same)

58 checked screens of this type; screens per subtype (a screen can be more than one): v1 29, v2 17, v3 9, v4 5.

- `v1` Sheet over results
  - A sheet that covers most of the screen, over the previous page
  - A main button pinned at the bottom
  - A short heading over each group of controls
  - A close or cancel control in the top third, and a reset or clear control
- `v2` Full-screen groups
  - A full page with no sheet or popover over it
  - A close or back control in the top third
  - Two or more groups, each under a short heading
  - A main button pinned at the bottom
- `v3` One facet at a time
  - A close or back control in the header
  - A single list of checkboxes or radio buttons
  - No group headings, because the list is the only group
  - Shown as a sheet or popover over the previous screen
- `v4` Small popover

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
