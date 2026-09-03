"""
Challenge: Pipeline Phase Order
Module 11: Analytics Architecture

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
