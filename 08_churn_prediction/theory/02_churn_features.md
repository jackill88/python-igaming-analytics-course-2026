# Churn Features

Strong churn models use **recency, frequency, and monetary proxies** from RGS.

## Core features

| Feature | Signal |
|---------|--------|
| `days_since_last_session` | Recency — top predictor |
| `sessions_7d`, `sessions_30d` | Frequency trend |
| `avg_bet_30d` | Engagement depth |
| `ggr_30d` | Value (can be negative) |
| `favorite_game` | Habit / product stickiness |

## Derived features

- `sessions_7d / sessions_30d` — recent slowdown
- `ggr_7d - ggr_prev_7d` — momentum
- Days since registration — lifecycle stage

## Feature snapshot

All features computed at `snapshot_date` using only prior data.

Join labels from activity **after** snapshot.

## Missing history

New players with <7 days tenure — exclude or use separate model.

## Key takeaway

Churn features are mostly **RFM variants on gameplay** — keep them in `player_features_daily` for reuse.
