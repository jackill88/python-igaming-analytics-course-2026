import pandas as pd
from shared.testing import load_challenge

label_churn = load_challenge("08_churn_prediction", "label_churn.py").label_churn


def test_label_churn_inactive_player():
    activity = pd.DataFrame(
        {
            "player_id": [1, 1, 2, 2, 2],
            "activity_date": pd.to_datetime(
                ["2024-05-15", "2024-06-01", "2024-05-20", "2024-06-01", "2024-06-15"]
            ),
        }
    )
    out = label_churn(activity, pd.Timestamp("2024-06-01"), horizon_days=30)
    labels = dict(zip(out["player_id"], out["inactive_next_30_days"]))
    assert labels[1] == 1
    assert labels[2] == 0


def test_label_churn_active_in_horizon():
    activity = pd.DataFrame(
        {
            "player_id": [1, 1, 1],
            "activity_date": pd.to_datetime(["2024-05-15", "2024-06-01", "2024-06-15"]),
        }
    )
    out = label_churn(activity, pd.Timestamp("2024-06-01"), horizon_days=30)
    assert out.loc[out.player_id == 1, "inactive_next_30_days"].iloc[0] == 0


def test_label_churn_columns():
    activity = pd.DataFrame(
        {"player_id": [1], "activity_date": pd.to_datetime(["2024-06-01"])}
    )
    out = label_churn(activity, pd.Timestamp("2024-06-01"))
    assert list(out.columns) == ["player_id", "inactive_next_30_days"]
