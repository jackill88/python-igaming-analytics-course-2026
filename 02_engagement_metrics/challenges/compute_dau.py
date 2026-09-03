"""
Challenge: Compute DAU
Module 02: Engagement Metrics

Run: pytest tests/02_engagement_metrics/test_compute_dau.py -v
"""

import pandas as pd


def daily_active_users(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """
    Count unique player_id with activity_date == as_of.date().
    activity columns: player_id, activity_date
    """
    pass
