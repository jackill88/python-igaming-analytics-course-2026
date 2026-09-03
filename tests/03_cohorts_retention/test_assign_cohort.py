from shared.datasets import players_frame
from shared.testing import load_challenge

assign_registration_cohort = load_challenge("03_cohorts_retention", "assign_cohort.py").assign_registration_cohort


def test_cohort_week():
    out = assign_registration_cohort(players_frame())
    assert "cohort_week" in out.columns
    assert out.loc[out.player_id == 101, "cohort_week"].iloc[0].dayofweek == 0
