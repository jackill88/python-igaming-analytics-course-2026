"""
Challenge: Warehouse Source
Module 05: Models and the Pipeline

Theory: theory/03_warehouse_pipeline.md

Inputs:
  metric — name of a fact the warehouse might load

Outputs:
  Table family to replicate, or None when the metric must not be ingested

Mapping:
  player_identity -> customers
  login_activity -> login_sessions
  historical_ggr -> game_rounds
  deposits -> transactions
  bonus_cost -> bonuses_claimed
  bonus_catalogue -> bonuses
  reconciliation_check -> bo_reports
  realtime_balance_push -> None

Edge cases:
  - Unknown metric raises KeyError

Example:
  >>> warehouse_source("historical_ggr")
  'game_rounds'

Run: pytest tests/part_02_pam/05_models_and_pipeline/test_warehouse_source.py -v
"""


def warehouse_source(metric: str) -> str | None:
    """Return the PAM table family to replicate, or None if it is not a warehouse feed."""
    pass
