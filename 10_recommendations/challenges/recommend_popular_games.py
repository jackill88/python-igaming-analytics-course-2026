"""
Challenge: Recommend Popular Games
Module 10: Recommendation Engine

Run: pytest tests/10_recommendations/test_recommend_popular_games.py -v
"""

import pandas as pd


def recommend_popular_unplayed(events: pd.DataFrame, player_id: int, n: int = 3) -> list[str]:
    """
    Return top n globally popular games (by round count) the player has NOT played.
    Tie-break by game_id ascending.
    """
    pass
