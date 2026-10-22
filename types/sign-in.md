# This type: Sign-in (`sign-in`)

Also called: log in, sign up, create account, registration, auth screen
What it is for: Let the person prove who they are, or make an account, with as little typing as possible.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Back, close or cancel at the top left | Missing only on Rarible, Gymshark, Houzz and Epidemic Sound. |
| 2 | Text field for typing | From 1 field (Workplace, Compass, Expensify and My BMW) to 5 fields (Khan Academy). Provider-only screens (Rarible, Houzz and Pi) have none. |
| 3 | Main filled button | 12 sit right under the last field. 6 are pinned low (Tomorrow, Workplace, CVS Health and 3 more). |
| 4 | Password field |  |
| 5 | Show or hide password control | An eye icon on 8 screens and a 'Show' link on Jumprope. |
| 6 | Brand logo or name |  |
| 7 | Keyboard open | Dharma, Workplace, CVS Health and 5 more. |
| 8 | Terms or privacy line | Small type on 6. Handshake shows a full paragraph. |
| 9 | Buttons for other sign-in methods | Apple on Houzz, Jumprope, Epidemic Sound and Pi. Google on Houzz, Epidemic Sound and Pi. Facebook on Spring, Houzz, Jumprope and Pi. Wallets on Rarible. |
| 10 | 'Forgot password?' link | Dharma, HelloFresh, Gymshark and 3 more. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Log-in form: Email or username and password, one button, and a forgot-password link.
- `v2` Sign-up form: Name, email and password on one screen, with a create-account button.
- `v3` One question at a time: A single field (or a first and last name pair) and a Next or Continue button. The keyboard is usually open.
- `v4` Other methods first: A stack of provider buttons (Apple, Google, Facebook, wallet, phone) with no form fields.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The main button is grey while the form is incomplete, and nothing marks what is missing. On Linktree every field is filled and the unticked terms box is the only gap.
2. The main button is cut off at the bottom edge, or a date picker covers the rest of the form.
3. Sign-in opens in a web page with a browser bar, so the type and colors change from the app.

## What the checked screens of each subtype have (the linter expects the same)

63 checked screens of this type; screens per subtype (a screen can be more than one): v1 12, v2 16, v3 19, v4 8.

- `v1` Log-in form
  - An email or username field and a password field
  - One filled log-in button
  - A forgot-password link near the password field
  - A back or close control at the top left
- `v2` Sign-up form
  - Two to five text fields, with a password field among them
  - An eye icon or a Show link on the password field
  - A filled create-account button, usually low on the screen
  - A back or close control at the top left
- `v3` One question at a time
  - A single text field and no password field
  - A filled Next or Continue button, usually in the middle third
  - A back control at the top left
  - The keyboard open at the bottom, on most
- `v4` Other methods first
  - A stack of buttons for other sign-in methods, three or four of them
  - No text field and no filled button
  - A brand logo or name near the top

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
