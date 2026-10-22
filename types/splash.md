# This type: Splash (`splash`)

Also called: launch screen, launch image, startup screen, brand screen, boot screen
What it is for: Show the brand for a moment while the app starts.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 8 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Nothing to tap | Only Particle News has a button, and it belongs to a system dialog on top. |
| 2 | Logo or wordmark near the center | CHOPT is text only. Not Boring Camera shows a small icon at the top left. |
| 3 | Flat color or soft gradient fills the screen | Particle News and CHOPT use a textured background instead. |
| 4 | Saturated or dark brand color (not white or grey) | 9 saturated (Fidelity, Mozi, Nike SNKRS and 6 more), 5 near black or dark purple (Shipt, Mercedes-Benz, GIPHY and 2 more), 1 dark grey (Particle News). The other 4 are white or pale grey (Upside, Wise, Oportun and Not Boring Camera). |
| 5 | One line of text under the logo | A tagline (Particle News and Atoms), a loading message (Mozi), or a greeting (CHOPT). |
| 6 | Loading cue (dots or a message) | Credit Karma has faint dots under the wordmark. Mozi says 'Mozi'ing...'. |
| 7 | Small print at the bottom | Fidelity shows a version number and a legal footer. |
| 8 | System dialog on top of the splash | Particle News shows an Apple ID sign-in prompt over the logo. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Logo alone on a flat color: A single logo or wordmark centered on one color, with no other element.
- `v2` Logo with a line of text: The logo plus a tagline, a loading message or a legal footer.
- `v3` Logo with a loading cue: Dots or a message under the logo suggest the app is working.
- `v4` Greeting text with no logo: A short welcome line in large type on a patterned color field.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. A system sign-in prompt lands on top of the splash before the person has seen anything of the app.
2. Only a small app icon sits at the top left of a grey field. It reads as an unfinished launch image.
3. A text-only screen with no logo and no cue. Nothing says whether to wait or tap.

## What the checked screens of each subtype have (the linter expects the same)

59 checked screens of this type; screens per subtype (a screen can be more than one): v1 33, v2 14, v3 3, v4 2.

- `v1` Logo alone on color
  - One logo or wordmark in the middle of the screen
  - One flat color or soft gradient behind it
  - No tagline, loading cue or small print
  - Nothing to tap
- `v2` Logo with extra text
  - A logo or wordmark on every screen
  - A tagline under the logo or small print at the bottom
  - A saturated or dark brand color behind it
  - Nothing to tap
- `v3` Logo with a loading cue
- `v4` Greeting text with no logo

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
