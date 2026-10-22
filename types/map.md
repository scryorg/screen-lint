# This type: Map (`map`)

Also called: map view, store locator, nearby, location picker, live map
What it is for: Show where things are, so the person can pick a place or point on the map and act on it.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Map fills the width and most of the height | The 4 that frame the map above a form or list are Kakao T, Lyft, SKIMS and GoodRx. |
| 2 | Pins or icons on the map | Price or number inside the pin on ParkWhiz, OpenTable and Hopper. Scooter or bike icons on Lime and ofo. |
| 3 | Card, sheet or panel docked at the bottom | A place or person card on Booking.com, OpenTable, Slowly and InPost UK, departures on Transit, a confirm panel on Bolt, a time scrubber on The Weather Channel, a list of places on GoodRx. |
| 4 | Floating button or pill over the map | Back or close on Booking.com, OpenTable, Uber Eats and Bolt, zoom on SKIMS, 'Search this area' and Filters on Hopper. |
| 5 | Time, date, wait or opening hours shown | A time range on ParkWhiz, time slots on OpenTable, a clock on Sunlitt, minutes on Transit, 'Arriving in 2 days' on Slowly, a time and duration on Kakao T, opening hours on GoodRx and InPost UK, a time scrubber on The Weather Channel. |
| 6 | Locate or recenter arrow | ParkWhiz, Lime, Transit and 5 more. |
| 7 | Search field or place field at the top | A search field on Corner, Wikipedia and Uber Eats, a search icon on Placify, an address field on SKIMS, a place and dates header on Hopper. |
| 8 | Bottom tab bar | ParkWhiz, Wikipedia, SKIMS and 3 more. |
| 9 | Button in the panel or floating at the bottom | Group ride and Scan on Lime, DONE on Postmates, UNLOCK on ofo, 'Confirm destination' on Bolt, 'Get directions' on InPost UK, 'Enable location' on Wikipedia. |
| 10 | Chips or filter pills over the map | Category chips on Corner, Uber One and Offers chips on Uber Eats, 'All Regions', 'All Cities' and 'All Categories' filters on Placify, a Filters pill on Hopper, a layer legend and toggles on The Weather Channel. |

## Variants (`v1` to `v4` in `variants`)

- `v1` Pins, often with a place card: Pins mark places, and a card at the bottom describes the selected one, as on OpenTable and InPost UK. ParkWhiz and Hopper put prices in the pins and show no card.
- `v2` One map, one main action: A pin marks a spot and one button confirms it, as on Postmates and Bolt. ofo shows nearby bikes and a single UNLOCK button.
- `v3` Map as a data layer: The map shows weather, sun, dots or places as data, with a time or layer control, as on Sunlitt and The Weather Channel.
- `v4` Small map above a form or list: A framed map sits above fields or a list that set the location or list the places, as on Lyft and GoodRx.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. Pins crowd and overlap their labels in dense areas.
2. A permission dialog sits over the map and hides it until the person acts.
3. On the dark maps the street labels are small and dim, and the purple dots on Check sit among them.

## What the checked screens of each subtype have (the linter expects the same)

60 checked screens of this type; screens per subtype (a screen can be more than one): v1 31, v2 12, v3 6, v4 9.

- `v1` Pins and place card
  - Pins or icons mark places on the map, from a few to a crowd
  - A card or sheet for the selected place is docked at the bottom on most screens
  - Floating buttons or pills sit over the map, mostly in the top third
  - A locate arrow floats on the map on most screens
- `v2` Map with one action
  - A button for the one action sits at the bottom, in a panel or floating
  - A pin or icons on the map, mostly in the upper part
  - Floating buttons at the top of the map, such as back or close
  - No tab bar and no search field: the map and one button carry the screen
- `v3` Map as data layer
- `v4` Small map above list
  - The map is a frame that takes about a third of the height, in the upper part
  - Fields or a list below the map fill most of the rest of the screen
  - Pins or a marker sit on the small map on most screens

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
