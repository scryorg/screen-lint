# This type: Account (`account`)

Also called: profile, my account, personal details, account settings, membership, manage plan, You tab
What it is for: Show the person who they are signed in as and let them change their details, plan or membership, or leave.

The type was picked from the picture, so it can be wrong. Looking closely, if the screen does not do the job above, it is another type: set `is_type` false and put the best key from `references/types.md` (or `other`) in `instead`. `lint.py` then grades nothing and exits 3, and you go back to the classifier with that type.

## Parts (keys 1 to 10 in `parts`)

The notes name apps the page was written from. They explain what counts as the part; they do not tell you what is on your screen.

| k | part | what counts |
|---|---|---|
| 1 | Back arrow, Close or X at the top | Missing on Skyscanner, WeTransfer and On; Skyscanner and On are top-level tab pages and WeTransfer is a sheet. |
| 2 | Name, email, phone or other personal details on show | Tesla Robotaxi, Peloton Strength, Vivid and 5 more. |
| 3 | Delete account, log out or cancel subscription control | At the bottom of the list on Co–Star, Ada and WeTransfer; red icon or text on Ada and WeTransfer. MoonPay, informed News and untitled show the confirm step. |
| 4 | Plan, membership or status line | Plan and renewal date on Co–Star, plan and next payment on Revolut, Member since on untitled and On, a rewards status on SKIMS, Manage subscription on WeTransfer. |
| 5 | Rows with a chevron or link arrow to other pages | Tesla Robotaxi, Vivid, Coinbase Wallet and 3 more. |
| 6 | Bottom tab bar | Vivid, Skyscanner, Coinbase Wallet and 3 more. |
| 7 | Editable input fields | Text boxes on MoonPay, Peloton Strength, informed News and 2 more; a country dropdown on Hinge. |
| 8 | Avatar or profile photo | A photo or initials: Co–Star, Skyscanner, Coinbase Wallet and 2 more. |
| 9 | Save at the top right | Peloton Strength, Rent the Runway and Vinted. All three are editing pages. |
| 10 | Grey help text on how a detail is used | Tesla Robotaxi (phone used for sign-in), Peloton Strength (private details not shown), Vinted (phone used to log in). |

## Variants (`v1` to `v4` in `variants`)

- `v1` Account hub: A top-level page with a photo or card, then rows or tiles that open details, orders, plan and support.
- `v2` Edit personal details: Fields for name, contact, birthday or photo, with Save or Done.
- `v3` Plan and membership: Current plan, next payment or tier status, with a switch-plan or cancel option.
- `v4` Delete, secure or export: Sign-in security, a data download request, or the delete-account step with its warning.

## Pitfalls (keys "1" to "3" in `pitfalls`)

Mark one `seen` only when the screen clearly shows it.

1. The same job has many titles: Account, Account settings, Profile, Personal Information, Personal Details.
2. A profile page lists a dozen fields in one scroll, most marked Optional or Select.
3. In the delete sheet the red Delete Account option is the first one listed, above Manage membership and Cancel.

## What the checked screens of each subtype have (the linter expects the same)

50 checked screens of this type; screens per subtype (a screen can be more than one): v1 17, v2 13, v3 7, v4 16.

- `v1` Account hub
  - A photo or initials near the top
  - Name, email or phone in the top third
  - Rows or tiles that open other pages
  - A plan or status line
- `v2` Edit personal details
  - A back arrow or close at the top
  - The name, email or phone shown
  - Editable fields for the details
- `v3` Plan and membership
  - A back arrow or close at the top
  - A plan, membership or status line, mostly in the top third
- `v4` Delete, secure or export
  - A back arrow or close at the top
  - A delete, log out or cancel control
  - No tab bar under the page

The linter judges the parts and pitfalls above, and the contrast, size and position of what you mark. It does not judge taste.
