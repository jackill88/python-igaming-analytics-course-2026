"""
Challenge: Pipeline Phase Order
Module 11: Analytics Architecture

Theory: theory/01_rgs_to_warehouse.md, theory/03_batch_vs_realtime_ml.md

Inputs:
  completed — list of phase names already finished

Outputs:
  Next recommended phase string, or None if all complete

Edge cases:
  - Ignore unknown completed phases
  - Order: warehouse → dbt_features → segmentation_churn_ltv → recommendations → feature_store_eval

Example:
  >>> next_phase([])
  'warehouse'

Run: pytest tests/11_analytics_architecture/test_pipeline_phase_order.py -v
"""

RECOMMENDED_PHASES = [
    "warehouse",
    "dbt_features",
    "segmentation_churn_ltv",
    "recommendations",
    "feature_store_eval",
]


def next_phase(completed: list[str]) -> str | None:
    """Return the next recommended phase not yet in completed, or None if all done."""
    pass
