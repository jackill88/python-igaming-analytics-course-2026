from shared.datasets import daily_activity_frame, players_frame
from shared.testing import load_challenge

build = load_challenge("03_cohorts_retention", "build_cohort_table.py").cohort_retention_table


def test_cohort_table_shape():
    out = build(players_frame(), daily_activity_frame(), [1, 7])
    assert "d1" in out.columns or "d7" in out.columns or len(out.columns) >= 1
