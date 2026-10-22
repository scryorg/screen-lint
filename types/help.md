# This type: Help (`help`)

Also called: support, help centre, FAQ, contact us, about, terms and privacy, legal
What it is for: Answer a question or fix a problem, or put the person in touch with someone who can.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Back arrow, X or Done at the top | The sheets on Skyscanner, Pi and Coursera show only a grab handle; Coursera has a Close button at the bottom. |
| 2 | A way to reach a person | Contact, Chat, Message, Email or Start Conversation on Sweatcoin, Skyscanner, Bonobos and 7 more; Report Problem or Report a Bug on Stationhead and Zoom. |
| 3 | List of tappable rows to topics or pages | Stationhead, Wealthfront, Bonobos and 7 more. Chevrons on Marcus by Goldman Sachs, Zoom and Yuka; external-link arrows on World App and DeepSeek. |
| 4 | Large headline that names the topic or asks how to help | How can we help you? (Wealthfront), I need more help (Cash App), We're here to help! (Hush), Hi, How can we help? (DeepSeek), a policy title (Pi and Blank Street). |
| 5 | Question wording or an FAQ row | A question headline on Sweatcoin, Wealthfront, OKX and Yuka; an expandable question on Lloyds Mobile Banking; rows named FAQ on Bonobos, Kino and DeepSeek. |
| 6 | Legal text or legal links | Link lists on Bonobos, LIVESTRONG MyQuit Coach, World App and 2 more; full policy text on Pi and Blank Street. |
| 7 | Paragraphs of plain reading text | Sweatcoin, Skyscanner, Lloyds Mobile Banking and 4 more. |
| 8 | Shown as a sheet or panel over the app | Skyscanner, Pi, World App and 3 more. |
| 9 | Version number | Bonobos, LIVESTRONG MyQuit Coach and Zoom, at the bottom of the list. |
| 10 | Numbered steps | 1 to 5 on Sweatcoin and 1 to 4 on OKX. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Help start page: A friendly headline with search, topics or a chat or email button.
- `v2` One problem, one answer: A page about a single problem, with the explanation, the steps and a next action.
- `v3` Link list: support, about and legal: Rows that open support, feedback, terms and privacy pages.
- `v4` Full legal text: A policy page that starts straight into paragraphs.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The only contact route is a small or pale button after a long block of text.
2. Policy pages start as a wall of paragraphs with no short summary at the top.
3. Long steps are set in small pale type on a colour gradient.

## What the checked screens of each subtype have (the linter expects the same)

59 checked screens of this type; screens per subtype (a screen can be more than one): v1 16, v2 12, v3 15, v4 9.

- `v1` Help start page
  - A back arrow, X or Done at the top
  - A large headline that names the topic or asks how to help
  - A list of tappable rows to topics
  - Question wording or FAQ rows
- `v2` One problem, one answer
  - Paragraphs of plain text that give the answer
  - A headline that names the problem
  - A back arrow, X or Done at the top
- `v3` Support link list
  - A list of tappable rows to support, about and legal pages
  - The list starts in the top third of the screen
  - A back arrow, X or Done at the top
- `v4` Full legal text
  - Legal text that fills a large part of the screen
  - Paragraphs of plain reading text
  - A headline with the policy title
  - No contact button and no FAQ rows: the page is the text

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
