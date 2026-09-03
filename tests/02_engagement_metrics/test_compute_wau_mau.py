import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

mod = load_challenge("02_engagement_metrics", "compute_wau_mau.py")
wau = mod.wau
mau = mod.mau


def test_wau():
    activity = daily_activity_frame()
    assert wau(activity, pd.Timestamp("2024-06-05")) == 4


def test_mau():
    activity = daily_activity_frame()
    assert mau(activity, pd.Timestamp("2024-06-05")) == 4
