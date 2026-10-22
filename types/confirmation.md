# This type: Confirmation (`confirmation`)

Also called: success screen, order confirmation, receipt, all set screen, thank-you screen, done screen.
What it is for: Tell the person that what they just did worked, and show what to do next.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 9 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Headline that says what happened | You're all set, Order placed, Well done, You've transferred $10.00, Request submitted. Not on GCOO, Waymo and Blank Street. |
| 2 | One main button | 12 of the 15 sit in the bottom third. 8 say Done or Continue; the others name the next step (Let's go, Start reading, Start sending likes). |
| 3 | Close X or back arrow | Top corner. Usually shown on screens that also have a main button. |
| 4 | Line of text on what was done or what happens next | One or two sentences under the headline: WeTransfer, The New Yorker, Flo and 7 more. |
| 5 | Check mark icon | A large check on WeTransfer, The New Yorker, Flo and 5 more; small check bullets on HEY. |
| 6 | Second action or what-next options | Make Another Transfer (Mercury), Earn 75 pounds (Plum), Add to Siri and Track with Alexa (Panera Bread), a what-happens-next block (HEY), thumbs (GCOO, Brex and Blank Street). |
| 7 | Large picture, mascot or illustration | bless, Epsy, InPost UK and 3 more. |
| 8 | Amount or order details in rows | Stake, GCOO, Brex and Blank Street. Order type and price on Stake; items, tax, tip and payment on Blank Street. |
| 9 | Thumbs or star rating | GCOO, Panera Bread, Brex and Blank Street; all four follow an order, a ride or a matched receipt. |

## Variants (`v1` to `v4` in `variants`)

- `v1` All set after setup: A full page with a check or picture, a short line and one button, shown when an account or device is ready.
- `v2` Receipt: Order or ride details in rows, with the total, and sometimes a rating or a pickup note.
- `v3` Alert or sheet: A small panel over the previous page says Request submitted, Thank you or Well done, with one button.
- `v4` Done, then the next job: The result is stated, then a button or link pushes to the next task: make another transfer, start reading, add funds, earn a bonus.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Only a check mark on a plain screen, with no words and no button to leave.
2. The only control is a round arrow with no label, and the body text is small grey type on black.
3. No button is visible; the only exit is a small X in a corner.

## What the checked screens of each subtype have (the linter expects the same)

54 checked screens of this type; screens per subtype (a screen can be more than one): v1 24, v2 8, v3 11, v4 12.

- `v1` All set after setup
  - A headline that says what is ready, in the top or middle of the screen
  - A check mark or a large picture as the sign of success
  - A line of text on what was done or what comes next
  - One main button, usually in the bottom third
- `v2` Order receipt
  - Amount or order details in rows
  - A second action or what-next option
  - A line of text on what was done or what happens next
- `v3` Alert or sheet
  - A headline that says what happened
  - A line of text under it
  - One main button, in the middle or bottom of the screen
  - No close X: the button is the way out
- `v4` Done, then next job
  - A headline that says what is done
  - One main button, usually in the bottom third
  - A line of text on what was done or what comes next
  - A second option for the next job, usually near the bottom

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
