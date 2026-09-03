"""
Challenge: Train Churn Model
Module 08: Churn Prediction

Run: pytest tests/08_churn_prediction/test_train_churn_model.py -v
"""

import pandas as pd
import lightgbm as lgb


def train_churn_classifier(
    features: pd.DataFrame,
    labels: pd.Series,
    random_state: int = 42,
):
    """Train LightGBM binary classifier on features (drop player_id). Return fitted model."""
    pass
