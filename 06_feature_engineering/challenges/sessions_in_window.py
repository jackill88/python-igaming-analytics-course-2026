"""
Challenge: Sessions in Window
Module 06: Feature Engineering

Run: pytest tests/06_feature_engineering/test_sessions_in_window.py -v
"""

import pandas as pd


def sessions_7d(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    """Return player_id, sessions_7d counting distinct session_id in last 7 days ending feature_date."""
    pass
