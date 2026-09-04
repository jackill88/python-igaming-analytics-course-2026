"""
Challenge: Assign Cohort
Module 03: Cohorts & Retention

Theory: theory/01_cohort_basics.md

Inputs:
  players — player_id, registration_date

Outputs:
  Copy with cohort_week — Monday-start week of registration_date

Edge cases:
  - Wednesday registration maps to preceding Monday
  - Preserve all original columns

Example:
  >>> assign_registration_cohort(players).loc[players.player_id==101, "cohort_week"].iloc[0]
  Timestamp('2024-04-29')

Run: pytest tests/03_cohorts_retention/test_assign_cohort.py -v
"""

import pandas as pd


def assign_registration_cohort(players: pd.DataFrame) -> pd.DataFrame:
    """Add cohort_week column (Monday-start week of registration_date). Return copy."""
    pass
