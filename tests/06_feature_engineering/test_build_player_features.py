import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

build_player_features = load_challenge("06_feature_engineering", "build_player_features.py").build_player_features


def test_player_features():
    out = build_player_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    cols = {"player_id", "sessions_7d", "avg_bet_7d", "ggr_7d", "favorite_game_7d"}
    assert cols <= set(out.columns)
