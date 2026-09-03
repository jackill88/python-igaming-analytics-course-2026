"""
Challenge: LTV Feature Matrix
Module 09: LTV & Value Proxy

Run: pytest tests/09_ltv_proxy/test_ltv_feature_matrix.py -v
"""

import pandas as pd


def ltv_features(events: pd.DataFrame, snapshot_date: pd.Timestamp) -> pd.DataFrame:
    """Return player_id, ggr_30d, sessions_30d, avg_bet_30d for players active before snapshot."""
    pass
