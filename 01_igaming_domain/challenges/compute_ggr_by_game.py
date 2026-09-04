"""
Challenge: Compute GGR by Game
Module 01: iGaming Domain & RGS Events

Theory: theory/03_ggr_and_revenue_metrics.md

Inputs:
  df — RGS events with game_id, bet_amount, win_amount

Outputs:
  DataFrame: game_id, total_bets, total_wins, ggr — sorted by ggr descending

Edge cases:
  - Multiple games; roulette_b is top game in shared sample (ggr=60.0)
  - Empty input → empty result with correct columns

Example:
  >>> ggr_by_game(events).iloc[0]["game_id"]
  'roulette_b'

Run: pytest tests/01_igaming_domain/test_compute_ggr_by_game.py -v
"""

import pandas as pd


def ggr_by_game(df: pd.DataFrame) -> pd.DataFrame:
    """Return DataFrame with columns game_id, total_bets, total_wins, ggr sorted by ggr desc."""
    pass
