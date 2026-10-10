"""
Challenge: Convert To EUR
Module 01: What Changes with PAM

Theory: theory/03_keys_grain_currency.md

Inputs:
  amount — customer-currency amount
  currency — ISO code
  rates — DataFrame with columns currency, eur_per_unit

Outputs:
  amount * eur_per_unit for that currency

Edge cases:
  - Missing currency raises KeyError
  - Do not mutate rates

Example:
  >>> to_eur(100, "GBP", pam_fx_rates_frame())
  117.0

Run: pytest tests/part_02_pam/01_what_changes/test_convert_to_eur.py -v
"""

import pandas as pd


def to_eur(amount: float, currency: str, rates: pd.DataFrame) -> float:
    """Convert amount to EUR using the supplied rate card."""
    pass
