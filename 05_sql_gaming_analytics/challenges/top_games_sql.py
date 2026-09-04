"""
Challenge: Top Games SQL
Module 05: SQL Analytics on Gaming Data

Theory: theory/02_top_games_and_affinity.md

Inputs:
  None — return SQL string only

Outputs:
  SQL returning game_id, ggr for top 3 games by total GGR

Edge cases:
  - Table: rounds(round_id, player_id, game_id, bet_amount, win_amount, timestamp)
  - Order by ggr DESC; LIMIT 3

Example:
  >>> query_duckdb(top_games_by_ggr_sql(), {"rounds": events})
  first row: roulette_b, ggr=60.0

Run: pytest tests/05_sql_gaming_analytics/test_top_games_sql.py -v
"""


def top_games_by_ggr_sql() -> str:
    """
    Return SQL for top 3 games by total GGR.
    Table: rounds(round_id, player_id, game_id, bet_amount, win_amount, timestamp)
    Columns: game_id, ggr
    """
    pass
