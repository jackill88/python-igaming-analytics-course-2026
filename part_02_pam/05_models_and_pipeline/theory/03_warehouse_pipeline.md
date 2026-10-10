# What the pipeline becomes

Chapter 1's pipeline was an RGS stream, then a warehouse, then dbt features, then batch models. The sources are now PAM schemas.

```
service MySQL  →  warehouse tables  →  dbt features  →  batch scores  →  predictions table
```

| Metric | Warehouse source |
|--------|------------------|
| Player identity | `customers` |
| Login activity | `login_sessions` |
| Historical GGR | `game_rounds` |
| Deposits | `transactions` |
| Bonus cost | `bonuses_claimed` |
| Bonus catalogue | `bonuses` (offerings) |
| Reconciliation | `bo_reports` aggregates, compared to your facts, not modelled as features |
| Realtime balance push | Not a warehouse source |

Replicate MySQL (CDC or a scheduled snapshot of the facts above). Do not subscribe the warehouse to Redis pub/sub. A missed balance event cannot be replayed, and the transaction row already has the money.

`service-bo-reports` remains the backoffice's own cron output. Match daily GGR and deposit totals against it. Do not rebuild those crons as the analytics platform, and do not train models on a pre-aggregated table when the round exists.

Batch scoring is still the right default for churn, segmentation, and NGR LTV. The product already pushes balance over a websocket; that does not mean the churn model must score inside the bet path. Real-time scoring waits until an in-session recommendation has a measured lift.

A feature store is still a later decision. dbt on the warehouse, plus a predictions table for Solitics, is the Chapter 2 architecture.

## Key takeaway

Change the source from "an RGS topic" to "PAM MySQL facts". Keep the rest of the Chapter 1 stack: warehouse, dbt, batch models, and a reason before any new infrastructure.
