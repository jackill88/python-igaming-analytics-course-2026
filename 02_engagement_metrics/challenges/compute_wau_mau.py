"""
Challenge: Compute WAU and MAU
Module 02: Engagement Metrics

Theory: theory/01_dau_wau_mau.md

Inputs:
  activity — player_id, activity_date
  as_of — end of rolling window (inclusive)

Outputs:
  wau — unique players in [as_of − 6d, as_of]
  mau — unique players in [as_of − 29d, as_of]

Edge cases:
  - Inclusive bounds on both ends
  - Shared sample: wau(as_of=2024-06-05) == 4

Example:
  >>> wau(daily_activity, pd.Timestamp("2024-06-05"))
  4

Run: pytest tests/02_engagement_metrics/test_compute_wau_mau.py -v
"""

import pandas as pd


def wau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """Unique players active in [as_of - 6 days, as_of] inclusive."""
    pass


def mau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """Unique players active in [as_of - 29 days, as_of] inclusive."""
    pass
