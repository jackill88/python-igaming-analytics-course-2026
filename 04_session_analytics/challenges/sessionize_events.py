"""
Challenge: Sessionize Events
Module 04: Session Analytics

Theory: theory/02_sessionization.md

Inputs:
  events — player_id, timestamp (and other RGS columns)
  gap_minutes — split threshold (default 30)

Outputs:
  events copy with derived_session_id — int starting at 1 per player

Edge cases:
  - Sort by player_id, timestamp before processing
  - Gap > threshold starts new session (exactly 30 min does NOT split)
  - Player 102 has 2 derived sessions in shared sample

Example:
  >>> out = sessionize_by_gap(events, gap_minutes=30)
  >>> out[out.player_id == 102]["derived_session_id"].nunique()
  2

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
