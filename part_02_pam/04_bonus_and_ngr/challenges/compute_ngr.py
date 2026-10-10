"""
Challenge: Compute NGR
Module 04: Bonuses and NGR

Theory: theory/02_ngr.md

Inputs:
  rounds — cid, cash_bet_eur, bonus_bet_eur, win_amount_eur
  claims — cid, bonus_cost_eur
  provider_fee_rate — fraction of total stake
  tax_rate — fraction of GGR

Outputs:
  cid, ggr_eur, bonus_cost_eur, provider_fee_eur, tax_eur, ngr_eur
  One row per cid that appears in rounds or claims, sorted by cid

Rules:
  stake = cash_bet_eur + bonus_bet_eur
  ggr = stake - win_amount_eur
  provider_fee = provider_fee_rate * stake
  tax = tax_rate * ggr
  ngr = ggr - bonus_cost - provider_fee - tax
  Missing side of the outer join is 0

Example:
  >>> compute_ngr(rounds, claims, 0.10, 0.20).set_index("cid").loc[101, "ngr_eur"]
  7.8

Run: pytest tests/part_02_pam/04_bonus_and_ngr/test_compute_ngr.py -v
"""

import pandas as pd


def compute_ngr(
    rounds: pd.DataFrame,
    claims: pd.DataFrame,
    provider_fee_rate: float,
    tax_rate: float,
) -> pd.DataFrame:
    """NGR by cid from GGR, bonus cost, fee, and tax."""
    pass
