# DAU, WAU, MAU

Active-user metrics answer: **how many unique players were engaged in a period?**

| Metric | Window | Formula |
|--------|--------|---------|
| **DAU** | 1 day | Unique `player_id` active on date D |
| **WAU** | 7 days | Unique players active in [D−6, D] |
| **MAU** | 30 days | Unique players active in [D−29, D] |

## What counts as "active"?

In iGaming with RGS-only data, common definitions:

- **Played at least one round** (strongest gameplay signal)
- **Had a session** (may include lobby time)
- **Logged in** (requires PAM — not available in this course)

Pick one definition and use it consistently across dashboards.

## SQL pattern (daily activity table)

```sql
SELECT activity_date, COUNT(DISTINCT player_id) AS dau
FROM player_daily_activity
WHERE activity_date = '2024-06-01'
GROUP BY activity_date;
```

## Python pattern

```python
import pandas as pd

def dau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    day = as_of.normalize()
    mask = pd.to_datetime(activity["activity_date"]).dt.normalize() == day
    return activity.loc[mask, "player_id"].nunique()
```

## Key takeaway

Always state **active definition**, **timezone**, and **inclusive window bounds** when reporting DAU/WAU/MAU.
