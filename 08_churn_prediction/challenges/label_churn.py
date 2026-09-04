"""
Challenge: Label Churn Target
Module 08: Churn Prediction

Theory: theory/01_churn_definition.md

Inputs:
  activity — player_id, activity_date
  snapshot_date — label observation date
  horizon_days — forward inactivity window (default 30)

Outputs:
  player_id, inactive_next_30_days (1 = no future activity in horizon)

Edge cases:
  - Include players active in 30d before snapshot only
  - Future window: (snapshot_date, snapshot_date + horizon_days]

Example:
  >>> label_churn(activity, snapshot)["inactive_next_30_days"].tolist()

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
