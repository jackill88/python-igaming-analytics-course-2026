"""
Challenge: Top Games per Player
Module 10: Recommendation Engine

Theory: theory/02_collaborative_filtering.md

Inputs:
  events — player_id, game_id
  n — top-N per player (default 3)

Outputs:
  player_id, rank, game_id sorted by round count desc; tie-break game_id asc

Edge cases:
  - rank starts at 1 per player
  - Fewer than n games → return available only

Example:
  >>> top_n_games_per_player(events, n=2).query("player_id==101 and rank==1")["game_id"].iloc[0]
  'slots_a'

Run: pytest tests/10_recommendations/test_top_games_per_player.py -v
"""

import pandas as pd


def top_n_games_per_player(events: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Return player_id, rank, game_id sorted by round count descending per player."""
    pass

