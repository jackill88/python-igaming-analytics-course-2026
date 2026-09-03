"""
Challenge: Session Duration
Module 04: Session Analytics

Run: pytest tests/04_session_analytics/test_session_duration.py -v
"""

import pandas as pd


def session_durations(events: pd.DataFrame) -> pd.DataFrame:
    """
    Using session_id column. Return player_id, session_id, duration_minutes, round_count.
    duration = max(timestamp) - min(timestamp) in minutes.
    """
    pass
