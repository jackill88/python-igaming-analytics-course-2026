"""
Challenge: Days Since Last Session
Module 06: Feature Engineering

Run: pytest tests/06_feature_engineering/test_days_since_last_session.py -v
"""

import pandas as pd


def days_since_last_session(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    """
    Return player_id, days_since_last_session for each player active before feature_date.
    If never active, omit player. Days = (feature_date - last_timestamp).days
    """
    pass
