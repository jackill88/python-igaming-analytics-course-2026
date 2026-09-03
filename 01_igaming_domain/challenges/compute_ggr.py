"""
Challenge: Compute GGR
Module 01: iGaming Domain & RGS Events

Run: pytest tests/01_igaming_domain/test_compute_ggr.py -v
"""

import pandas as pd


def compute_ggr(df: pd.DataFrame) -> pd.DataFrame:
    """Add column ggr = bet_amount - win_amount. Return copy with ggr column."""
    pass


def total_ggr(df: pd.DataFrame) -> float:
    """Return sum of GGR across all rows."""
    pass
