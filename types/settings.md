# This type: Settings (`settings`)

Also called: preferences, app settings, options, notification settings, appearance settings, controls
What it is for: Let the person change how the app behaves, looks or notifies them, and see the current choice at a glance.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Back arrow or close X at the top | 14 back arrows, 6 close X (on sheets). Missing on zenly, Starlink, IKEA Home smart and HODINKEE. |
| 2 | Rows with a chevron that open a sub-page | Chevron at the right edge: Feeld, TechCrunch, Eight Sleep and 10 more. |
| 3 | On/off toggle at the right end of the row | All 12 put the label on the left and the switch on the right. |
| 4 | Group heading in small grey or capital type | Examples: SPEECH, ABOUT, SCHEDULE, MODES, App Settings, Legal. |
| 5 | Grey help sentence under a row | The Athletic, Feeld, zenly and 6 more. Used mostly under toggles whose effect is not obvious. |
| 6 | Current value shown at the right of the row | USD, Moonlit, On, Light, Default, noon, midnight, a username. |
| 7 | Slider, stepper, radio, check or time picker | Slider on Rise and Mammoth, steppers on Eight Sleep, equaliser on Spotify, radios on Remote Global HR, check mark on Stadium Live, time boxes on Waking Up. |
| 8 | Bottom tab bar still visible | The Athletic, Buddy, Spotify and 3 more. |
| 9 | Log out, sign out or reset row near the end | Feeld, IGTV, Klima and 2 more. Red text on Feeld; a confirm alert on Klima and HODINKEE. |
| 10 | Version number | Small grey text at the end of the list: Feeld, Starlink, Klima and 2 more. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Switch list: Labelled rows with a toggle and a grey explanation under each, usually for notifications.
- `v2` Pick one option: A short list where one choice is selected: a currency, a notification level, a theme.
- `v3` Sliders and steppers: A range or number is set with a slider, a stepper or an equaliser, often with a live preview.
- `v4` Link list and exits: Rows that open help, legal and privacy pages, with Log out or Reset at the end.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Help text is very small grey type, and on dark pages it is hard to read.
2. A page titled Settings holds feedback links and promotions for other apps rather than controls.
3. The page holds one row and a large empty area.

## What the checked screens of each subtype have (the linter expects the same)

61 checked screens of this type; screens per subtype (a screen can be more than one): v1 25, v2 12, v3 5, v4 21.

- `v1` Switch list
  - An on/off toggle at the right end of the row, on nearly every screen
  - A grey help sentence under many of the switches
  - A back arrow or close X at the top
- `v2` Pick one option
  - A radio, check or other pick control beside the options
  - A back arrow or close X at the top
  - Few or no switches and no chevron rows
- `v3` Sliders and steppers
- `v4` Link list and exits
  - Rows with a chevron that open a sub-page
  - A back arrow or close X at the top
  - Small group headings above the rows

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
