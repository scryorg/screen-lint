# This type: Feed (`feed`)

Also called: timeline, news feed, activity feed, stream, for you, wall
What it is for: Let a person scroll through a steady supply of posts, stories or articles and stop on whatever catches their eye.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 9 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Image, video or logo on each item | The 3 text-only screens are Vivino, Dot and Stocks. |
| 2 | Source or author line on each item | Often with a time: '11 minutes ago' on Hush, '32m ago' on Gawq, '2 days ago' on WEAR. |
| 3 | Bottom tab bar | Only IPSY and Google News put words under the icons. The other 8 use icons alone. |
| 4 | Action on each item (like, react, save, upvote, open) | Like and comment on Vivino and Hush, react on Shelf, open on Must, save on Gawq, upvote on Product Hunt. |
| 5 | Chips, tabs or a dropdown to change the stream | Chips on Vivino, Gawq and Medium, tabs on Must and WEAR, dropdown on Edits and Matter. |
| 6 | Heading above the stream or a group of items | Vivino, IPSY, Shelf and 4 more. |
| 7 | Photo or video across the full width of the item | BeReal, Must, IPSY and 4 more. |
| 8 | '...' menu on the item | BeReal, Hush, Shelf and 3 more. |
| 9 | Counts shown (likes, upvotes, views, scores) | Vivino, Hush, Edits and 2 more. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Posts and reviews from people: Short posts, reviews or activity from users, each with a name, a time and a like or react control, as on Vivino and Hush.
- `v2` News and article cards: Headline cards with a source and a time, usually with a photo, as on Gawq and Google News.
- `v3` One item per screen: A full-screen photo or video with the controls laid over it, as on Edits.
- `v4` Compact ranked or queued list: Small rows with an icon, a title and one line, ranked by votes on Product Hunt and ordered as a reading queue on Matter.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Tab bar icons with no words: 8 of the 10 tab bars (Hush, Must, Edits and 5 more) rely on icons alone.
2. An image slot shows a blank grey placeholder on the first item of Gawq; Vivino has a solid black circle beside its heading.
3. The last card of Dot fades into a blur at the bottom edge, so its text cannot be read.

## What the checked screens of each subtype have (the linter expects the same)

51 checked screens of this type; screens per subtype (a screen can be more than one): v1 16, v2 19, v3 5, v4 4.

- `v1` Posts and reviews
  - A name or source line on every post
  - A heading at the top above the posts
  - A picture, avatar or logo on most posts
  - A like or react control on most posts
- `v2` News and article cards
  - An image, video or logo on nearly every card
  - A heading above the cards or a group of them
  - A source line on most cards
  - A bottom tab bar under the stream
- `v3` One item per screen
- `v4` Compact ranked or queued list

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
