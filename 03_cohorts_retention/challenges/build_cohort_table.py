"""
Challenge: Build Cohort Table
Module 03: Cohorts & Retention

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
