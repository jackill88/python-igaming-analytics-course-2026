import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

sessions_7d = load_challenge("06_feature_engineering", "sessions_in_window.py").sessions_7d


def test_sessions_7d():
    out = sessions_7d(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert "sessions_7d" in out.columns
