"""
Challenge: Label Churn Target
Module 08: Churn Prediction

Run: pytest tests/08_churn_prediction/test_label_churn.py -v
"""

import pandas as pd


def label_churn(activity: pd.DataFrame, snapshot_date: pd.Timestamp, horizon_days: int = 30) -> pd.DataFrame:
    """
    For each player active in 30d before snapshot_date, label inactive_next_30_days:
    1 if no activity in (snapshot_date, snapshot_date + horizon_days], else 0.
    Return player_id, inactive_next_30_days.
    """
    pass
