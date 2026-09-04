# Churn Definition

In iGaming with RGS data, churn is typically **inactivity**, not account closure.

## Standard definition

```
Churned = no gameplay activity for 30 consecutive days
```

## ML label

```
inactive_next_30_days = 1 if no activity in (snapshot_date, snapshot_date + 30 days]
```

Players must be **active in the lookback window** before snapshot to be eligible (existing players, not brand-new).

## Alternative definitions

| Definition | When to use |
|------------|-------------|
| 14-day inactive | Fast-cycle mobile products |
| 60-day inactive | Low-frequency lottery-style |
| Deposit churn | Needs PAM — no deposit in 30d |

## Class imbalance

Churn datasets are often imbalanced (many non-churners). Use:

- `scale_pos_weight` in LightGBM
- Precision@K for top decile
- Calibration for CRM capacity planning

## Key takeaway

Align churn definition with **CRM action window** — if campaigns react at 14 days idle, don't train on 30-day labels.
