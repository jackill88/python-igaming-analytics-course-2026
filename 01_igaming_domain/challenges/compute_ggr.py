"""
Challenge: Compute GGR
Module 01: iGaming Domain & RGS Events

Theory: theory/03_ggr_and_revenue_metrics.md

Inputs:
  df — DataFrame with bet_amount, win_amount columns

Outputs:
  compute_ggr — copy of df with ggr column (bet − win)
  total_ggr — scalar sum of GGR across all rows

Edge cases:
  - Preserve original columns; do not mutate input
  - Wins exceeding bets yield negative per-row GGR

Example:
  >>> total_ggr(rgs_events)  # shared sample total is -4.0

Run: pytest tests/01_igaming_domain/test_compute_ggr.py -v
"""

import pandas as pd


def compute_ggr(df: pd.DataFrame) -> pd.DataFrame:
    """Add column ggr = bet_amount - win_amount. Return copy with ggr column."""
    pass


def total_ggr(df: pd.DataFrame) -> float:
    """Return sum of GGR across all rows."""
    pass
