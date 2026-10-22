# This type: List (`list`)

Also called: table view, index, saved items, collection, records list, library
What it is for: Shows a set of records one per row so the person can scan them, open one or add another.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Title at the top, in the bar or as a large title | Large titles on 8 of them (Vipps, Shipt, Orbit and 5 more). Buddy is scrolled and shows none. On Beep, Zocdoc, NYT Audio and 19 more. |
| 2 | Back arrow, close X, Done or Edit at the top | The list is a pushed or modal page, not a tab root. On Beep, Dropbox, Live Nation and 14 more. |
| 3 | One thing at the right end of each row | A button or icon on 6, a value on 4, a chevron on 3 and avatars on 1. On NYT Audio, Dropbox, Shipt and 11 more. |
| 4 | Thumbnail, icon or avatar at the left of each row | Cover art, file icons, logos, folder icons or profile pictures. On Beep, NYT Audio, Dropbox and 11 more. |
| 5 | Two-line rows: a name with a pale detail line | The second line holds a type, a date, a size or a count. On Beep, NYT Audio, Dropbox and 10 more. |
| 6 | Way to add: a plus, a create button or a compose icon | Top right, a floating button, a bottom bar icon or an inline button. On Beep, NYT Audio, Vipps and 7 more. |
| 7 | Bottom tab bar | The list is a main screen of the app. On Zocdoc, NYT Audio, Vipps and 6 more. |
| 8 | Search, filter or sort control | A search field, a Show or Sort by line, or filter chips. On NYT Audio, Dropbox, Apple Notes and 5 more. |
| 9 | Empty message or an Empty slot | Four screens are empty from top to bottom (Zocdoc, Live Nation, Product Hunt and musical.ly). On Zocdoc, Live Nation, Product Hunt and 3 more. |
| 10 | Section headings that group the rows | Dates, categories or folders. On Notion, Orbit, Apple Notes and 3 more. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Media and file rows: Each row has a thumbnail or icon, a title, a pale detail line and a small control such as a download icon or a menu.
- `v2` People with a Follow button: Avatar, name and a short line, with Follow or a role at the right end.
- `v3` Rows grouped under headings: Records are split by day, category or folder, often with a plus button for new ones.
- `v4` Empty list: One sentence says there is nothing yet, sometimes with an illustration.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. An empty page gives a message and no button.
2. A popover, a toast or a floating button covers rows of the list.
3. Row text is cut off with an ellipsis, so the full name cannot be read.

## What the checked screens of each subtype have (the linter expects the same)

62 checked screens of this type; screens per subtype (a screen can be more than one): v1 19, v2 5, v3 17, v4 16.

- `v1` Media and file rows
  - A title at the top
  - A thumbnail, icon or avatar at the left of every row
  - A name with a pale detail line in every row
  - A button, value or chevron at the right end of the rows
- `v2` People with a Follow button
- `v3` Grouped rows
  - Section headings that split the rows into groups
  - A title at the top
  - A button, value or chevron at the right end of the rows
  - A thumbnail, icon or avatar at the left of most rows
- `v4` Empty list
  - An empty message or an empty slot in the page
  - A title at the top
  - A back, close, Done or Edit control at the top
  - No rows, so no thumbnails or right-end controls

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
