"""
Challenge: CRM Eligible Players
Module 02: Activity and Cohorts

Theory: theory/03_crm_eligibility.md

Inputs:
  customers — cid, status, marketing_email_allowed

Outputs:
  DataFrame with column cid, sorted ascending

Rules:
  - status must be "active"
  - marketing_email_allowed must be 1
  - Do not mutate customers

Example:
  >>> crm_eligible_players(pam_customers_frame())["cid"].tolist()
  [101, 102, 104]

Run: pytest tests/part_02_pam/02_activity_and_cohorts/test_crm_eligible_players.py -v
"""

import pandas as pd


def crm_eligible_players(customers: pd.DataFrame) -> pd.DataFrame:
    """Return cids that may be contacted."""
    pass
