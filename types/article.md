# This type: Article (`article`)

Also called: story, reader view, long read, document view, text page, post body
What it is for: Let the person read a long piece of text from top to bottom without distraction.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Body text in one full-width column | No screen splits the text into two columns. |
| 2 | Large headline near the top | All but Spark Mail, which is an email that shows only its own text. |
| 3 | Back, close or Done at the top | Top-left on IKEA Place, The Guardian, Spark Mail and 9 more. X at the top right on Dot, Done and Yik Yak. Missing on Queue, WWDC and The New York Times. |
| 4 | Bottom bar (tab bar or toolbar) | Tab bar on The Guardian, WWDC, The Atlantic Magazine and komoot. Toolbar with arrows or share on Spark Mail, Starbucks, The New York Times and Reeder 5. |
| 5 | Photo, video or illustration | Queue, The Guardian, Breeze and 4 more. |
| 6 | Subheadings inside the text | IKEA Place, The Guardian, WWDC and 4 more. |
| 7 | Serif type for the headline | Dot, Queue, The Guardian and 4 more. |
| 8 | Byline, date or last-updated line | Dot, IKEA Place, The Guardian and 3 more. |
| 9 | Tools at the top right (share, bookmark, text size, reader) | The Guardian, Spark Mail, Starbucks and 3 more. |
| 10 | One button below or over the text | Continue on IKEA Place, Start on Breeze, Learn More on Yik Yak, Done on Imprint. |

## Variants (`v1` to `v4` in `variants`)

- `v1` News or magazine story: A photo or video, a headline, a byline or date, then the body. Serif type on 4 of the 5 headlines.
- `v2` Policy, terms or notice: Plain text with subheadings and no photo, often with a Continue or Done step.
- `v3` Short lesson or update card: A few paragraphs or bullets with one step to continue, such as Start or Done.
- `v4` Outside content shown in the app: An email or a web page placed inside the app with the original styling.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The Continue button floats over the last lines of text and hides them.
2. Very small, dense type with little spacing: all-caps grey blocks on Starbucks and a long run of small text on WWDC.
3. The top row of tabs is cut off at the right edge, so part of it cannot be read.

## What the checked screens of each subtype have (the linter expects the same)

47 checked screens of this type; screens per subtype (a screen can be more than one): v1 11, v2 16, v3 12, v4 11.

- `v1` News or magazine story
  - A photo, video or illustration with the story
  - A large headline above the text
  - A back, close or Done control at the top
  - Body text in one column
- `v2` Policy or notice
  - Body text in one full-width column
  - A headline near the top
  - Subheadings that break up the text
  - No photo or video
- `v3` Short lesson card
  - Body text in one column
  - A back, close or Done control at the top
  - A headline above the text
  - One button near the bottom to continue
- `v4` Outside content
  - Body text in one full-width column
  - A back, close or Done control at the top
  - A headline above the text
  - A bottom bar with arrows or share

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
