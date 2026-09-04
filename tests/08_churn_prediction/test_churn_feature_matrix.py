import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

build_churn_features = load_challenge(
    "08_churn_prediction", "churn_feature_matrix.py"
).build_churn_features


def test_churn_features_columns():
    out = build_churn_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert set(out.columns) == {
        "player_id",
        "days_since_last_session",
        "sessions_30d",
        "avg_bet_30d",
        "ggr_30d",
    }


def test_churn_features_player_101():
    out = build_churn_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    row = out[out.player_id == 101].iloc[0]
    assert row["sessions_30d"] == 1
    assert row["days_since_last_session"] == 2


def test_churn_features_includes_all_active_players():
    out = build_churn_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert set(out["player_id"]) == {101, 102, 103, 104}
