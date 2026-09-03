import pandas as pd
from shared.testing import load_challenge

train_churn_classifier = load_challenge("08_churn_prediction", "train_churn_model.py").train_churn_classifier


def test_train():
    features = pd.DataFrame({
        "player_id": [1, 2, 3, 4],
        "sessions_30d": [10, 2, 8, 1],
        "avg_bet_30d": [5.0, 1.0, 4.0, 2.0],
        "ggr_30d": [100.0, -10.0, 50.0, -5.0],
        "days_since_last_session": [1, 20, 2, 25],
    })
    labels = pd.Series([0, 1, 0, 1])
    model = train_churn_classifier(features, labels, random_state=42)
    assert hasattr(model, "predict")
