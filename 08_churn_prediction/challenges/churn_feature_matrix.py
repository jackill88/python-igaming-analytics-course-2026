"""
Challenge: Churn Feature Matrix
Module 08: Churn Prediction

Theory: theory/02_churn_features.md

Inputs:
  events — RGS events with timestamp, session_id, bet/win amounts
  snapshot_date — feature cutoff (inclusive for history)

Outputs:
  player_id, days_since_last_session, sessions_30d, avg_bet_30d, ggr_30d

Edge cases:
  - History window: 30 days ending snapshot_date
  - Only players with activity in that window

Example:
  >>> build_churn_features(events, pd.Timestamp("2024-06-03"))

Run: pytest tests/08_churn_prediction/test_churn_feature_matrix.py -v
"""

import pandas as pd


def build_churn_features(events: pd.DataFrame, snapshot_date: pd.Timestamp) -> pd.DataFrame:
    """
    Return player_id, days_since_last_session, sessions_30d, avg_bet_30d, ggr_30d
    for players with any activity in 30d before snapshot_date.
    """
    pass
