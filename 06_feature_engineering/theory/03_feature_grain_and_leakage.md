# Feature Grain and Leakage

**Leakage** = using information from the future to predict the past. It inflates offline metrics and fails in production.

## Common leakage mistakes in iGaming

| Mistake | Fix |
|---------|-----|
| Include same-day rounds when scoring at midnight | Cutoff timestamp policy |
| Use lifetime GGR as a feature | Use GGR only before feature_date |
| Label churn using activity before snapshot | Label uses activity *after* snapshot only |
| Train/test split by random rows | Split by time or player cohort |

## Train / serve skew

Features computed in notebooks differently from dbt SQL → silent production bugs.

**Mitigation:** single source of truth in warehouse; notebooks read the feature table.

## Feature_date semantics

Document:

- Timezone of `feature_date`
- Whether window ends at start-of-day or end-of-day
- Handling of players with zero history (null vs 0)

## Key takeaway

For every feature, ask: **"Would I know this value at scoring time?"** If not, it's leakage.
