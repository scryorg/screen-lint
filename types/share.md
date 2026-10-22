# This type: Share (`share`)

Also called: share sheet, invite friends, refer a friend, referral page, send to
What it is for: Help the person send something out of the app, or bring other people in, in a few taps.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | A way out (X, back, Cancel or Done) | None on Locket, TickPick and Saily. |
| 2 | Row of app icons to send to | The New York Times, zenly, GIPHY and 8 more. Messages or Text is in the row on 9 of the 11. |
| 3 | Link or code shown on the screen, or a copy action | The New York Times, Marcus by Goldman Sachs, GIPHY and 8 more. |
| 4 | Preview of what is being shared | A page title (The New York Times, Apple News, foodpanda and Imprint), a story or streak card (zenly, GIPHY and Brilliant), a QR card (Instagram), an invite card (Apple Invites), a share card (Any Distance). |
| 5 | Reward stated in words or numbers | Marcus by Goldman Sachs, Rakuten, TickPick and 6 more. Money, credit or an unlocked feature. |
| 6 | Bottom sheet over a dimmed screen | The New York Times, Locket, Apple News and 6 more. |
| 7 | Wide button for the main action | Marcus by Goldman Sachs, Saily and KOHO (share the link or code), Dimensional (invite), GIPHY and Any Distance (copy or save), Notion (view site). |
| 8 | How-it-works or rules text | Numbered steps on Rakuten and Vibecode, a How it works block on Saily, a Rules block on KOHO. |
| 9 | Referral tracking (counts or history) | Marcus by Goldman Sachs (See My Referral History), Dimensional (people registered), KOHO (Sign-ups, Completed), Vibecode (Referral history). |
| 10 | Short confirmation toast | 'Saved successfully' on Brilliant and 'Link Copied' on Fabulous. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Share sheet over the content: A bottom sheet over the page with a row of apps and quick actions such as Copy and Save.
- `v2` Referral page: A full page that sells the reward, gives a link or code, and sometimes tracks sign-ups.
- `v3` Preview card plus targets: A card of the thing to send (story, QR, invite or workout) with a row of apps or actions under it.
- `v4` Pick people to invite: A list of friends or members to add, or a publish panel (Notion) with link and access settings.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. A page whose job is sharing shows no share control in view.
2. The sheet covers the page text and cuts a sentence off in the middle.
3. Small dim text on a dark or coloured background is hard to read.

## What the checked screens of each subtype have (the linter expects the same)

58 checked screens of this type; screens per subtype (a screen can be more than one): v1 17, v2 20, v3 12, v4 10.

- `v1` Share sheet over content
  - A bottom sheet over a dimmed screen
  - A row of app icons to send to
  - A way out: X, back, Cancel or Done
  - A wide button for the main action
- `v2` Referral page
  - A reward stated in words or numbers
  - A way out, usually in the top third
  - A wide button for the main action
  - A full page, not a sheet over a dimmed screen
- `v3` Preview card plus targets
  - A preview of what is being shared, in the middle third
  - A way out, usually in the top third
  - No reward text and no referral tracking
- `v4` Pick people to invite
  - A way out, usually in the top third
  - No row of app icons to send to
  - No reward text and no referral tracking

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
