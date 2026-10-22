# Classifier guide: which of the 35 types is this screen?

Pick the type from the picture (`grid.jpg`, with `ocr.json` for the words). Name one type and one runner-up, one
sentence each. The type decides which rules the screen is graded against, so a wrong type gives a wrong grade.

## How to decide

1. Decide by the job the screen does for the person right now, not by its title or its look. A page titled
   "Profile" that shows only streaks and a chart is `stats`; a "Menu" that is mostly people with Add buttons is
   `list`.
2. Each entry below gives what the type is for, what you can see on it, and the types it is most often mistaken
   for, with the cue that decides. The confusions come from the checked screens: where a screen carried one
   label and a careful look said another.
3. A sheet, popup or alert that is the whole job of the screen (a rating sheet, an email popup over a dimmed page)
   is classified by that job. A small system dialog over an app page asking for access is `permission`.
4. A screen that names the type but does not do its job is another type. If none of the 35 fits, say `other`.

You confirm the type once more when you read the screen: `types/<type>.md` says what the type is for, and
`is_type` in obs.json is your answer. If you set it false, `lint.py` stops with exit 3 and you come back here
with the type you named in `instead`.

## Not an iPhone app screen: say so and stop

The rules were made from iPhone app screens. A web page in a browser, a desktop or Mac window, an iPad layout, an
Android screen, a marketing image, a photograph, a slide, a lock screen or a widget is not graded. Say what it
is and that the rules are for iPhone app screens. `prep.py` prints a note when the width or the height-to-width
ratio is not a phone's. A Figma frame exported at 390 px wide (1x) is fine.

## `other`: an iPhone screen that fits none of the 35

Say which type is closest and that no rules fit; do not grade. Typical cases: the system photo picker when it
is not a step in making something, a waiting interstitial with nothing to do and no brand (a spinner and one
line), a Live Activity banner on a blank page, a web page inside a sheet with nothing to act on.

---

## Getting in

