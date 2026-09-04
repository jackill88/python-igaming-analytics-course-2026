"""
Challenge: Train Churn Model
Module 08: Churn Prediction

Theory: theory/03_model_training_and_eval.md

Inputs:
  features — includes player_id + numeric features
  labels — binary inactive_next_30_days
  random_state — default 42

Outputs:
  Fitted LightGBM classifier (drop player_id before fit)

Edge cases:
  - Model must expose .predict and .predict_proba
  - Small synthetic data should fit without error

Example:
  >>> model = train_churn_classifier(features, labels)
  >>> model.predict(features.drop(columns=["player_id"]))

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
