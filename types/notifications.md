# This type: Notifications (`notifications`)

Also called: alerts, activity feed, activity log, notification center, mentions
What it is for: Tells the person what happened since they last looked and lets them act on it.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Title that names the screen | 15 say notifications (Baemin in Korean) and 5 use another word: Alerts, Activity, Mentions. On Partiful, Air NZ, Baemin and 17 more. |
| 2 | Back arrow or close X at the top | Most are pushed from a bell icon or a profile. On Partiful, Air NZ, Baemin and 12 more. |
| 3 | A time on each item | Relative (2 hours ago) or a clock time. 18 screens have items, so 15 of 18. On Air NZ, Baemin, Zoom and 12 more. |
| 4 | Avatar, icon or thumbnail at the left of the item | South China Morning Post puts the thumbnail at the right. On Zoom, Upwork, happn and 11 more. |
| 5 | Bottom tab bar | Six of the ten have a bell, Alerts or Activity tab (Upwork, Navigator, Splitwise and 3 more). On Baemin, Upwork, Dimensional and 7 more. |
| 6 | Unread dot or tinted row | Blue or red dots, or a pale blue row. On Air NZ, happn, Dimensional and 6 more. |
| 7 | Button or action row on the item | Accept, Follow, Check in, Add Note, Cancel Reminder, reply and like icons. On Air NZ, Zoom, Airtime and 3 more. |
| 8 | Headings that group by time | Today, This week, Earlier, New or Most Recent. On Upwork, happn, Airtime and 2 more. |
| 9 | Tabs that filter the list | All / Upcoming / Overdue, Latest / Manage, Received / Sent, Messages / News / Orders. On Zoom, The Weather Channel, South China Morning Post and 2 more. |
| 10 | Gear, Manage or channel setting in the header | A way to change what gets sent. On Partiful, Baemin, The Weather Channel and 2 more. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Event rows: An icon or avatar, one sentence about what happened and a time, with nothing to press.
- `v2` Rows with an answer button: The item carries the one action that fits, such as Accept, Follow, Check in or Add Note.
- `v3` Headline alerts under tabs: News, weather or order alerts, with tabs that filter the list.
- `v4` Empty: No items yet: a sentence, sometimes with a bell, or only a channel setting (Partiful).

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Item text and times are set very small and in pale grey.
2. Several lines in a row are almost the same, so the person cannot tell them apart without reading each one.
3. The screen holds one setting row and nothing else, so it does not say what will appear.

## What the checked screens of each subtype have (the linter expects the same)

59 checked screens of this type; screens per subtype (a screen can be more than one): v1 26, v2 11, v3 5, v4 17.

- `v1` Event rows
  - An icon or avatar at the left of each row
  - A time on each row
  - A title that names the screen
  - Nothing to press on the rows
- `v2` Answer button rows
  - A button or action row on every item
  - A time on most items
  - An avatar, icon or thumbnail at the left of the items
  - A title that names the screen
- `v3` Headline alerts under tabs
- `v4` Empty
  - A title that names the screen
  - A back or close control at the top on most
  - No times, avatars, unread marks or buttons, because there are no items

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
