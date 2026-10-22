# This type: Gallery (`gallery`)

Also called: photo viewer, image viewer, lightbox, media browser, photo carousel, full-screen photo
What it is for: Let the person look at one photo at full size and move through the set.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 8 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | One large photo that fills most of the screen | Fiverr, IDAGIO, Lake and 12 more. How We Feel and Placify inset the photo as a card. IDAGIO shows full-width booklet pages. |
| 2 | Close or back control | Top left on Fiverr, IDAGIO, GetYourGuide and 9 more. Top right on Lake and Hollister Co. A Close button at the bottom on GCOO. Missing on Sephora and Hush. |
| 3 | Caption, credit or handle that goes with the photo | Fiverr and GetYourGuide give a review quote or name and date. Kitchen Stories, Roku and Zesty give a name and when. Placify, Skyscanner and Nike Training Club give a title, source or handle (above the photo on Nike Training Club). |
| 4 | Black or very dark backdrop | Fiverr, Lake, GetYourGuide and 5 more. |
| 5 | Position counter or page dots | Counter on Fiverr, Roku, Skyscanner and Zomato. Dots on Hollister Co, Hush and Zesty. |
| 6 | One action button | Put into My Studio on Lake, Save Photo on How We Feel, Save on Placify, Close on GCOO, REFINE on Sephora. |
| 7 | Icons for share, favorite, flag or delete | Share on IDAGIO, flag and heart on Kitchen Stories, cast and delete on Roku. |
| 8 | Bottom tab bar still visible | Roku, Sephora and Workplace. Each keeps the app around the photos. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Full-screen photo with a credit: A large photo on black or white with a credit line or caption, and often a counter such as 1 of 2.
- `v2` Photo carousel with dots: A product or venue photo with dots or arrows that show more photos can be swiped.
- `v3` Photo with one button: The photo has a single action under it: put into a studio, save a photo, save, or close.
- `v4` Thumbnail grid inside the app: A grid of small photos from other users with tabs or an Add Photo row above.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The close icon is small and sits at the very edge of the screen.
2. The photos fill only the top part and the rest of the screen is blank white.
3. The Close button is the only way out, and it is grey text on a light grey box that is easy to miss.

## What the checked screens of each subtype have (the linter expects the same)

41 checked screens of this type; screens per subtype (a screen can be more than one): v1 22, v2 7, v3 6, v4 8.

- `v1` Photo with a credit
  - One large photo in the middle of the screen
  - A close or back control at the top
  - A caption or credit, most often below the photo
  - A black or very dark backdrop around the photo
- `v2` Photo carousel with dots
- `v3` Photo with one button
- `v4` In-app thumbnail grid
  - A grid of small photo tiles, not one large photo
  - A back or close control at the top
  - A title row or app header above the tiles

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
