# Model Training and Evaluation

## Model choice

**LightGBM** or **XGBoost** — handle mixed features, nonlinear patterns, fast training on tabular data.

```python
import lightgbm as lgb

model = lgb.LGBMClassifier(random_state=42)
model.fit(X_train, y_train)
```

## Validation strategy

- **Time-based split:** train on older snapshots, test on recent
- Never random-split rows from the same player across train/test

## Metrics

| Metric | Use |
|--------|-----|
| AUC-ROC | Overall ranking quality |
| Precision@K | Top-K list for CRM calls |
| Recall@K | Coverage of actual churners |
| Calibration | Expected vs actual churn rate in bucket |

## Deployment workflow

```
RGS → warehouse → player_features_daily → nightly score → churn_scores table → CRM
```

Batch is sufficient for most win-back campaigns.

## Key takeaway

Optimize for **CRM capacity** (precision at top decile), not only AUC.
