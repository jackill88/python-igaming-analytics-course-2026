"""
Challenge: Train LTV Model
Module 09: LTV & Value Proxy

Run: pytest tests/09_ltv_proxy/test_train_ltv_model.py -v
"""

import pandas as pd
import lightgbm as lgb


def train_ltv_regressor(features: pd.DataFrame, targets: pd.Series, random_state: int = 42):
    """Train LightGBM regressor. Return fitted model."""
    pass
