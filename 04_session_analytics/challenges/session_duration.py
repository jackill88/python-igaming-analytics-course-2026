"""
Challenge: Session Duration
Module 04: Session Analytics

Theory: theory/03_session_metrics.md

Inputs:
  events — player_id, session_id, timestamp, round_id

Outputs:
  player_id, session_id, duration_minutes, round_count

Edge cases:
  - Single-event session → duration 0.0
  - Player 101 session s1 → 35.0 minutes, 3 rounds in shared sample

Example:
  >>> session_durations(events).query("player_id==101 and session_id=='s1'")
  duration_minutes=35.0, round_count=3

Run: pytest tests/04_session_analytics/test_session_duration.py -v
"""

import pandas as pd


def session_durations(events: pd.DataFrame) -> pd.DataFrame:
    """
    Using session_id column. Return player_id, session_id, duration_minutes, round_count.
    duration = max(timestamp) - min(timestamp) in minutes.
    """
    pass
