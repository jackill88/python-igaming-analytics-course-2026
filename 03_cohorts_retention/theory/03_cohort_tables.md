# Cohort Tables

A cohort retention table is a matrix:

```
              d1    d7    d14   d30
cohort_week
2024-05-01   45%   22%   18%   12%
2024-05-08   48%   25%   20%   ...
```

Rows = cohorts, columns = days since anchor, values = retention rate.

## Building the table

1. Assign each player to a cohort (registration week)
2. For each `(cohort, day_offset)`, count players active on `cohort_date + offset`
3. Divide by cohort size

## Reading the table

- **Horizontal (across columns):** decay curve for one cohort
- **Vertical (down rows):** whether newer cohorts retain better at D7
- **Diagonal:** calendar-time effects (seasonality, campaigns)

## Visualization

Heatmaps highlight improving (darker later cohorts) vs declining retention.

## Warehouse design

Materialize as `mart_cohort_retention(cohort_week, day_offset, retained_players, cohort_size, retention_rate)`.

Refresh nightly from `player_daily_activity`.

## Key takeaway

Cohort tables are the standard product analytics artifact for **onboarding and engagement quality** over time.
