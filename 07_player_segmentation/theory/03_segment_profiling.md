# Segment Profiling

After clustering, profile each segment to make it actionable.

## Profile table

| Segment | Count | avg_ggr_30d | avg_sessions_30d | top_game |
|---------|-------|-------------|------------------|----------|
| 0 | 12k | 450 | 25 | slots_a |
| 1 | 80k | 5 | 2 | roulette_b |

Compute **mean/median** of each feature per cluster.

## Naming segments

Compare centroids to global averages:

- Segment mean GGR >> global → "Whales"
- High days_since_last_session → "Dormant / churn-risk"

## Stability checks

- Re-cluster monthly — do segment sizes drift wildly?
- Track segment migration (player moves whale → casual)

## Export to CRM

```
player_segments(player_id, segment_id, segment_name, scored_at)
```

Refresh nightly or weekly.

## Key takeaway

A segment without a **profile and recommended action** is just an integer label.
