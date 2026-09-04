"""
Challenge: LTV Feature Matrix
Module 09: LTV & Value Proxy

Theory: theory/01_ltv_definitions.md

Inputs:
  events — RGS events
  snapshot_date — feature cutoff (inclusive)

Outputs:
  player_id, ggr_30d, sessions_30d, avg_bet_30d for players active before snapshot

Edge cases:
  - 30-day lookback ending at snapshot_date
  - Point-in-time: no future events in features

Example:
  >>> ltv_features(events, pd.Timestamp("2024-06-03"))

Run: pytest tests/09_ltv_proxy/test_ltv_feature_matrix.py -v
"""

import pandas as pd


def ltv_features(events: pd.DataFrame, snapshot_date: pd.Timestamp) -> pd.DataFrame:
    """Return player_id, ggr_30d, sessions_30d, avg_bet_30d for players active before snapshot."""
    pass
