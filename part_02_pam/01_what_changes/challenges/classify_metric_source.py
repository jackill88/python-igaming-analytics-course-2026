"""
Challenge: Classify Metric Source
Module 01: What Changes with PAM

Theory: theory/02_service_to_fact_map.md

Inputs:
  metric — short name of an analytical fact

Outputs:
  Owning service name, or "unknown"

Known metrics:
  login_dau, kyc_status -> service-customers
  deposits, bonus_claims -> service-wallet
  game_rounds, free_spins -> service-casino
  bonus_definitions -> service-offerings
  messages_sent -> service-communications
  daily_gaming_activity -> service-bo-reports

Edge cases:
  - Any other string returns "unknown"
  - Do not raise

Example:
  >>> classify_metric_source("game_rounds")
  'service-casino'

Run: pytest tests/part_02_pam/01_what_changes/test_classify_metric_source.py -v
"""


def classify_metric_source(metric: str) -> str:
    """Return the PAM service that owns this metric, or 'unknown'."""
    pass
