"""
Challenge: GGR per Session
Module 04: Session Analytics

Theory: theory/03_session_metrics.md

Inputs:
  events — player_id, session_id, bet_amount, win_amount

Outputs:
  player_id, session_id, total_bets, total_wins, ggr

Edge cases:
  - Aggregate all rounds within session
  - Player 101 s1 → ggr=20.0 in shared sample

Example:
  >>> ggr_per_session(events).query("player_id==101")["ggr"].iloc[0]
  20.0

Run: pytest tests/04_session_analytics/test_ggr_per_session.py -v
"""

import pandas as pd


def ggr_per_session(events: pd.DataFrame) -> pd.DataFrame:
    """Return player_id, session_id, total_bets, total_wins, ggr."""
    pass
