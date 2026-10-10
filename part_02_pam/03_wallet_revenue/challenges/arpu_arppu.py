"""
Challenge: ARPU and ARPPU
Module 03: Wallet Revenue

Theory: theory/02_arpu_arppu.md

Inputs:
  revenue — cid, revenue_eur (already the revenue definition you chose)
  active_cids — ids in the activity population
  transactions — used only to count paying users (approved deposits)

Outputs:
  (arpu, arppu)
  ARPU = sum(revenue_eur) / unique active ids
  ARPPU = sum(revenue_eur) / paying users
  Either denominator of 0 yields 0.0 for that ratio

Example:
  >>> arpu, arppu = arpu_arppu(revenue, [101, 102, 103, 104], transactions)

Run: pytest tests/part_02_pam/03_wallet_revenue/test_arpu_arppu.py -v
"""

import pandas as pd


def arpu_arppu(
    revenue: pd.DataFrame,
    active_cids: list[int],
    transactions: pd.DataFrame,
) -> tuple[float, float]:
    """Return ARPU and ARPPU for an explicit revenue column."""
    pass
