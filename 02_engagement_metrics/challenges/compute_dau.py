"""
Challenge: Compute DAU
Module 02: Engagement Metrics

Theory: theory/01_dau_wau_mau.md

Inputs:
  activity — player_id, activity_date
  as_of — snapshot timestamp (compare normalized calendar date)

Outputs:
  int — count of unique player_id active on as_of date

Edge cases:
  - Multiple rows per player on same day count once
  - No activity on date → 0

Example:
  >>> daily_active_users(activity, pd.Timestamp("2024-06-01"))
  2

Run: pytest tests/02_engagement_metrics/test_compute_dau.py -v
"""

import pandas as pd


def daily_active_users(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """
    Count unique player_id with activity_date == as_of.date().
    activity columns: player_id, activity_date
    """
    pass
