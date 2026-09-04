import pandas as pd
from shared.datasets import players_frame
from shared.testing import load_challenge

assign_registration_cohort = load_challenge(
    "03_cohorts_retention", "assign_cohort.py"
).assign_registration_cohort


def test_cohort_week_monday_start():
    out = assign_registration_cohort(players_frame())
    assert pd.Timestamp(out.loc[out.player_id == 101, "cohort_week"].iloc[0]) == pd.Timestamp(
        "2024-04-29"
    )
    assert pd.Timestamp(out.loc[out.player_id == 104, "cohort_week"].iloc[0]) == pd.Timestamp(
        "2024-05-27"
    )


def test_assign_cohort_preserves_columns():
    players = players_frame()
    out = assign_registration_cohort(players)
    assert "cohort_week" in out.columns
    assert set(players.columns).issubset(out.columns)
    assert len(out) == len(players)
