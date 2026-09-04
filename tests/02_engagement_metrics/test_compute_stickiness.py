import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

stickiness = load_challenge("02_engagement_metrics", "compute_stickiness.py").stickiness


def test_stickiness_shared_sample():
    activity = daily_activity_frame()
    assert stickiness(activity, pd.Timestamp("2024-06-05")) == 0.25


def test_stickiness_zero_mau():
    activity = pd.DataFrame(
        {"player_id": [1], "activity_date": pd.to_datetime(["2023-01-01"])}
    )
    assert stickiness(activity, pd.Timestamp("2024-06-01")) == 0.0


def test_stickiness_perfect_daily():
    activity = pd.DataFrame(
        {
            "player_id": [1] * 30,
            "activity_date": pd.date_range("2024-06-01", periods=30),
        }
    )
    assert stickiness(activity, pd.Timestamp("2024-06-30")) == 1.0
