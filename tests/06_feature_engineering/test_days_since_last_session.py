import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

days_since_last_session = load_challenge("06_feature_engineering", "days_since_last_session.py").days_since_last_session


def test_days_since():
    out = days_since_last_session(rgs_events_frame(), pd.Timestamp("2024-06-04"))
    assert "days_since_last_session" in out.columns
    assert (out["days_since_last_session"] >= 0).all()
