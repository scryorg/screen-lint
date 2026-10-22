# This type: Chat (`chat`)

Also called: conversation thread, messaging screen, DM thread, AI chat, message view
What it is for: Let the person read and write one running conversation with another person, a group or an AI.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Header with back, close or menu and a title | The title is a person, channel or group on Slack, Messages, Beep and Artsy, and the assistant name on ChatGPT and Grok. |
| 2 | Text field pinned to the bottom edge | Missing on Microsoft Copilot and Perplexity (voice mode), World of Hyatt and Saily (waiting or support view), and DeepSeek (hidden under a sheet). |
| 3 | Send, mic or attach button beside the field | A send arrow or Send label on 9 (Julienne, Woolworths, Beep and 6 more). Plus, mic or paper clip only on Slack, Messages, Cameo and Sonar. |
| 4 | Messages in the thread | The other 7 show a greeting, a waiting line or nothing yet: Microsoft Copilot, Perplexity, World of Hyatt and 4 more. |
| 5 | Own message in a filled bubble on the right | Messages, Cameo, Julienne and 5 more. |
| 6 | Time stamp or status line | Times on Slack, Cameo, Artsy and 2 more. Status words ('Waiting', 'Searching the web') on World of Hyatt and ChatGPT. |
| 7 | Picture or card inside the thread or the field | A photo and voice note on Messages, a hotel card on IHG Hotels & Rewards, an artwork card on Artsy, an attached image on ChatGPT and Grok. |
| 8 | Starter buttons or a hello link before the first message | Slack (Add description, Add people), Google Pay (Say Hello), Speechify (Summarize, Generate Quiz), Grok (mode cards). |
| 9 | Keyboard open | Woolworths, Beep, Grok and theScore. Sticker or sound trays take its place on Cameo and Sonar. |
| 10 | Bottom tab bar | Only Slack and Artsy. The other 17 are pushed screens with no tab bar. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Person or group thread: People talking to people, from a channel (Slack) to a live team chat inside a tab strip (theScore).
- `v2` AI assistant, typed: Replies are plain text, and the field often carries extra tools such as attach, DeepSearch or Think (Grok).
- `v3` Support or inquiry chat: A brand's bot or agent answers inside a non-messaging app, sometimes with a card or an action button in the thread (IHG Hotels & Rewards and Artsy).
- `v4` Voice mode: No thread and no field. A glowing shape and close, mic and settings buttons replace them.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. A support thread that shows no way to reply: the page is mostly blank with one waiting line or a short greeting.
2. The placeholder and the Send label are pale grey on white and hard to read.
3. An attached picture appears as a solid black block.

## What the checked screens of each subtype have (the linter expects the same)

55 checked screens of this type; screens per subtype (a screen can be more than one): v1 20, v2 11, v3 22, v4 2.

- `v1` Person or group thread
  - A header at the top with the name of the person or group
  - Messages stacked in the thread, with a time stamp or status line
  - A text field pinned at the bottom of the screen
  - A send, mic or attach button beside the field
- `v2` AI assistant, typed
  - A header at the top with the name of the assistant
  - A text field at the bottom of the screen
  - A send, mic or attach button beside the field
  - Replies and questions stacked in the thread
- `v3` Support or inquiry chat
  - A header at the top with a title and a back or close control
  - Messages stacked in the thread, replies from a bot or an agent
  - A text field pinned at the bottom of the screen
  - A send, mic or attach button beside the field
- `v4` Voice mode

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
