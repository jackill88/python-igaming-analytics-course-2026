# Cohort Basics

A **cohort** groups players by a shared start event — usually **registration date** or **first bet date**.

```
Cohort = players who registered in the same week/month
```

## Why cohorts?

Aggregate retention hides whether **newer players behave differently** from older ones. Cohort analysis answers:

- Is D7 retention improving release over release?
- Did a product change help May registrants vs April?

## Assigning cohorts

```python
import pandas as pd

reg = pd.to_datetime(players["registration_date"])
cohort_week = reg - pd.to_timedelta(reg.dt.dayofweek, unit="D")  # Monday start
```

## Cohort types in iGaming

| Cohort anchor | Use case |
|---------------|----------|
| Registration date | Marketing / onboarding quality |
| First deposit date | Monetization (needs PAM) |
| First bet date | Gameplay engagement (RGS) |

## Key takeaway

Pick the cohort anchor that matches the **question** — registration for acquisition quality, first bet for gameplay retention.
