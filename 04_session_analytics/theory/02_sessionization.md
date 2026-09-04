# Sessionization

Sessionization assigns a **session key** to each event using inactivity gaps.

## Algorithm

1. Sort events by `player_id`, `timestamp`
2. Compute gap from previous event (same player)
3. Increment session counter when gap > threshold
4. Assign `derived_session_id`

## SQL approach (window functions)

```sql
SELECT
    *,
    SUM(CASE WHEN gap_minutes > 30 OR gap_minutes IS NULL THEN 1 ELSE 0 END)
        OVER (PARTITION BY player_id ORDER BY timestamp) AS derived_session_id
FROM with_gaps;
```

Where `with_gaps` uses `LAG(timestamp)` to compute gap.

## Python approach

See Module 04 challenge `sessionize_by_gap`.

## Choosing the gap threshold

| Threshold | Effect |
|-----------|--------|
| 15 min | More sessions, shorter duration |
| 30 min | Common default |
| 60 min | Fewer, longer sessions |

Run sensitivity analysis before locking a threshold.

## Key takeaway

Sessionization is a **gaps-and-islands** problem — define timeout and partition key before coding.
