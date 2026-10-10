"""
Challenge: Bonus Cost
Module 04: Bonuses and NGR

Theory: theory/01_bonus_three_owners.md

Inputs:
  claims — cid, bonus_cost_eur

Outputs:
  cid, bonus_cost_eur summed across claims, sorted by cid
  Empty input -> empty frame with those columns

Example:
  >>> bonus_cost_per_player(pam_bonus_claims_frame()).set_index("cid").loc[102, "bonus_cost_eur"]
  20.0

Run: pytest tests/part_02_pam/04_bonus_and_ngr/test_bonus_cost.py -v
"""

import pandas as pd


def bonus_cost_per_player(claims: pd.DataFrame) -> pd.DataFrame:
    """Sum bonus cost in EUR per cid."""
    pass
