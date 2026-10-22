# This type: Inbox (`inbox`)

Also called: message list, conversations list, mailbox, chats tab, direct messages
What it is for: Show every conversation or message in one list so the person can find the one they want to open.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Title that names the list | Inbox, Messages, Chats, Direct messages, Archive, Team Chat. Only Gmail has no title, just a search bar. |
| 2 | Rows with a name or title, most with a time at the right | 9 of the 10 show a time (all but HEY). 6 show a preview line (Handshake, Fanatics Live, Spark Mail and 3 more). Rows are on Claude, Handshake, Fanatics Live and 7 more. |
| 3 | Bottom tab bar | Messenger, Riot Mobile, Behance and 7 more. The other 10 are pushed screens, sheets or dialogs. |
| 4 | Search field or icon | A top field on Behance, Slack, Handshake and 3 more, a top icon on Spark Mail and Polywork, and a bottom field on Claude. |
| 5 | New-message or compose button | Floating at bottom right on Claude, Behance, Slack and 2 more. Icon at top right on Zoom, Fanatics Live and Dispo. |
| 6 | Empty-state message | Messenger, Apple Mail, Zoom and 4 more. Four add a button or link (Apple Mail, Zoom, Riot Mobile and Slack). |
| 7 | Round avatar at the left of the row | Handshake, Fanatics Live, Dispo and 4 more. Rows on Claude, Spark Mail and Singapore Airlines have none. |
| 8 | Filter tabs, chips or a filter button | Messenger, Riot Mobile, Dispo and 2 more use tabs or chips. Slack has a filter icon beside search. |
| 9 | Unread marker (dot, 'new' pill or count badge) | Dots on Handshake and Spark Mail, 'new' pills on Dispo, count badges on a tab icon on BFF and Gmail. |
| 10 | Separate place for requests or unknown senders | Messenger (Message requests), Riot Mobile (Requests tab), HEY (Screener), Polywork (Requests row). |

## Variants (`v1` to `v4` in `variants`)

- `v1` Conversation list: People or groups in rows, with avatar, time and often a preview.
- `v2` Email mailbox: Sender, subject and time rows, with mailbox folders, a screener or filter chips.
- `v3` Notice inbox: Messages from the app itself shown as cards or short rows, with no people in them.
- `v4` Empty chat list that asks for friends: A first-run screen with no threads yet and, on three of them, a button to add people.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The floating compose button sits on a row and covers the end of its time stamp.
2. Large image cards fill the page, so only three items are in view at once.
3. The empty state says 'No messages' and offers no next step.

## What the checked screens of each subtype have (the linter expects the same)

58 checked screens of this type; screens per subtype (a screen can be more than one): v1 26, v2 9, v3 10, v4 11.

- `v1` Conversation list
  - Rows of people or groups, each with a name and a time
  - A round avatar at the left of each row
  - A title in the top third
- `v2` Email mailbox
  - A title or mailbox name in the top third
  - A new-message button, mostly floating at the bottom
  - A search field or icon, mostly at the top
- `v3` Notice inbox
  - A title in the top third
  - Short rows or cards of notices from the app
  - No round avatars, because no people are in the list
- `v4` Empty chat list
  - A title in the top third
  - An empty-state message in the middle of the screen
  - A bottom tab bar on most of them
  - A new-message or add button on most of them

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
