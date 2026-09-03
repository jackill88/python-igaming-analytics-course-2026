import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

stickiness = load_challenge("02_engagement_metrics", "compute_stickiness.py").stickiness


def test_stickiness():
    activity = daily_activity_frame()
    ratio = stickiness(activity, pd.Timestamp("2024-06-05"))
    assert 0 < ratio <= 1.0
