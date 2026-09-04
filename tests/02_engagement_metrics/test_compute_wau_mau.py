import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

mod = load_challenge("02_engagement_metrics", "compute_wau_mau.py")
wau = mod.wau
mau = mod.mau


def test_wau_shared_sample():
    activity = daily_activity_frame()
    assert wau(activity, pd.Timestamp("2024-06-05")) == 4


def test_mau_shared_sample():
    activity = daily_activity_frame()
    assert mau(activity, pd.Timestamp("2024-06-05")) == 4


def test_wau_single_day_window():
    activity = pd.DataFrame(
        {"player_id": [1, 1, 2], "activity_date": pd.to_datetime(["2024-06-01"] * 3)}
    )
    assert wau(activity, pd.Timestamp("2024-06-01")) == 2
