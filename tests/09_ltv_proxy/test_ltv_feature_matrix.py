import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ltv_features = load_challenge("09_ltv_proxy", "ltv_feature_matrix.py").ltv_features


def test_ltv_features():
    out = ltv_features(rgs_events_frame(), pd.Timestamp("2024-06-05"))
    assert "ggr_30d" in out.columns
