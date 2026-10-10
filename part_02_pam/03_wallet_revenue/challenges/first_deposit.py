"""
Challenge: First Deposit
Module 03: Wallet Revenue

Theory: theory/01_deposits_and_ftd.md

Inputs:
  transactions — transaction_id, cid, tx_type, status, amount_eur, created_at

Outputs:
  cid, first_deposit_at, amount_eur
  One row per cid that has an approved deposit, sorted by cid

Rules:
  - tx_type == "deposit" and status == "approved"
  - Earliest created_at; tie-break on smaller transaction_id
  - amount_eur is the amount on that winning row
  - No approved deposits -> empty frame with those columns

Example:
  >>> first_deposit(pam_transactions_frame()).set_index("cid").loc[101, "amount_eur"]
  117.0

Run: pytest tests/part_02_pam/03_wallet_revenue/test_first_deposit.py -v
"""

import pandas as pd


def first_deposit(transactions: pd.DataFrame) -> pd.DataFrame:
    """Earliest approved deposit per cid."""
    pass
