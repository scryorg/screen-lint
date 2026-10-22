# This type: Permission (`permission`)

Also called: pre-prompt, soft ask, priming screen, access request, notification opt-in, consent screen
What it is for: Ask for access to notifications, location, camera, tracking or similar, and say what the person gets in return.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 8 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Reason written in the app's own words | Missing on Rarible, Bloom and Google Podcasts, where the system dialog is the only ask visible. |
| 2 | App's own button | Labels: Enable Notifications, Allow, Continue, Find My Location, Share location, Yes. |
| 3 | Picture or icon | Apple News and Tempo show what the notification will look like. |
| 4 | Visible no, skip or not-now choice | Not Now, Skip, Maybe later, No thanks, Remind Me Later, or Enter address. Yes/No pairs on Lloyds Mobile Banking and Vevo. |
| 5 | System permission dialog on top | Hollister Co, Fitbod, Rarible and 5 more. |
| 6 | Back, close or skip at the top | Fitbod, Google Fit, Lloyds Mobile Banking and 5 more. |
| 7 | Several choices on one screen (toggles, boxes, Yes/No) | Hollister Co, Lloyds Mobile Banking, Halide and 2 more. Google Fit has a single toggle. |
| 8 | Privacy or policy link | A policy link on Opera and Lloyds Mobile Banking. Halide has a 'Tap to learn more' line under the list. |

## Variants (`v1` to `v4` in `variants`)

- `v1` App asks first: The app's own screen explains the ask and has its own buttons. The system dialog comes after the tap.
- `v2` System dialog on top: The phone's own Allow and Don't Allow dialog is showing over the app.
- `v3` Data consent: Choices about ads, analytics and tracking, shown as Yes/No pairs, a checklist or a system tracking prompt.
- `v4` Several asks on one screen: A toggle, box or circle for each ask, with a reason under each.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Only the system dialog is visible, so the reason for the ask shows nowhere.
2. Long consent text runs under the tab bar, and the last policy line is cut off.
3. The system dialog asks about notifications while the screen behind it says 'Turn on Location Services'.

## What the checked screens of each subtype have (the linter expects the same)

58 checked screens of this type; screens per subtype (a screen can be more than one): v1 37, v2 18, v3 9, v4 6.

- `v1` App asks first
  - A reason in the app's own words, on nearly every screen
  - One button of the app's own, in the bottom third
  - A picture or icon that shows what the access is for, on most screens
- `v2` System dialog on top
  - One phone dialog, in the middle third
  - The app's own screen dimmed behind the dialog
  - Usually no back or close control at the top
- `v3` Data consent
  - A reason in the app's own words, on nearly every screen
  - One button of the app's own, in the bottom third
  - A privacy or policy link, in the middle or bottom third, on most screens
- `v4` Several asks on one screen

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
