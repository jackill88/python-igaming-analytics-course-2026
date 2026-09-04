import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

days_since_last_session = load_challenge(
    "06_feature_engineering", "days_since_last_session.py"
).days_since_last_session


def test_days_since_player_101():
    out = days_since_last_session(rgs_events_frame(), pd.Timestamp("2024-06-04"))
    assert out.loc[out.player_id == 101, "days_since_last_session"].iloc[0] == 3


def test_days_since_excludes_feature_date_events():
    out = days_since_last_session(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert 104 not in set(out["player_id"])


def test_days_since_columns():
    out = days_since_last_session(rgs_events_frame(), pd.Timestamp("2024-06-05"))
    assert list(out.columns) == ["player_id", "days_since_last_session"]
    assert (out["days_since_last_session"] >= 0).all()
