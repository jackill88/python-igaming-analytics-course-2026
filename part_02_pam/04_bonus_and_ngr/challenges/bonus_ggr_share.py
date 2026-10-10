"""
Challenge: Bonus GGR Share
Module 04: Bonuses and NGR

Theory: theory/03_bonus_ggr_share.md

Inputs:
  rounds — cid, cash_bet_eur, bonus_bet_eur, win_amount_eur

Outputs:
  cid, ggr_eur, bonus_ggr_eur, bonus_ggr_share
  Sorted by cid

Rules:
  Sum stake, bonus stake, and GGR per cid first
  share = bonus stake / total stake, or 0 when total stake is 0
  bonus_ggr_eur = ggr_eur * share

Example:
  >>> bonus_ggr_share(pam_game_rounds_frame()).set_index("cid").loc[103, "bonus_ggr_share"]
  1.0

Run: pytest tests/part_02_pam/04_bonus_and_ngr/test_bonus_ggr_share.py -v
"""

import pandas as pd


def bonus_ggr_share(rounds: pd.DataFrame) -> pd.DataFrame:
    """Stake-weighted bonus portion of GGR per cid."""
    pass
