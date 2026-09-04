import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

build_player_features = load_challenge(
    "06_feature_engineering", "build_player_features.py"
).build_player_features


def test_player_features_columns_and_players():
    out = build_player_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert set(out.columns) == {
        "player_id",
        "sessions_7d",
        "avg_bet_7d",
        "ggr_7d",
        "favorite_game_7d",
    }
    assert set(out["player_id"]) == {101, 102, 103, 104}


def test_player_features_player_101():
    out = build_player_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    row = out[out.player_id == 101].iloc[0]
    assert row["sessions_7d"] == 1
    assert row["favorite_game_7d"] == "slots_a"
    assert row["ggr_7d"] == 20.0


def test_player_features_avg_bet():
    out = build_player_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    row = out[out.player_id == 101].iloc[0]
    assert abs(row["avg_bet_7d"] - 35.0 / 3) < 1e-6
