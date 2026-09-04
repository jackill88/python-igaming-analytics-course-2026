import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

label_future_ggr = load_challenge("09_ltv_proxy", "label_future_ggr.py").label_future_ggr


def test_future_ggr_player_101():
    out = label_future_ggr(rgs_events_frame(), pd.Timestamp("2024-06-01"), horizon_days=30)
    row = out[out.player_id == 101].iloc[0]
    assert row["future_ggr_30d"] == 20.0


def test_future_ggr_columns():
    out = label_future_ggr(rgs_events_frame(), pd.Timestamp("2024-06-01"))
    assert list(out.columns) == ["player_id", "future_ggr_30d"]


def test_future_ggr_empty_horizon():
    out = label_future_ggr(rgs_events_frame(), pd.Timestamp("2024-12-01"), horizon_days=7)
    assert len(out) == 0
