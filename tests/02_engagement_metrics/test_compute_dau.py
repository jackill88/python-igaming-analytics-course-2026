import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

daily_active_users = load_challenge("02_engagement_metrics", "compute_dau.py").daily_active_users


def test_dau_on_active_day():
    activity = daily_activity_frame()
    assert daily_active_users(activity, pd.Timestamp("2024-06-01")) == 2


def test_dau_counts_unique_players():
    activity = daily_activity_frame()
    assert daily_active_users(activity, pd.Timestamp("2024-06-05")) == 1


def test_dau_no_activity():
    activity = daily_activity_frame()
    assert daily_active_users(activity, pd.Timestamp("2024-06-04")) == 0
