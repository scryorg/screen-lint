# This type: Checkout (`checkout`)

Also called: cart, basket, shopping bag, order summary, payment screen, review order, place order screen
What it is for: Let the person check what they are buying, choose how to pay, and commit with one clear button.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Back, close or Done control at the top | Missing only on Mucho and Jet, which sit inside a tab bar. |
| 2 | Main pay or continue button | 12 of the 13 sit in the bottom third. Labels: Place order, Place delivery order, Proceed to checkout, Go to checkout, Start investment, Buy now, Pay 31,000 won. |
| 3 | Payment method row or card fields | Card number and CVC fields on Vivino and SKIMS; a saved-card row on Gojek, Wonder, Rent the Runway and Taco Bell; a method list on Trainline, H&M and Coinbase Wallet. |
| 4 | Total or amount to pay | Shown as Total, Order Total, Est. total, or the amount in the heading (Signal). |
| 5 | Promo, coupon or gift-card entry | A text field with Apply (Rent the Runway and Jet), or a row that opens a code screen (Wonder and Under Armour). |
| 6 | Wallet or pay-later brand: Apple Pay, PayPal, Klarna, Afterpay | As filled buttons on Burberry and Signal, as list rows on H&M and SKIMS. |
| 7 | Itemised cost lines (subtotal, fees, tax) | Gojek, Burberry, Wonder and 3 more. |
| 8 | Product lines with picture, quantity and price | Burberry, Under Armour, Redbubble and 3 more. |
| 9 | Address or delivery row | Shipping address on Under Armour and Rent the Runway, delivery address on Cornershop, billing address on SKIMS. |
| 10 | Tip choice | Chips with preset amounts on Wonder, Taco Bell and CHOPT; all three are food delivery. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Cart or basket: Items with pictures and quantities, a running price, and a button that moves on to checkout.
- `v2` Order summary with Place order: One long page of address, payment, code, cost lines and a final button.
- `v3` Payment method step: Only the way to pay: card fields, a list of wallets, or a list of saved cards.
- `v4` Quick pay sheet: A short sheet over another screen with wallet buttons or card fields and nothing else.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The main button is greyed out while the rows above still read Enter shipping address and Select payment method.
2. The page shows item prices or fields but the total is out of view, so the cost is not visible before the button.
3. Cost lines are small grey text with an info icon beside each fee, which makes the fees harder to read than the total.

## What the checked screens of each subtype have (the linter expects the same)

60 checked screens of this type; screens per subtype (a screen can be more than one): v1 16, v2 28, v3 14, v4 5.

- `v1` Cart or basket
  - Product lines with a picture, a quantity and a price
  - A back or close control at the top
  - One main button low on the screen that moves on to checkout
- `v2` Order summary
  - A back, close or Done control at the top
  - One main Place order button in the bottom third
  - A payment method row or card fields
  - A total or amount to pay
- `v3` Payment method step
  - Card fields, saved cards or a list of payment methods
  - A back, close or Done control at the top
  - Only the way to pay, with no product lines and no cost breakdown
- `v4` Quick pay sheet

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
