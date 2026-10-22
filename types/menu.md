# This type: Menu (`menu`)

Also called: More tab, navigation drawer, hamburger menu, side menu, profile menu, section list, action sheet
What it is for: Put the app's sections and actions in one short list so the person can jump to any of them.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | List of labelled rows or buttons | Every screen is words in a column. Small tiles also appear on Check and Not Boring Calculator, but the rows are the main thing. |
| 2 | Back arrow, close X, Done or Cancel | At the top on Walgreens, Gusto Mobile, Check and 9 more. On GIPHY it is a Cancel button at the bottom. |
| 3 | Small icon at the left of each row | Gusto Mobile, Check, Apple Sports and 9 more. |
| 4 | Shown over another screen: sheet, popover, slide-in panel or overlay | Apple Sports, Airtable, Taco Bell and 6 more. The page behind stays partly visible. |
| 5 | Chevron at the right edge of rows | Gusto Mobile, Check, Kakao Pay and 5 more. |
| 6 | Help or support row | Gusto Mobile, Check, Not Boring Calculator and 5 more. |
| 7 | Group headings | Settings, Help and More on Gusto Mobile; ACCOUNT and HELP & SAFETY on Check; APPS on Not Boring Calculator; Tools and Help Center on Grailed; Help and Control center on Klarna; two headings on Kakao Pay and one on OLIO. |
| 8 | Bottom tab bar still visible | PayPal Honey, Taco Bell, Grailed and 3 more. |
| 9 | Account or settings row | Gusto Mobile, Check, OLIO and 2 more. Log out or Sign out is a separate row on Gusto Mobile, Attio and LIVESTRONG MyQuit Coach. |
| 10 | Identity header: avatar, name or email | Check, Apple Sports, Attio and 2 more. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Profile or account menu: Account, settings and help rows. Log out or Sign out ends the list on Gusto Mobile, Attio and LIVESTRONG MyQuit Coach.
- `v2` Slide-in or overlay navigation: A panel or layer over the current page lists the main sections. The page shows behind it on all four.
- `v3` Section list: A list of departments, products, projects or feature pages used to move around. PayPal Honey and Bonobos are shop categories, Todoist is projects.
- `v4` Action or switch sheet: A short sheet of choices for the thing on screen: switch table on Airtable, save or report on GIPHY, view or close an account on Marcus by Goldman Sachs.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The panel is dark and see-through, so scores and team crests stay busy beside and below the rows.
2. A banner, rating tiles, an invite box and a promo box sit above the list, so the first row starts about halfway down the page.
3. A full page holds two rows in one box, and the rest of the page is empty.

## What the checked screens of each subtype have (the linter expects the same)

59 checked screens of this type; screens per subtype (a screen can be more than one): v1 13, v2 10, v3 25, v4 14.

- `v1` Profile or account menu
  - The rows start in the top third of the screen
  - A small icon at the left of the rows
  - An account or settings row
  - A help or support row
- `v2` Slide-in navigation
  - A panel drawn over another screen, with the page still showing behind it
  - The list of rows starts in the top third
  - A small icon at the left of most rows
- `v3` Section list
  - The list of rows starts in the top third of the screen
  - A back arrow, close X, Done or Cancel at the top
  - A chevron at the right edge of the rows
  - The list fills the page and is not drawn over another screen
- `v4` Action or switch sheet
  - A sheet drawn over another screen
  - A back arrow, close X, Done or Cancel
  - No group headings: the choices run as one list

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
