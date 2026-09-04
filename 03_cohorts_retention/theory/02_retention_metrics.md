# Retention Metrics

Retention measures whether players **return after a reference day**.

| Metric | Definition |
|--------|------------|
| **D1** | Active 1 day after registration (or cohort anchor) |
| **D7** | Active 7 days after registration |
| **D30** | Active 30 days after registration |

```
D7 retention = players active on day 7 / cohort size
```

## Return vs survival

- **Return-based (common):** active exactly on day N (or within a window around N)
- **Survival / rolling:** active at any point in days 1–N

State which you use — they produce different numbers.

## SQL sketch

```sql
SELECT
    cohort_week,
    COUNT(DISTINCT player_id) AS cohort_size,
    COUNT(DISTINCT CASE WHEN days_since_reg = 7 THEN player_id END) AS d7_retained
FROM player_cohort_activity
GROUP BY cohort_week;
```

## iGaming benchmarks

Benchmarks vary by market, product, and channel. Use **internal baselines** and **cohort-over-cohort trends** rather than generic industry numbers.

## Key takeaway

Retention is **cohort size in the denominator** and a **precise day/window definition** in the numerator.
