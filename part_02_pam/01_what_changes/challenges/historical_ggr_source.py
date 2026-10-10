"""
Challenge: Historical GGR Source
Module 01: What Changes with PAM

Theory: theory/03_keys_grain_currency.md

Inputs:
  table_name — candidate fact table

Outputs:
  True when the table can back a historical GGR fact, else False

True for:
  game_rounds, transactions

False for:
  customer_balance, and every other name

Example:
  >>> is_historical_ggr_source("customer_balance")
  False

Run: pytest tests/part_02_pam/01_what_changes/test_historical_ggr_source.py -v
"""


def is_historical_ggr_source(table_name: str) -> bool:
    """Return True only for tables that record historical stakes and wins."""
    pass
