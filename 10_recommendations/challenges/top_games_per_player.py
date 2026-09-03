"""
Challenge: Top Games per Player
Module 10: Recommendation Engine

Run: pytest tests/10_recommendations/test_top_games_per_player.py -v
"""

import pandas as pd


def top_n_games_per_player(events: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Return player_id, rank, game_id sorted by round count descending per player."""
    pass
