# This type: Search (`search`)

Also called: search box, type-ahead, search results, explore search, find
What it is for: Let a person type what they are looking for and get to it without browsing.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Search field with a placeholder or a typed query | 18 sit at the top edge. zenly and Apple TV put the field just above the keyboard. The 3 without a field are Google Chrome (voice), Trainline and Hopper (forms). |
| 2 | Results, suggestions or recent searches under the field | Recent searches on zenly and Neo Financial, topics on Finimize, a suggestion on Canopi and Moda Operandi, browse lists on Preply and Pacemaker, results on Cherrypick, WAV, Fanatics Live and 6 more. |
| 3 | Clear (x), Cancel or close control | An x in the field and a Cancel button together on Cherrypick, Fanatics Live and Moda Operandi. Close buttons on Google Chrome, Preply, Pacemaker and 2 more. |
| 4 | Typed query visible | Canopi, Cherrypick, WAV and 7 more. |
| 5 | On-screen keyboard open | Canopi, Finimize, zenly and 7 more. |
| 6 | Empty field showing only placeholder text | Finimize, zenly, Preply and 7 more. |
| 7 | Photo, avatar or product image in result rows | Cherrypick, WAV, Fanatics Live and 4 more. |
| 8 | Bottom tab bar | WAV, Fanatics Live, Trainline and 4 more. |
| 9 | Tabs, chips or a Filters link under the field | Tabs on WAV and Clubhouse, chips on Google Drive, Filters and Sort on Cherrypick, 'View Filters' on Instamotor. |
| 10 | One-tap button on each result row | Add on Cherrypick, Follow on WAV, Buy on Fanatics Live, + on Byte, join or request on Clubhouse. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Type-ahead over the keyboard: The keyboard is open and a short list of suggestions, recents or live matches sits above it, as on zenly and Byte.
- `v2` Results page with controls: The query stays in the box and a longer result list follows, often with a Cancel button or tabs, as on Cherrypick and Clubhouse.
- `v3` Explore page with a box on top: A search field sits above browse content such as categories or subjects, as on informed News and Blinkist.
- `v4` Voice or form-style search: Search starts from a mic on Google Chrome, a tabbed form with a Find button on Trainline, or from-to fields on Hopper.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Nothing is shown under the box while the keyboard is open, so there is no hint of what to type.
2. Two close controls sit side by side: an x in the field and a Cancel or close button beside it.
3. The placeholder is pale grey on a light grey field and is hard to read.

## What the checked screens of each subtype have (the linter expects the same)

58 checked screens of this type; screens per subtype (a screen can be more than one): v1 20, v2 22, v3 15, v4 6.

- `v1` Type-ahead over the keyboard
  - The keyboard is open at the bottom of the screen
  - A search field at the top, with a placeholder or a typed query
  - Suggestions, recent searches or live matches in the space above the keyboard
  - A clear or cancel control beside the field
- `v2` Results page with controls
  - The typed query stays in the field at the top
  - A list of results under the field
  - A clear or cancel control beside the field
  - A photo, avatar or product image in most result rows
- `v3` Explore page with box
  - A search field at the top that shows only its placeholder
  - Browse content under the field, such as categories, topics or lists
  - Images in most of the browse rows
  - No keyboard open
- `v4` Voice or form-style search

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
