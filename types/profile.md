# This type: Profile (`profile`)

Also called: user page, creator page, account page, artist page, seller page, bio page
What it is for: Show who a person, creator or business is, and give a reason to follow, contact or trust them.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Avatar or portrait | All but Future (a text bio in a sheet) and Vevo (an artist page that opens on videos). |
| 2 | Name or handle as a heading in the page | Missing in the page on Future, Vevo, Breaker and Pacemaker, where the name is only in the top bar or in the text. |
| 3 | List or grid of what the person made, posted or sold | Py, Patreon, Vevo and 10 more. |
| 4 | Back or close control | Top-left on ID, Patreon, Polywork and 6 more. An X on HQ Trivia and Nike Training Club. |
| 5 | Icons at the top right (gear, share, more) | Gear on Py, Mammoth and Riot Mobile. Share on Polywork, Breaker and OpenSea. More on Behance, Patreon and Rarible. Heart and radio on Vevo. |
| 6 | Bottom tab bar still visible | Behance, Py, Patreon and 7 more. |
| 7 | Row of counts (followers, wins, ratings) | Behance, Must, Patreon and 6 more. |
| 8 | Tabs under the header | Two tabs on Py, Vevo, Rarible and 4 more. Three on Behance. Five or more on OpenSea. |
| 9 | Follow, add or edit button near the name | Follow on Breaker and Hypelist, Following on Polywork and Snackpass, Add Friend on Nike Training Club, Edit on Behance and Mammoth. |
| 10 | Banner or cover picture behind the avatar | Behance, Patreon, Polywork and 3 more. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Creator or social profile: Avatar, name, counts and a follow or add button, then a feed, grid or list of the person's posts.
- `v2` Own account profile: Edit or a gear is in view, with the person's own stats, posts or match history below.
- `v3` Seller, business or driver page: A name with ratings, verified facts or opening hours, so a stranger can decide whether to trust them.
- `v4` Profile as a sheet or card: A bio, a report-or-block sheet or a stats card laid over another screen.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The sheet shows a long bio but neither the person's name nor a photo, so the reader cannot tell who it is without reading the text.
2. A toast banner covers the top of the page: it cuts across the avatar on Hypelist and the header on HEY.
3. The stats are set in small grey text over a photo and are hard to read.

## What the checked screens of each subtype have (the linter expects the same)

54 checked screens of this type; screens per subtype (a screen can be more than one): v1 28, v2 11, v3 8, v4 9.

- `v1` Creator or social profile
  - An avatar near the top, with the name set as a heading close to it
  - A back control at the top left
  - Gear, share or more icons at the top right
  - A list or grid of the person's posts below the header
- `v2` Own account profile
  - An avatar at the top, with the name beside or under it
  - A gear or other icon at the top right
  - The bottom tab bar still in view
  - The person's own posts or items below the header
- `v3` Seller or business page
  - A back control at the top left
  - A name with an avatar or logo near the top
  - A row of ratings or other counts that help a stranger decide
  - No bottom tab bar
- `v4` Sheet or card profile
  - A close control or a Done button at the top
  - No bottom tab bar, because the card sits over another screen
  - No tabs under the header

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
