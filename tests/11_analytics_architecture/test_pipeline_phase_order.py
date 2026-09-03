from shared.testing import load_challenge

next_phase = load_challenge("11_analytics_architecture", "pipeline_phase_order.py").next_phase


def test_next_phase():
    assert next_phase([]) == "warehouse"
    assert next_phase(["warehouse"]) == "dbt_features"
    assert next_phase(["warehouse", "dbt_features", "segmentation_churn_ltv", "recommendations", "feature_store_eval"]) is None
