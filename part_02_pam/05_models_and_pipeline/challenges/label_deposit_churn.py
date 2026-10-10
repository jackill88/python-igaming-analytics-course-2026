"""
Challenge: Label Deposit Churn
Module 05: Models and the Pipeline

Theory: theory/01_pam_features_and_labels.md

Inputs:
  transactions — cid, tx_type, status, created_at
  snapshot_date — label date
  horizon_days — forward window (default 30)

Outputs:
  cid, no_deposit_next_30_days
  Sorted by cid

Rules:
  - Population: cids with an approved deposit on the 30 calendar days
    ending on snapshot_date, inclusive
  - Label 1 when that cid has no approved deposit in
    (snapshot_date, snapshot_date + horizon_days]
  - Label 0 otherwise
  - Empty population -> empty frame with those columns

Example:
  >>> label_deposit_churn(transactions, pd.Timestamp("2024-06-01"))

Run: pytest tests/part_02_pam/05_models_and_pipeline/test_label_deposit_churn.py -v
"""

import pandas as pd


def label_deposit_churn(
    transactions: pd.DataFrame,
    snapshot_date: pd.Timestamp,
    horizon_days: int = 30,
) -> pd.DataFrame:
    """Label players who deposited recently and not again inside the horizon."""
    pass
