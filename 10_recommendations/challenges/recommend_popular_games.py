"""
Challenge: Recommend Popular Games
Module 10: Recommendation Engine

Theory: theory/03_offline_evaluation.md

Inputs:
  events — all player rounds
  player_id — target player
  n — number of recommendations

Outputs:
  list[str] — top globally popular games (by round count) not yet played by player

Edge cases:
  - Tie-break by game_id ascending
  - Player 101 → blackjack_c is top unplayed in shared sample

Example:
  >>> recommend_popular_unplayed(events, player_id=101, n=1)
  ['blackjack_c']

Run: pytest tests/10_recommendations/test_recommend_popular_games.py -v
"""

import pandas as pd


def recommend_popular_unplayed(events: pd.DataFrame, player_id: int, n: int = 3) -> list[str]:
    """
    Return top n globally popular games (by round count) the player has NOT played.
    Tie-break by game_id ascending.
    """
    pass
