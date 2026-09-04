"""
Challenge: Compute Stickiness
Module 02: Engagement Metrics

Theory: theory/02_stickiness.md

Inputs:
  activity — player_id, activity_date
  as_of — date for DAU numerator and MAU denominator

Outputs:
  float — DAU / MAU; 0.0 when MAU is 0

Edge cases:
  - Guard division by zero
  - Shared sample: stickiness on 2024-06-05 == 0.25 (DAU=1, MAU=4)

Example:
  >>> stickiness(activity, pd.Timestamp("2024-06-05"))
  0.25

Run: pytest tests/02_engagement_metrics/test_compute_stickiness.py -v
"""

import pandas as pd


def stickiness(activity: pd.DataFrame, as_of: pd.Timestamp) -> float:
    """Return DAU / MAU for as_of. Return 0.0 if MAU is 0."""
    pass
