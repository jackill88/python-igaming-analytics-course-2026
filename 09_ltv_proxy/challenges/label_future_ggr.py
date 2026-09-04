"""
Challenge: Label Future GGR
Module 09: LTV & Value Proxy

Theory: theory/02_future_ggr_prediction.md

Inputs:
  events — RGS events
  snapshot_date — start of label window (exclusive for past)
  horizon_days — forward window length (default 30)

Outputs:
  player_id, future_ggr_30d — sum of GGR in forward window

Edge cases:
  - Label period: (snapshot_date, snapshot_date + horizon_days]
  - Players with no future rounds omitted from result

Example:
  >>> label_future_ggr(events, pd.Timestamp("2024-06-01"))["future_ggr_30d"].sum()

Run: pytest tests/09_ltv_proxy/test_label_future_ggr.py -v
"""

import pandas as pd


def label_future_ggr(events: pd.DataFrame, snapshot_date: pd.Timestamp, horizon_days: int = 30) -> pd.DataFrame:
    """
    For players active before snapshot_date, sum GGR in (snapshot_date, snapshot_date + horizon_days].
    Return player_id, future_ggr_30d.
    """
    pass
