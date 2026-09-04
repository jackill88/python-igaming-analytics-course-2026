"""
Challenge: Player Favorite Game SQL
Module 05: SQL Analytics on Gaming Data

Theory: theory/02_top_games_and_affinity.md

Inputs:
  None — return SQL string only

Outputs:
  SQL: player_id, favorite_game (most rounds played; tie-break game_id ASC)

Edge cases:
  - Use window function or equivalent ranking
  - One favorite per player

Example:
  >>> result.query("player_id==101")["favorite_game"].iloc[0]
  'slots_a'

Run: pytest tests/05_sql_gaming_analytics/test_player_favorite_game_sql.py -v
"""


def player_favorite_game_sql() -> str:
    """
    Return SQL: player_id, favorite_game (most rounds played).
    Table: rounds(round_id, player_id, game_id, bet_amount, win_amount, timestamp)
    Tie-break by game_id ascending.
    """
    pass
