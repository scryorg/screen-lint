# This type: Player (`player`)

Also called: now playing, media player, video player, audio player, live room, full-screen player
What it is for: Play one video, track or live stream and give the few controls needed to steer it.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 9 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Title or name of what is playing | Rebel Girls, Clubhouse, Vevo and 10 more. Equinox is rotated sideways. |
| 2 | Large video, artwork or photo | Video on Vevo, Equinox, Apple TV and 4 more. Artwork or photo on Rebel Girls, Pillow, Not Boring Vibes and 2 more. |
| 3 | Icons for share, like, queue, cast or more | Rebel Girls, Clubhouse, Vevo and 8 more. |
| 4 | Scrub bar or waveform | Rebel Girls, Vevo, Patreon and 6 more. Patreon uses a waveform. |
| 5 | Play or pause button | Centered on Rebel Girls, Equinox, Calm and Particle News. In a corner on Vevo, Patreon, IGTV and Neuecast. |
| 6 | Time readout (elapsed and remaining) | Rebel Girls, Patreon, Equinox and 5 more. |
| 7 | Down arrow at the top left to minimize | Rebel Girls, Clubhouse, Vevo and 4 more. Patreon has Cancel and Shazam has an X at the top instead. |
| 8 | Skip or jump-15-seconds buttons | Rebel Girls, Calm and Particle News. All three are audio screens. |
| 9 | Live badge or audience count | ON AIR with a listener count on Stationhead, LIVE with a viewer count on Periscope. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Full-screen video: The video fills the width or the whole screen, and controls are light or hidden.
- `v2` Audio with artwork and controls: Artwork or a waveform, the title, a scrub bar with times, and play, skip and share controls.
- `v3` Live room or broadcast: A room, radio show or camera feed with a live badge or people on stage and actions such as chat, tip or follow.
- `v4` Calm and sleep sessions: A quiet scene or portrait with a title and length, and very little else on the screen.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. No title or controls are visible while the media plays, so it is hard to tell how to pause or leave.
2. A card or sheet sits on top of the player: the Close card covers most of the artwork on Rebel Girls, and the Options sheet covers the lower half of the video on Powder.
3. Small, low-contrast caption text on a dark picture is hard to read.

## What the checked screens of each subtype have (the linter expects the same)

52 checked screens of this type; screens per subtype (a screen can be more than one): v1 28, v2 15, v3 5, v4 3.

- `v1` Full-screen video
  - The video fills the width of the screen, mostly in the middle
  - A title printed with the video
  - A scrub bar to show progress
- `v2` Audio with artwork
  - Large artwork and a title in the upper two thirds of the screen
  - A scrub bar with a time readout
  - A play or pause button toward the bottom
  - Icons for share, like or queue
- `v3` Live room or broadcast
- `v4` Calm and sleep sessions

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
