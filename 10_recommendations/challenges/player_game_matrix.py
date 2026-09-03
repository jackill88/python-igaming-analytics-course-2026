"""
Challenge: Player-Game Matrix
Module 10: Recommendation Engine

Run: pytest tests/10_recommendations/test_player_game_matrix.py -v
"""

import pandas as pd


def player_game_matrix(events: pd.DataFrame) -> pd.DataFrame:
    """
    Return pivot: rows=player_id, columns=game_id, values=round_count (number of rounds).
    Fill missing with 0.
    """
    pass
