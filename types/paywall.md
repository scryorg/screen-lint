# This type: Paywall (`paywall`)

Also called: upgrade screen, subscription screen, plan picker, premium offer, trial offer, go Pro screen
What it is for: Show what paid access gives you and let you start paying, or start a trial, in one step.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Way out: close X, back arrow, Not Now or No Thanks | A close X on 20 and a back arrow on 6. Text like Not Now, No Thanks or Cancel on the other 11: Castro, Done, Apple Invites and 8 more. |
| 2 | One filled main button | 28 of the 33 sit in the bottom third; TIDAL, Careem, WeTransfer, Apple Games and Timepage put it higher. Labels: Continue, Subscribe, Upgrade Now, Start Free Month, Try ... Free. |
| 3 | Price in currency | On the 8 screens with the App Store sheet, the price is in the sheet. 12 screens show no price at all. |
| 4 | Large illustration, art or 3D object | Coin on Not Boring Calculator, gold badge on Not Boring Weather, podcast covers on Apple Podcasts, line art on Lake, a tree on bunq. |
| 5 | Fine print on renewal, cancelling or refunds | From one line on Alfread (Cancel anytime. Plan renews automatically.) to a full block of legal text on TIDAL. Blinkist and Canva also promise a reminder before the trial ends. |
| 6 | Plan choice with two or more priced options | 10 are a monthly and yearly pair, and 9 of those mark the yearly plan with a badge: Save 50%, 25% OFF, Best Value, $19.89 saved. The Guardian shows 3 lengths, Dropbox 3 tiers, Careem 5 passes. |
| 7 | Free-trial wording | Trial length is in the button or a line near it: Epicurious, iFood, Apple Invites and 10 more. |
| 8 | Benefit list | 1 to 9 short rows: Airwallex, Apple Invites, Not Boring Weather and 16 more. |
| 9 | Restore purchase link | Small text at the top or bottom: TIDAL, Not Boring Weather, Atoms, Citymapper and 5 more. |
| 10 | App Store purchase sheet on top | Epicurious, Finimize, Tumblr, Pocket, Canva, Mimo, MUBI GO and Squarespace. The offer page is dimmed behind it. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Plan picker: Two or more priced plans side by side, one button to confirm the chosen plan.
- `v2` Benefit list and one button: A short list of what is included, then a single main button.
- `v3` Hero art, little text: A big picture and a line or two of copy in place of a benefit list; 6 of the 14 also leave the price for the next screen.
- `v4` System purchase sheet: The App Store sheet with price and trial terms sits over the dimmed offer page.

## Pitfalls (keys "1" to "4" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. No price on the offer screen, so the cost is only found after the button is tapped.
2. The close control is a faint X or link over art or a pale page, under the 3:1 a control needs, and easy to miss.
3. A full-screen block of small legal text sits next to the offer and pushes the plan details to the top.
4. The main button's label or the price is too pale to read against what is behind it, under 3:1.

## What the checked screens of each subtype have (the linter expects the same)

46 checked screens of this type; screens per subtype (a screen can be more than one): v1 15, v2 20, v3 15, v4 7.

- `v1` Plan picker
  - Two or more plans side by side, each with its price
  - A way out at the top: a close X, a back arrow or Not Now
  - One filled button low on the screen that confirms the chosen plan
- `v2` Benefit list, one button
  - A list of benefits in the top or middle of the screen
  - One filled button at the bottom
  - A way out at the top
  - A price on most of them
- `v3` Hero art, little text
  - A large picture, illustration or art object in the top or middle of the screen
  - A filled button at the bottom on most
  - A way out at the top on most
  - No benefit list: a line or two of copy instead
- `v4` System purchase sheet
  - The system purchase sheet at the bottom, over the offer page
  - A price on the screen
  - Fine print on renewal or cancelling on most
  - No filled main button on the page: the sheet takes its place

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
