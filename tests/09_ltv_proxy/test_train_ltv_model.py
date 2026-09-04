import pandas as pd
from shared.testing import load_challenge

train_ltv_regressor = load_challenge("09_ltv_proxy", "train_ltv_model.py").train_ltv_regressor


def test_train_ltv_predict():
    features = pd.DataFrame(
        {
            "player_id": [1, 2, 3],
            "ggr_30d": [100.0, 50.0, 10.0],
            "sessions_30d": [20, 10, 2],
            "avg_bet_30d": [5.0, 4.0, 2.0],
        }
    )
    targets = pd.Series([120.0, 40.0, 15.0])
    model = train_ltv_regressor(features, targets, random_state=42)
    preds = model.predict(features.drop(columns=["player_id"]))
    assert len(preds) == 3
    assert preds.dtype.kind in {"f", "i"}


def test_train_ltv_regressor_fitted():
    features = pd.DataFrame({"ggr_30d": [1.0, 2.0], "sessions_30d": [1, 2]})
    targets = pd.Series([10.0, 20.0])
    model = train_ltv_regressor(features, targets, random_state=42)
    assert hasattr(model, "predict")
