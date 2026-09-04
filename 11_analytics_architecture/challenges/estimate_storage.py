"""
Challenge: Estimate Storage
Module 11: Analytics Architecture

Theory: theory/04_cost_and_feasibility.md

Inputs:
  events_per_day — daily round/event volume
  bytes_per_event — average row size (default 256)

Outputs:
  float — estimated GB per day (1 GB = 1e9 bytes)

Edge cases:
  - Linear scaling with volume
  - 10_000_000 × 256 / 1e9 == 2.56

Example:
  >>> estimate_daily_storage_gb(10_000_000)
  2.56

Run: pytest tests/11_analytics_architecture/test_estimate_storage.py -v
"""


def estimate_daily_storage_gb(
    events_per_day: int,
    bytes_per_event: int = 256,
) -> float:
    """Return estimated GB per day (use 1 GB = 1e9 bytes)."""
    pass
