"""
Challenge: Anchor Retention
Module 02: Activity and Cohorts

Theory: theory/02_cohort_anchors.md

Inputs:
  customers — cid, registered_at
  rounds — cid, event_ts (play)
  transactions — cid, tx_type, status, created_at
  anchor — "registration" or "ftd"
  offset_days — calendar-day offset from the anchor date

Outputs:
  retained unique cids / cohort size

Rules:
  - registration anchor date is registered_at; every customer is in the cohort
  - ftd anchor date is the earliest approved deposit; customers with none are excluded
  - retained: any round on the calendar day anchor_date + offset_days
  - empty cohort returns 0.0
  - any other anchor raises ValueError

Example:
  >>> anchor_retention(customers, rounds, transactions, "registration", 1)
  0.4

Run: pytest tests/part_02_pam/02_activity_and_cohorts/test_anchor_retention.py -v
"""

import pandas as pd


def anchor_retention(
    customers: pd.DataFrame,
    rounds: pd.DataFrame,
    transactions: pd.DataFrame,
    anchor: str,
    offset_days: int,
) -> float:
    """Play-retention rate at offset_days for a registration or FTD cohort."""
    pass
