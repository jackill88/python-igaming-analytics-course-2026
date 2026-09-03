import pandas as pd
from shared.datasets import daily_activity_frame, players_frame
from shared.testing import load_challenge

d7_retention = load_challenge("03_cohorts_retention", "compute_retention.py").d7_retention


def test_d7_retention():
    players = players_frame()
    activity = daily_activity_frame()
    rate = d7_retention(players, activity)
    assert 0.0 <= rate <= 1.0
