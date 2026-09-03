import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

label_future_ggr = load_challenge("09_ltv_proxy", "label_future_ggr.py").label_future_ggr


def test_future_ggr():
    out = label_future_ggr(rgs_events_frame(), pd.Timestamp("2024-06-01"), horizon_days=30)
    assert "future_ggr_30d" in out.columns
