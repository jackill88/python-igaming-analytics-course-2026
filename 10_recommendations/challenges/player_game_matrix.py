"""
Challenge: Player-Game Matrix
Module 10: Recommendation Engine

Theory: theory/02_collaborative_filtering.md

Inputs:
  events — player_id, game_id (round-level)

Outputs:
  Pivot: rows=player_id, columns=game_id, values=round_count; fill NaN with 0

Edge cases:
  - Count every round row
  - Shared sample: shape (4 players, 3 games)

Example:
  >>> player_game_matrix(events).loc[101, "slots_a"]
  2

Run: pytest tests/10_recommendations/test_player_game_matrix.py -v
"""

import pandas as pd


def player_game_matrix(events: pd.DataFrame) -> pd.DataFrame:
    """
    Return pivot: rows=player_id, columns=game_id, values=round_count (number of rounds).
    Fill missing with 0.
    """
    pass
