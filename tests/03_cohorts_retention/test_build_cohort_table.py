import pandas as pd
from shared.datasets import daily_activity_frame, players_frame
from shared.testing import load_challenge

cohort_retention_table = load_challenge(
    "03_cohorts_retention", "build_cohort_table.py"
).cohort_retention_table


def test_cohort_table_columns():
    out = cohort_retention_table(players_frame(), daily_activity_frame(), [1, 7])
    assert list(out.columns) == ["d1", "d7"]
    assert len(out.index) >= 1


def test_cohort_table_d1_zero_for_may_cohort():
    out = cohort_retention_table(players_frame(), daily_activity_frame(), [1])
    cohort = pd.Timestamp("2024-04-29")
    if cohort in out.index:
        assert out.loc[cohort, "d1"] == 0.0


def test_cohort_table_retention_bounds():
    out = cohort_retention_table(players_frame(), daily_activity_frame(), [1, 7, 30])
    assert (out.values >= 0.0).all()
    assert (out.values <= 1.0).all()
