import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

daily_active_users = load_challenge("02_engagement_metrics", "compute_dau.py").daily_active_users


def test_dau():
    activity = daily_activity_frame()
    assert daily_active_users(activity, pd.Timestamp("2024-06-01")) == 2
    assert daily_active_users(activity, pd.Timestamp("2024-06-03")) == 2
