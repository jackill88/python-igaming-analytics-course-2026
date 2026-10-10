# Cohort anchors

Chapter 1 retention usually starts from registration, or from the first observed round when registration is missing. PAM stores both dates, plus a third.

| Anchor | Source | Typical use |
|--------|--------|-------------|
| Registration | `customers.registered_at` | Product acquisition, including players who never pay |
| First play | earliest `game_rounds.event_ts` | Gameplay retention, the Chapter 1 cohort |
| First deposit (FTD) | earliest **approved** deposit `created_at` | Monetization cohorts |

A player can register on 1 May, deposit on 2 May, and play on 3 May. Day-1 retention is a different set of people for each anchor.

Definition used in this module: a player is retained at offset *d* if any play round falls on the calendar day `anchor_date + d`. Players with no date for that anchor are **out of the cohort**, not counted as churned. Registration cohorts include every customer. FTD cohorts include only customers with an approved deposit.

On the shared sample, registration day-1 play retention is 2/5 (cid 101 and 103). FTD day-1 play retention is 1/3 (only cid 101 plays on the day after the first approved deposit). Same rounds, different story.

## Key takeaway

Publish the anchor next to the rate. "D1 = 40%" is not comparable to "FTD D1 = 33%" without that label.
