"""
Challenge: Sessions in Window
Module 06: Feature Engineering

Theory: theory/02_rolling_windows.md

Inputs:
  events — player_id, session_id, timestamp
  feature_date — end of 7-day window (inclusive)

Outputs:
  player_id, sessions_7d — distinct session count in window

Edge cases:
  - Window [feature_date − 6d, feature_date] inclusive
  - Player with no events in window omitted

Example:
  >>> sessions_7d(events, pd.Timestamp("2024-06-03")).query("player_id==103")["sessions_7d"].iloc[0]
  1

Run: pytest tests/06_feature_engineering/test_sessions_in_window.py -v
"""

import pandas as pd


def sessions_7d(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    """Return player_id, sessions_7d counting distinct session_id in last 7 days ending feature_date."""
    pass
