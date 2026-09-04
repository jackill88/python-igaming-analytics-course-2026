"""
Challenge: Build Cohort Table
Module 03: Cohorts & Retention

Theory: theory/03_cohort_tables.md

Inputs:
  players — player_id, registration_date
  activity — player_id, activity_date
  days — list of offsets (e.g. [1, 7, 30])

Outputs:
  DataFrame indexed by cohort_week, columns d{day} with retention rates 0–1

Edge cases:
  - Cohort size denominator is players in that registration week
  - Empty cohort → 0.0 rates

Example:
  >>> table = cohort_retention_table(players, activity, [1, 7])
  >>> "d7" in table.columns

Run: pytest tests/03_cohorts_retention/test_build_cohort_table.py -v
"""

import pandas as pd


def cohort_retention_table(
    players: pd.DataFrame, activity: pd.DataFrame, days: list[int]
) -> pd.DataFrame:
    """
    Return DataFrame: cohort_week x day_offset with retention rate (0-1).
    Index: cohort_week, columns: d{day} for each day in days.
    """
    pass
