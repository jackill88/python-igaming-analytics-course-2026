"""
Challenge: Activity Counts
Module 02: Activity and Cohorts

Theory: theory/01_three_activity_definitions.md

Inputs:
  logins — cid, login_at
  rounds — cid, event_ts
  transactions — cid, tx_type, status, created_at
  as_of — calendar day to measure

Outputs:
  dict with keys login, play, deposit: unique cid counts on that day

Rules:
  - Compare normalized calendar dates
  - deposit: tx_type == "deposit" and status == "approved" only

Example:
  >>> activity_counts(logins, rounds, transactions, "2024-06-01")
  {'login': 2, 'play': 1, 'deposit': 1}

Run: pytest tests/part_02_pam/02_activity_and_cohorts/test_activity_counts.py -v
"""

import pandas as pd


def activity_counts(
    logins: pd.DataFrame,
    rounds: pd.DataFrame,
    transactions: pd.DataFrame,
    as_of: pd.Timestamp,
) -> dict[str, int]:
    """Count unique cids for login, play, and approved deposit on as_of."""
    pass
