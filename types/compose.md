# This type: Compose (`compose`)

Also called: editor, composer, create screen, post editor, canvas
What it is for: Let the person make or change one thing, such as a post, note, photo, video or design, and then finish or drop it.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 8 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | The thing being made fills the middle | Image or video on Apple Photos, Cameo, Signal and 2 more. Canvas, board or timeline on Clover, Procreate Pocket, GoDaddy Studio and 2 more. Text page on Facebook Local, Digg, Medium and 4 more. Calendar, store, camera look or avatar on Not Boring Camera, Canopi, Shopify and Meta Quest. |
| 2 | A way out (Cancel, Close, X, back or Exit) | 15 at the top (Facebook Local, Digg, Canopi and 12 more) and 3 at the bottom left (Not Boring Camera, Cameo and Powder). |
| 3 | Commit button | 11 use a word (Post, Done, Add, Choose, Save, Next, Finished Editing) and 5 use a check or arrow (GoDaddy Studio, Givingli, Signal and 2 more). 9 sit top right and 7 sit low. |
| 4 | Tool strip or row of tool tabs | In the lower half on 13 of the 14. Only Procreate Pocket puts tools along the top. |
| 5 | Options panel under the work | Not Boring Camera, Apple Photos, Shopify and 4 more show settings or choices for the selected item. |
| 6 | Keyboard open | Medium, Givingli, Amie and 2 more. All five are writing screens. |
| 7 | Undo or redo arrows | Clover, Apple Photos, GoDaddy Studio and Play. |
| 8 | Audience or recipient chip | Facebook Local (Friends, Album), Signal (a named person), Mammoth (Everyone). |

## Variants (`v1` to `v4` in `variants`)

- `v1` Text composer: A page of text with the keyboard up and a formatting or media strip above it.
- `v2` Photo or video editor: The picture or clip fills the screen, with a dial, timeline or caption bar below.
- `v3` Canvas or builder: A board, page or layout with a tool strip and an options panel for the selected item.
- `v4` Customizer: A live preview of a camera look or an avatar, with swatches or style tiles below and a Done or Save button.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Text breaks in the middle of a word on the card ('Christma' then 's!') because of wide letter spacing.
2. Tool labels are very small and pale grey.
3. Labels on the timeline are too small to read.

## What the checked screens of each subtype have (the linter expects the same)

52 checked screens of this type; screens per subtype (a screen can be more than one): v1 21, v2 10, v3 10, v4 4.

- `v1` Text composer
  - The text page fills the middle of the screen
  - A way out, Cancel or Close, sits at the top
  - A commit button such as Post, Done or Next
  - The keyboard is open along the bottom
- `v2` Photo or video editor
  - The picture or clip fills the middle of the screen
  - A commit button such as Done, Next or Send
  - A way out, Cancel or Close, next to it
  - No keyboard is up
- `v3` Canvas or builder
  - The board, page or timeline fills the middle of the screen
  - A tool strip or row of tool tabs
  - A way out at the top of the screen
  - No keyboard is up
- `v4` Customizer

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
