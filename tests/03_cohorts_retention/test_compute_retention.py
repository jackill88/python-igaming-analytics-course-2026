import pandas as pd
from shared.datasets import daily_activity_frame, players_frame
from shared.testing import load_challenge

d7_retention = load_challenge("03_cohorts_retention", "compute_retention.py").d7_retention


def test_d7_retention_shared_sample():
    assert d7_retention(players_frame(), daily_activity_frame()) == 0.0


def test_d7_retention_perfect_cohort():
    players = pd.DataFrame(
        {"player_id": [1, 2], "registration_date": pd.to_datetime(["2024-06-01", "2024-06-01"])}
    )
    activity = pd.DataFrame(
        {"player_id": [1, 2], "activity_date": pd.to_datetime(["2024-06-08", "2024-06-08"])}
    )
    assert d7_retention(players, activity) == 1.0


def test_d7_retention_empty_players():
    empty = pd.DataFrame(columns=["player_id", "registration_date"])
    activity = daily_activity_frame()
    assert d7_retention(empty, activity) == 0.0
