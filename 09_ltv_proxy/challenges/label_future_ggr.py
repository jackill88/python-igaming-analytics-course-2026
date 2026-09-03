"""
Challenge: Label Future GGR
Module 09: LTV & Value Proxy

Run: pytest tests/09_ltv_proxy/test_label_future_ggr.py -v
"""

import pandas as pd


def label_future_ggr(events: pd.DataFrame, snapshot_date: pd.Timestamp, horizon_days: int = 30) -> pd.DataFrame:
    """
    For players active before snapshot_date, sum GGR in (snapshot_date, snapshot_date + horizon_days].
    Return player_id, future_ggr_30d.
    """
    pass
