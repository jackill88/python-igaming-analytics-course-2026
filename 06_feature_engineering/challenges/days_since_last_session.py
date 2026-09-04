"""
Challenge: Days Since Last Session
Module 06: Feature Engineering

Theory: theory/01_player_features_daily.md

Inputs:
  events — player_id, timestamp
  feature_date — snapshot (exclude events >= feature_date)

Outputs:
  player_id, days_since_last_session

Edge cases:
  - Players with no activity before feature_date are omitted
  - Integer day difference via .days

Example:
  >>> days_since_last_session(events, pd.Timestamp("2024-06-04")).query("player_id==101")
  days_since_last_session == 3

Run: pytest tests/06_feature_engineering/test_days_since_last_session.py -v
"""

import pandas as pd


def days_since_last_session(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    """
    Return player_id, days_since_last_session for each player active before feature_date.
    If never active, omit player. Days = (feature_date - last_timestamp).days
    """
    pass