### `splash` Splash
For: show the brand for a moment while the app starts.
Tell it by: nothing to tap; a logo or wordmark near the centre; flat colour or soft gradient fills the screen,
often saturated or dark; at most one line of text or loading dots.
Mistaken for: `activity`, when there is no brand mark and a back or close control or a progress message ("Loading
visuals... 5%", "Building your store") holds the person on a task: that is `activity`. `home`, when a loading shell
shows the tab bar: that is part of the app. `welcome`, when there is a headline and a button.

### `welcome` Welcome
For: tell a new person in one short line what the app does for them, then let them start.
Tell it by: a headline-size message; a picture, illustration or product shot; a button in the bottom third; page
dots; sometimes log-in buttons under it.
Mistaken for: `confirmation`, when the headline says something worked or finished ("You're on the list", "Next step
unlocked", a praise page at the end of a story): that is `confirmation`, not an intro. `sign-in`, when the way in
(Continue with email, Apple, Google) is the main thing and not a value line.

### `sign-in` Sign-in
For: let the person prove who they are, or make an account, with as little typing as possible.
Tell it by: a text field for email or phone, often a password field with a show/hide control; one filled button;
buttons for other methods (Apple, Google); a terms line; a "Forgot password?" link; the keyboard often open.
Mistaken for: `verify`, when a code was sent to an email or phone to prove the person owns it: that is `verify`; a
PIN, passcode or biometric that unlocks the person's own account is `sign-in`. `form`, when it asks for a phone
number to send a login code: that is `sign-in`. `setup`, when it asks one profile question after the account exists.

### `verify` Verify
For: check that the person owns the email, phone or device they gave, by asking for a code or a tap on a link.
Tell it by: a title that says what to do; it says where the code or link was sent; code boxes or one code field;
a Resend control; a countdown; a number pad.
Mistaken for: `sign-in`, for a PIN or passcode that unlocks the person's own account and sends nothing to an email
or phone. `setup`, when the person is creating an app passcode.

### `permission` Permission
For: ask for access to notifications, location, camera, tracking or similar, and say what the person gets.
Tell it by: a reason in the app's own words; the app's own button (Allow, Enable); a picture or icon; a visible
Not Now or Skip; or the system permission dialog on top of the app page.
Mistaken for: `setup` or `welcome`, when the screen only collects an answer or explains the app. `confirmation`, when
the headline says a thing was done and a notification opt-in is only a side button.

### `setup` Setup
For: collect one answer or one connection at a time so the app can be set up for this person.
Tell it by: a heading phrased as a question or an instruction; tappable answer choices (rows, cards, chips) or
one typed answer; a Next or Continue button; a progress bar; Skip or Later.
Mistaken for: `form`, a plain data-entry screen that saves or sends something: `setup` is the one-question-at-a-time
first-run step. `verify`, for a code screen: a passcode being created is `setup`.

## Finding

### `home` Home
For: show a person what is new and what needs attention, then give a short way into what they came to do.
Tell it by: the bottom tab bar; several kinds of block, each under a short heading; a row that scrolls sideways;
a large photo block; a number or ring summary; a greeting or date; icons for account or alerts at the top.
Mistaken for: `feed`, which is one stream of the same kind of card (posts, stories); `home` mixes block kinds.
`catalog`, when a promo banner sits above a single shelf of cards with the Home tab selected: that is `home`.
`list`, when the app's front screen is plain rows of records (a watchlist): the rows are the content, so `list`.

### `feed` Feed
For: let a person scroll through a steady supply of posts, stories or articles.
Tell it by: an image, video or logo on each item; a source or author line and a time; like, react, save or
vote actions and counts on each item; chips or tabs that change the stream; the tab bar.
Mistaken for: `catalog`, when the cards are things to pick and join (challenges, groups, products, job listings)
and no one posted them: that is `catalog`. `chat`, `article`, when it is comments or poll results under a post:
many people's comments with no compose field is `feed`.

### `catalog` Catalog
For: show many things of one kind (products, meals, songs, places) so the person can scan them and pick one.
Tell it by: a photo or cover leading each item; a grid, shelves or rows with thumbnails; category tabs or
chips; a filter or sort control; a price on the item; a result count; the tab bar.
Mistaken for: `feed`, when each item is a post by someone with a time and actions. `search`, when the field holds a
typed query or has focus and the results sit under it. `list`, when it is records to open or edit (saved items,
a product picker with checkboxes) and not a browse of photos.

### `search` Search
For: let a person type what they are looking for and get to it without browsing.
Tell it by: a search field with a placeholder or a typed query; suggestions, recent searches or results under
it; Cancel or a clear X; the keyboard open.
Mistaken for: `catalog`, when the results fill the screen as photo cards under a title and tabs and the field is only
an icon: that is `catalog`.

### `filter` Filter
For: let a person narrow a long list by setting a few choices, then go back to a shorter list.
Tell it by: a sheet or page of grouped choices (checkboxes, radio buttons, chips, a price range); Reset or Clear;
a main button at the bottom, often with a count ("Show 42 results"); a close control in the header.
Mistaken for: `settings`, when the choices change how something looks or which items show (chart choices, map
layers, a sort option with switches) and narrow no list of results: that is `settings`.

### `map` Map
For: show where things are, so the person can pick a place or point on the map and act on it.
Tell it by: a map filling the width and most of the height; pins or icons; a card or panel docked at the bottom;
a locate arrow; floating pills or chips; a search field over the map.
Mistaken for: `activity`, when a live trip, delivery or incident is the task and one main control sits on the map:
that is `activity`.

## Viewing

### `detail` Detail
For: show everything about one thing the person picked, and put the next step within reach.
Tell it by: a back or down arrow; the item's name as a large heading; a key fact beside it (price, date, length,
status); a large photo or video at the top; a block of description; a filled button in the bottom third; a
rail of related items.
Mistaken for: `article`, when the page is mostly long running text with a headline. `list`, when it is a titled page
of rows of records, even with an Add row. `form`, when a popup or sheet that asks for one input is the screen.
`confirmation`, when nothing says an action worked (a reservation page, a past order). `player`, when the player
is only a small strip above notes. `activity`, when the page for one reward or trip launches the task elsewhere:
that is `detail`.

### `article` Article
For: let the person read a long piece of text from top to bottom without distraction.
Tell it by: body text in one full-width column; a large headline near the top, often serif; a byline or date;
subheadings inside the text; share or bookmark tools at the top right.
Mistaken for: `detail`, for one item with facts and a next action (a single review, a Notion page with a table).
`other`, for a paged card with a headline and one chart and no running text. `help`, for terms, privacy
and answers: policy text fits either, so pick `help` when it is reached from support or settings and `article` when it
is a story, a notice or a document read for its own sake.

### `player` Player
For: play one video, track or live stream and give the few controls needed to steer it.
Tell it by: large video, artwork or photo; the title; a scrub bar and elapsed and remaining times; a play or
pause button; skip buttons; a down arrow to minimise; share, like or queue icons; a live badge.
Mistaken for: `detail`, when the player is a strip of a quarter of the height or less above description or
episode notes. `camera`, for a live feed from another device (a car camera): nothing is captured by this phone,
so it is `player`.

### `gallery` Gallery
For: let the person look at one photo at full size and move through the set.
Tell it by: one large photo filling most of the screen on a black or dark backdrop; a close or back control;
a position counter or page dots; a caption or credit; one action or a few icons.
Mistaken for: the system photo picker, a grid of the person's own photos with Cancel, Albums and Add: it is not a
viewer. Call it `compose` when it is a step in making a post or message; otherwise `other`.

### `profile` Profile
For: show who a person, creator or business is, and give a reason to follow, contact or trust them.
Tell it by: an avatar or portrait; a name or handle as a heading; a row of counts (followers, ratings); a
Follow, Add or Edit button; tabs; a grid or list of what they made; a banner behind the avatar.
Mistaken for: `account`, which is the signed-in person's details, plan and way to leave. `stats`, when there is no
avatar or name and the page shows counts, streaks, badges or a chart, even under the title Profile.

## Making and talking

### `chat` Chat
For: let the person read and write one running conversation with a person, a group or an AI.
Tell it by: messages as bubbles, the person's own filled and on the right; a text field pinned to the bottom with
a send, mic or attach button; a header with a title; a time stamp; starter buttons before the first message.
Mistaken for: `inbox`, the list of many threads. `feed`, for comments under a post with no field to write in.
`share`, for a send-to-people sheet drawn over a thread. `compose`, for a recipient picker before the first thread.

### `inbox` Inbox
For: show every conversation or message in one list so the person can find the one to open.
Tell it by: a title that names the list; rows with a name, a preview and a time; round avatars; unread markers;
a search field; a new-message button; an empty-state message.
Mistaken for: `notifications`, which tells what happened (a like, a reminder) and does not hold messages.
`chat`, when one thread is open. `list`, for rows of records that are not messages.

### `compose` Compose
For: let the person make or change one thing (a post, note, photo, video, design) and then finish or drop it.
Tell it by: the thing being made fills the middle; a way out (Cancel, Close, X); a commit button (Post, Save,
Done, Send); a tool strip; an options panel under the work; undo and redo; the keyboard open on a text card.
Mistaken for: `form`, when it collects answers (fields, sliders, pickers, a feedback box) and nothing being made is
visible. `camera`, when a live viewfinder and shutter are shown: editing a captured photo is `compose`. `gallery`
or `other`, for a photo picker grid.

### `camera` Camera
For: let the person point the phone at something and capture it, scan it or place an object in the room.
Tell it by: a black or near-black surround; a large round shutter button at the bottom centre; close or back; a
frame or bracket showing where to aim; one line of instruction; flash, flip, zoom and mode controls; a library
shortcut.
Mistaken for: `compose`, when a captured photo is being drawn on or a plan is being edited with no viewfinder.
`player`, for a remote live feed. A screen-recording start sheet is `compose` or `other`.

### `form` Form
For: collect a few facts, choices or amounts from the person so the app can save, book, send or change something.
Tell it by: a title that names the task; labelled fields; pickers, toggles, dropdowns, chips or a date row; a
Cancel word, back arrow or X; a commit button (Save, Submit, Done) at the bottom or in the top bar; often a sheet.
Mistaken for: `compose`, where something being made is on screen. `setup`, the first-run one-question step. `sign-in`,
when it asks for a phone number to send a login code. `detail`, when a rating or email popup over a dimmed page is
the whole job: that is `form`.

### `share` Share
For: help the person send something out of the app, or bring other people in, in a few taps.
Tell it by: a way out (X, Cancel, Done); a row of app icons to send to; a link or code with a copy action; a
preview of what is shared; reward wording ("Give $10, get $10"); a bottom sheet over a dimmed screen.
Mistaken for: `chat`, when the sheet sits over a thread and only picks people to send to: that is `share`.

## Tracking

### `calendar` Calendar
For: let the person pick a date or a time, or read what is planned on which day.
Tell it by: a month grid of days in seven columns; the selected day filled or ringed; a month name; a time wheel
or slots; a week strip; rows of events under dated headings; often a sheet over a dimmed screen.
Mistaken for: `form`, when dates and times are plain rows among other fields: that is `form`. `list`, when the
rows are records and not events tied to days. An agenda (events under dated headings) is `calendar`.

### `stats` Stats
For: show the person how they are doing, in a few figures or one drawing, over a stretch of time.
Tell it by: a chart, gauge or ring; a period named or switchable (Week, Month); one large headline number or
score; rows of a label and a right-aligned value; one sentence reading the numbers; zeros where figures go.
Mistaken for: `profile`, when there is an avatar and a name. `list`, when it is rows or cards with no chart, period
or headline figure (check-in rows, goal rows). `home`, when rings and balances sit among several kinds of block.

### `activity` Activity
For: hold the person on one task while it runs, with one clear control to move on or stop.
Tell it by: a lesson or quiz step, a timer, a game or a live session; a progress or live readout; one control in
the bottom third; a close X or back arrow; a full-bleed colour, dark or art background; a question and answers.
Mistaken for: `splash`, when a brand mark is shown at launch: no brand and a task message is `activity`. `other`, for
a pure waiting interstitial with no control and no progress, or a Live Activity banner. `detail`, for one reward's
page that launches the task elsewhere. `confirmation`, for an order already done with a rating card.

### `list` List
For: show a set of records one per row so the person can scan them, open one or add another.
Tell it by: a title; a thumbnail, icon or avatar at the left of each row; two-line rows (a name and a pale detail);
one thing at the right end (chevron, button, count); a way to add (plus, Create); section headings; an empty slot.
Mistaken for: `settings`, when the rows are plain chevrons with no switches or current values (it is `list`). `detail`,
for one item's page. `home`, `stats`, `account`, for a balance or figure with rows underneath: the rows are the
content when there is no identity, plan or chart. `menu`, when the rows are sections and actions, not records.

### `notifications` Notifications
For: tell the person what happened since they last looked and let them act on it.
Tell it by: a title; a time on each item; an avatar, icon or thumbnail at the left; an unread dot or tinted
row; a button or action on the item; headings that group by time; tabs; a gear or Manage in the header; an empty bell.
Mistaken for: `inbox`, which holds messages from people. `chat` or `feed`, for a running thread or posts.

## Managing

### `settings` Settings
For: let the person change how the app behaves, looks or notifies them, and see the current choice at a glance.
Tell it by: a back arrow or close X; rows with a chevron to a sub-page; on/off toggles at the right end; group
headings in small grey or capital type; a grey help sentence under a row; the current value at the right;
sliders, radio or check rows; a log-out row; a version number.
Mistaken for: `account`, which shows who is signed in, with details, plan, delete or log out. `filter`, which narrows a
list. `list`, for plain chevron rows with no toggles or values. `menu`, for a short list of sections to jump to.

### `account` Account
For: show who the person is signed in as and let them change their details, plan or membership, or leave.
Tell it by: name, email or phone; an avatar; a plan, membership or status line; editable fields; rows to other
pages; Delete account, Log out or Cancel subscription; Save at the top right.
Mistaken for: `paywall`, when the page offers a price to start paying; the current plan with Manage, Switch or Cancel is
`account`, as is a "Cancel your plan" page that lists lost benefits. `list`, for a balance with credit history or
card rows and no identity, plan or way to leave. `menu`, for a signed-out "You" tab that is only Log in and links.
`profile`, for the public page of a person.

### `help` Help
For: answer a question or fix a problem, or put the person in touch with someone who can.
Tell it by: a headline that names the topic or asks "How can we help?"; FAQ or topic rows; a way to reach a
person (chat, email, phone); paragraphs of plain text; legal text or links; numbered steps; a version number.
Mistaken for: `article`, for a story or a notice read for its own sake. `settings`, for a list of toggles with Help and
Terms rows. `menu`, for a More list of sections with a Help row among them.

### `menu` Menu
For: put the app's sections and actions in one short list so the person can jump to any of them.
Tell it by: a short list of labelled rows or buttons, usually each with a small icon; shown over another screen
(sheet, popover, slide-in drawer) or as the More tab; an identity header; an account, settings or help row; an
action sheet that ends in Log out or Cancel.
Mistaken for: `account`, when it shows the person's details and plan. `list`, when the rows are records (open tabs,
history, people with Add buttons) and not sections or actions.

