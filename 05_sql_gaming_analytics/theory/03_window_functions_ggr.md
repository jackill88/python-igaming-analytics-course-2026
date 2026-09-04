# Window Functions for GGR

Window functions compute **rolling** and **running** metrics without collapsing rows.

## Rolling 7-day GGR

```sql
SELECT
    activity_date,
    ggr,
    SUM(ggr) OVER (
        ORDER BY activity_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7d_ggr
FROM daily_ggr
ORDER BY activity_date;
```

## Running total by player

```sql
SELECT
    player_id,
    timestamp,
    SUM(bet_amount - win_amount) OVER (
        PARTITION BY player_id
        ORDER BY timestamp
    ) AS cumulative_ggr
FROM rounds;
```

## Lag for session gaps

```sql
LAG(timestamp) OVER (PARTITION BY player_id ORDER BY timestamp) AS prev_ts
```

## Frame clauses

| Frame | Meaning |
|-------|---------|
| `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` | Last 7 days including today |
| `RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW` | Calendar-aware (engine-dependent) |

## Key takeaway

Windows preserve row grain — use them for **trends and running totals**, `GROUP BY` for **snapshots**.
