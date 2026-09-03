import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

label_churn = load_challenge("08_churn_prediction", "label_churn.py").label_churn


def test_label():
    activity = daily_activity_frame()
    out = label_churn(activity, pd.Timestamp("2024-06-01"), horizon_days=30)
    assert "inactive_next_30_days" in out.columns
