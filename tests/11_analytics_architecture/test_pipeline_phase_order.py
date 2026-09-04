from shared.testing import load_challenge

next_phase = load_challenge(
    "11_analytics_architecture", "pipeline_phase_order.py"
).next_phase


def test_next_phase_first():
    assert next_phase([]) == "warehouse"


def test_next_phase_after_warehouse():
    assert next_phase(["warehouse"]) == "dbt_features"


def test_next_phase_complete():
    completed = [
        "warehouse",
        "dbt_features",
        "segmentation_churn_ltv",
        "recommendations",
        "feature_store_eval",
    ]
    assert next_phase(completed) is None


def test_next_phase_skips_unknown():
    assert next_phase(["warehouse", "unknown_phase"]) == "dbt_features"
