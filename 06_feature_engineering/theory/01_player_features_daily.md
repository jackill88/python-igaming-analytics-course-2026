# player_features_daily

The central feature table for iGaming ML. One row per `(player_id, feature_date)`.

## Recommended columns

```
player_id
feature_date
days_since_last_session
sessions_7d
sessions_30d
avg_bet_7d
avg_bet_30d
ggr_7d
ggr_30d
favorite_game_7d
rounds_7d
```

## Build pattern (dbt-style)

1. Start from `rounds` fact table
2. Filter events with `timestamp < feature_date` (no leakage)
3. Aggregate rolling 7d / 30d windows ending `feature_date - 1 day` or end-of-day policy
4. Join dimension attributes (country, registration_date)

## Why daily grain?

- Batch scoring nightly for CRM
- Aligns with churn labels (inactive next 30 days)
- Easy to audit point-in-time correctness

## Storage

Partition by `feature_date`. Retain 90–365 days depending on model needs.

## Key takeaway

`player_features_daily` is the **contract between analytics and ML** — version and document every column.
