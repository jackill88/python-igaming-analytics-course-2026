import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

build_churn_features = load_challenge("08_churn_prediction", "churn_feature_matrix.py").build_churn_features


def test_churn_features():
    out = build_churn_features(rgs_events_frame(), pd.Timestamp("2024-06-05"))
    assert "sessions_30d" in out.columns
