"""
Challenge: Sessionize Events
Module 04: Session Analytics

Run: pytest tests/04_session_analytics/test_sessionize_events.py -v
"""

import pandas as pd


def sessionize_by_gap(events: pd.DataFrame, gap_minutes: int = 30) -> pd.DataFrame:
    """
    Assign derived_session_id per player when gap > gap_minutes.
    Return events copy with derived_session_id (int, starting at 1 per player).
    Sort by player_id, timestamp before processing.
    """
    pass
