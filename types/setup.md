# This type: Setup (`setup`)

Also called: onboarding question, profile setup, preferences quiz, interest picker, account setup step
What it is for: Collect one answer or one connection at a time so the app can be set up for this person.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Heading phrased as a question or instruction | Not shown on Tesla and Queue, where there is no heading or it has scrolled off. |
| 2 | Filled button (Next, Continue, Save, Done) | Bottom of the screen or just above the keypad in all 19. Pale on Orb Social, Cocoon and Houzz until the fields are filled. |
| 3 | Back, close or dismiss at the top |  |
| 4 | Tappable answer choices (rows, cards, chips, tiles) | Radio circles on Lifesum, Origin and Klima. Pick-many controls on Tock, Queue, Bleacher Report and Kraken. |
| 5 | Small line under the heading about why or how to answer | Bumble, HelloFresh, Origin and 7 more. |
| 6 | Typed answer | Orb Social, Cocoon, Houzz and 6 more. |
| 7 | Keyboard or keypad open | Orb Social, Cocoon, Wealthsimple Invest and 3 more. |
| 8 | Picture or illustration | Rivian, Oportun, Tesla and 2 more. |
| 9 | Progress cue (bar, steps) | Bumble, HelloFresh, Origin and Duolingo Math. Only Origin says 'Step 5 of 11'. |
| 10 | Skip or later option | Bumble, Brex and Amazon Alexa. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Pick from a list: Rows, chips or cards the person taps. Some allow one pick and some allow many.
- `v2` Type one answer: One or two fields and a keypad: a name, birthday, username or PIN.
- `v3` Connect something: Link a bank, a calendar, a car key, a phone key or a voice profile.
- `v4` Profile form: Several prompts or fields on one screen: profile prompts (Bumble), company details (Houzz), date and country (Microsoft Copilot).

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The main button is pale until the fields are filled, and nothing points to the missing one.
2. Choice lists run under the pinned button, so the last options are cut off.
3. A long paragraph in small type sits above the buttons.

## What the checked screens of each subtype have (the linter expects the same)

55 checked screens of this type; screens per subtype (a screen can be more than one): v1 24, v2 14, v3 8, v4 10.

- `v1` Pick from a list
  - Tappable rows, cards or chips in the middle of the screen
  - A heading at the top that asks the question
  - A filled button pinned at the bottom
  - A back or close control at the top
- `v2` Type one answer
  - A heading at the top that asks for one thing
  - A field to type in
  - A back control at the top
  - The keyboard open under the field
- `v3` Connect something
  - A heading that names what to connect
  - A small line under it saying why
  - A picture or illustration in the middle
  - A filled button pinned at the bottom
- `v4` Profile form
  - A filled button pinned at the bottom
  - A small line under the heading
  - Tappable choices such as chips or rows
  - A heading at the top

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
