"""
Challenge: Train LTV Model
Module 09: LTV & Value Proxy

Theory: theory/03_proxy_limitations.md

Inputs:
  features — numeric columns (+ optional player_id)
  targets — future_ggr_30d Series
  random_state — default 42

Outputs:
  Fitted LightGBM regressor

Edge cases:
  - Drop player_id before training
  - Must expose .predict for regression

Example:
  >>> model = train_ltv_regressor(features, targets)
  >>> len(model.predict(features.drop(columns=["player_id"])))

Run: pytest tests/09_ltv_proxy/test_train_ltv_model.py -v
"""

import pandas as pd
import lightgbm as lgb


def train_ltv_regressor(features: pd.DataFrame, targets: pd.Series, random_state: int = 42):
    """Train LightGBM regressor. Return fitted model."""
    pass
