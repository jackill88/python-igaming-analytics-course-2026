"""
Challenge: PAM Player Features
Module 05: Models and the Pipeline

Theory: theory/01_pam_features_and_labels.md

Inputs:
  customers — cid, status, marketing_email_allowed
  transactions — cid, tx_type, status, created_at
  rounds — cid, cash_bet_eur, bonus_bet_eur, win_amount_eur, event_ts
  feature_date — snapshot date; rows after this calendar day are invisible

Outputs:
  One row per customer, in customer-file order:
  cid, days_since_ftd, deposits_30d, bonus_ggr_share, crm_eligible

Rules:
  - days_since_ftd: days from the earliest approved deposit on or before
    feature_date. pandas NA when there is none
  - deposits_30d: count of approved deposits on the 30 calendar days
    ending on feature_date, inclusive ([feature_date - 29 days, feature_date])
  - bonus_ggr_share: module 04 share using rounds on or before feature_date;
    0 when the player has no stake in that window
  - crm_eligible: 1 if status == "active" and marketing_email_allowed == 1 else 0

Example:
  >>> pam_player_features(customers, transactions, rounds, pd.Timestamp("2024-06-01"))

Run: pytest tests/part_02_pam/05_models_and_pipeline/test_pam_player_features.py -v
"""

import pandas as pd


def pam_player_features(
    customers: pd.DataFrame,
    transactions: pd.DataFrame,
    rounds: pd.DataFrame,
    feature_date: pd.Timestamp,
) -> pd.DataFrame:
    """Point-in-time PAM columns for every customer."""
    pass
