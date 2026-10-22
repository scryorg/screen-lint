# This type: Verify (`verify`)

Also called: one-time code, OTP screen, confirm your email, check your inbox, two-factor step, security code
What it is for: Check that the person owns the email, phone or device they gave, by asking for a code or a tap on a link.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Title that says what to do | All but IKEA Home smart, which opens with an explanation instead. |
| 2 | Back, close or cancel at the top | Missing only on Facebook and Monese. |
| 3 | Says where the code or link was sent | Email on 10 screens and phone on 4 (Manus, Google Pay, Dave and Blank Street). Some addresses are blurred in the capture. |
| 4 | Code entry | A single field on 9 screens. Separate boxes or slots on 5 (Vivid, Google Pay, Netflix and 2 more). |
| 5 | Button to send the code or move on | Grey or pale while the field is empty on Atoms, Alipay and sweetgreen. |
| 6 | Resend control | Manus, Vivid, Netflix and 7 more. Three show a countdown before it works (Manus, Vivid and Powder). |
| 7 | Way out if nothing arrives | Change number or email (Manus and Netflix), get help (Netflix), contact support (Blank Street and sweetgreen), log out (Figma), another method (Alipay), 'not you?' (Facebook). |
| 8 | Countdown or expiry time stated | Countdowns on Manus, Vivid and Powder. Expiry notes on Netflix, State Farm and sweetgreen. |
| 9 | Number keypad open | Vivid, Netflix, Powder and 3 more. No code screen shows a letter keyboard. |
| 10 | Illustration or photo | IKEA Home smart, Figma, Nu and 2 more. None of the five has a code field. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Code in separate boxes: Four or six boxes or slots for the digits, with no submit button.
- `v2` Code in one field with a button: A single field for the code and a Next, Verify or Continue button (only a small Next link at the top on State Farm).
- `v3` Check your email: No field. The person taps a link in an email and comes back.
- `v4` Identity check without a sent code: A reason and a Continue button (Nu and Acorns), or a question about part of an ID number (Alipay).

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. An iOS save-password dialog sits on top of the code form.
2. A marketing consent box and a block of fine print sit between the code field and the Continue button.
3. The main button is pale or grey and nothing says what is missing.

## What the checked screens of each subtype have (the linter expects the same)

53 checked screens of this type; screens per subtype (a screen can be more than one): v1 23, v2 22, v3 4, v4 3.

- `v1` Separate code boxes
  - A title that says what to do, near the top
  - One box or slot per digit, with no submit button
  - A back or close control at the top
  - The number keypad open under the form
- `v2` One field, one button
  - A title that says what to do, near the top
  - A line saying where the code was sent
  - A single code field with a button to send it
  - A back or close control at the top
- `v3` Check your email
- `v4` Identity check without a sent code

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
