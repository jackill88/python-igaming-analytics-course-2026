import pandas as pd
from shared.testing import load_challenge

train_ltv_regressor = load_challenge("09_ltv_proxy", "train_ltv_model.py").train_ltv_regressor


def test_train_ltv():
    features = pd.DataFrame({
        "player_id": [1, 2, 3],
        "ggr_30d": [10.0, 20.0, 5.0],
        "sessions_30d": [5, 10, 2],
        "avg_bet_30d": [2.0, 4.0, 1.0],
    })
    targets = pd.Series([15.0, 30.0, 8.0])
    model = train_ltv_regressor(features, targets, random_state=42)
    assert hasattr(model, "predict")