## Paying

### `paywall` Paywall
For: show what paid access gives you and let you start paying, or start a trial, in one step.
Tell it by: a way out (X, back, Not Now); a price in currency; one filled main button; plan choices (monthly and
yearly, a Save badge); free-trial wording; a list of benefits; fine print on renewal; a Restore purchase link; the
App Store purchase sheet on top.
Mistaken for: `account`, for a page of the current plan with Manage, Switch or Cancel. `checkout`, when there is a cart
or several goods; a coin shop sits between the two. `other`, for a web page of membership terms with no price and
no way to start paying, or a modal that says more points are needed.

### `checkout` Checkout
For: let the person check what they are buying, choose how to pay, and commit with one clear button.
Tell it by: product lines with picture, quantity and price; a total; a payment method row or card fields; a
promo or gift-card entry; Apple Pay or PayPal buttons; an address or delivery row; a tip choice; one pay button.
Mistaken for: `paywall`, one subscription with no cart. `detail`, for a past order page ("View order", "View
receipt"). `form`, for an address or card step that only collects facts.

### `confirmation` Confirmation
For: tell the person that what they just did worked, and show what to do next.
Tell it by: a headline that says what happened ("Order placed", "Saved", "You're all set"); a check mark; one main
button; a line on what happens next; receipt rows; a rating prompt; sometimes a sheet or alert.
Mistaken for: `detail`, when nothing says an action just worked (a reservation page with a confirmation code and
no headline, a past order). `welcome`, when the headline is about what is next in an intro and not about what was
done.
