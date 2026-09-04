"""
Challenge: Build Player Features
Module 06: Feature Engineering

Theory: theory/03_feature_grain_and_leakage.md

Inputs:
  events — full RGS events
  feature_date — end of 7-day feature window (inclusive)

Outputs:
  player_id, sessions_7d, avg_bet_7d, ggr_7d, favorite_game_7d

Edge cases:
  - Only players with activity in window
  - favorite_game = game with most rounds; tie-break game_id ascending

Example:
  >>> feats = build_player_features(events, pd.Timestamp("2024-06-03"))
  >>> set(feats.columns) >= {"sessions_7d", "ggr_7d", "favorite_game_7d"}

Run: pytest tests/06_feature_engineering/test_build_player_features.py -v
"""

import pandas as pd


def build_player_features(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    """
    Return player_id, sessions_7d, avg_bet_7d, ggr_7d, favorite_game_7d
    for players with activity in the 7-day window ending feature_date.
    favorite_game = game with most rounds in window.
    """
    pass
