# This type: Camera (`camera`)

Also called: viewfinder, capture screen, scanner, AR view, photo capture
What it is for: Let the person point the phone at something and capture it, scan it or place an object in the room.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Black or near-black surround | Glow, HelloFresh, HQ Trivia and 13 more. The four light ones are Chase UK, Houzz, IKEA Place and LookUp. |
| 2 | Large round button at the bottom centre | A shutter or record button on Glow, Kino, Houzz and 6 more. On IKEA Place it is a check that places the object. |
| 3 | Close, cancel or back control | Top left on HelloFresh, Airbnb, Warby Parker and 5 more. Bottom left on Glow. Top right on LookUp. |
| 4 | Frame, bracket or circle that shows where to aim or how the photo is cropped | Halide, Airbnb, Warby Parker and 2 more. |
| 5 | One line of instruction or status text over the view | Warby Parker ('Can't detect box'), Chase UK ('Move your ID inside the border'), Betterment (a yes or no question), Yuka (a banner), GIPHY ('Swipe left and right'). |
| 6 | Flash control | Glow, Halide, Apple Mail and 2 more. Docusign spells it out as Auto, On, Off. |
| 7 | Mode, zoom or settings row | Zoom and PHOTO label on Glow, Camera and Photo library tabs on HelloFresh, a settings strip on Halide, zoom on Kino, a filter carousel on GIPHY. |
| 8 | Camera flip button | Glow, Otter.ai, Dispo and GIPHY. |
| 9 | Review controls after the shot | Retake and Use Photo on HQ Trivia and Postmates, a red cross and green check on Betterment, Edit photo on Airbnb. |
| 10 | Shortcut to the photo library | A Photo library tab on HelloFresh, a thumbnail on GIPHY, a Library chip on Dispo. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Photo or video capture: A plain viewfinder with a shutter, plus flash, zoom or flip. Halide adds histogram and manual controls, and musical.ly shows a record countdown.
- `v2` Guided scan: The camera reads a box, an ID, a page or a label, often with a frame and a line of help.
- `v3` AR and effects: The live view carries a virtual object or filter, with a product label (Houzz and IKEA Place) or a filter carousel (GIPHY).
- `v4` Review after capture: The shot is shown back with accept, retake or edit controls and no viewfinder.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The instruction is grey text on a light grey photo and is hard to read.
2. The controls are dark grey on black and almost disappear.
3. A banner and a dialog both ask a question over the viewfinder at the same time.

## What the checked screens of each subtype have (the linter expects the same)

51 checked screens of this type; screens per subtype (a screen can be more than one): v1 19, v2 22, v3 7, v4 9.

- `v1` Photo or video capture
  - A black or near-black surround around the live view
  - One big round capture button at the bottom centre
  - A mode, zoom or settings row
- `v2` Guided scan
  - A black or near-black surround around the view
  - A small close or back control, usually at the top
  - A frame or bracket that shows where to aim
  - One line of instruction or status text
- `v3` AR and effects
- `v4` Review after capture
  - Two review controls at the bottom, such as retake and use photo
  - A black or near-black surround behind the shot
  - No big round capture button, because the shot is already taken
  - No aiming frame

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
