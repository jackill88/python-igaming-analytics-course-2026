"""
Challenge: Compute WAU and MAU
Module 02: Engagement Metrics

Run: pytest tests/02_engagement_metrics/test_compute_wau_mau.py -v
"""

import pandas as pd


def wau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """Unique players active in [as_of - 6 days, as_of] inclusive."""
    pass


def mau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """Unique players active in [as_of - 29 days, as_of] inclusive."""
    pass
