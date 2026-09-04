# Future GGR Prediction

Regression model: features at snapshot → sum of GGR in next N days.

## Label

```python
future_ggr_30d = sum(bet_amount - win_amount) for rounds in (snapshot, snapshot + 30d]
```

## Features

Same as churn: `ggr_30d`, `sessions_30d`, `avg_bet_30d`, tenure, favorite game.

## Model

```python
import lightgbm as lgb

model = lgb.LGBMRegressor(random_state=42)
model.fit(X_train, y_train)
```

## Evaluation

- MAE / RMSE on holdout
- Spearman correlation (ranking quality)
- Decile lift: top decile actual GGR vs bottom

## Use cases

- Prioritize VIP outreach
- Budget allocation by expected value
- Early whale detection

## Key takeaway

LTV proxy models are **ranking tools** — validate that top decile players actually generate more GGR.
