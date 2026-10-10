"""
Challenge: Paying Users
Module 03: Wallet Revenue

Theory: theory/01_deposits_and_ftd.md

Inputs:
  transactions — cid, tx_type, status

Outputs:
  Count of distinct cids with at least one approved deposit

Example:
  >>> paying_user_count(pam_transactions_frame())
  3

Run: pytest tests/part_02_pam/03_wallet_revenue/test_paying_users.py -v
"""

import pandas as pd


def paying_user_count(transactions: pd.DataFrame) -> int:
    """Distinct cids with an approved deposit."""
    pass
