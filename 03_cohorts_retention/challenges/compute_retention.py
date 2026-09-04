"""
Challenge: Compute Retention
Module 03: Cohorts & Retention

Theory: theory/02_retention_metrics.md

Inputs:
  players — player_id, registration_date
  activity — player_id, activity_date

Outputs:
  float — fraction with activity exactly 7 days after registration_date

Edge cases:
  - Empty players → 0.0
  - Compare normalized calendar dates

Example:
  >>> d7_retention(players_frame(), daily_activity_frame())
  0.0

Run: pytest tests/03_cohorts_retention/test_compute_retention.py -v
"""

import pandas as pd


def d7_retention(players: pd.DataFrame, activity: pd.DataFrame) -> float:
    """
    Fraction of players who had activity exactly 7 days after registration_date.
    Return 0.0 if no players.
    """
    pass
