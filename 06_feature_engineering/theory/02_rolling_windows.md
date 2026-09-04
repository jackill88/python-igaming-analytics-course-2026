# Rolling Windows

Rolling features capture **recent behavior** for ML and segmentation.

## Common windows

| Window | Features |
|--------|----------|
| 7d | sessions_7d, ggr_7d, avg_bet_7d |
| 30d | sessions_30d, ggr_30d, avg_bet_30d |
| 90d | Longer-term value signals |

## Point-in-time rule

For feature_date = `2024-06-15`:

```
Include events where timestamp ∈ [2024-06-08 00:00, 2024-06-15 23:59:59]
```

Never include events **after** feature_date (label leakage).

## SQL rolling example

```sql
SELECT player_id, feature_date,
       COUNT(DISTINCT session_id) AS sessions_7d
FROM rounds
WHERE timestamp >= feature_date - INTERVAL 6 DAY
  AND timestamp < feature_date + INTERVAL 1 DAY
GROUP BY player_id, feature_date;
```

## Python

Use pandas `rolling` on daily aggregates, or filter-then-aggregate per snapshot date.

## Key takeaway

Rolling windows must use **consistent inclusive/exclusive bounds** across training and scoring.
