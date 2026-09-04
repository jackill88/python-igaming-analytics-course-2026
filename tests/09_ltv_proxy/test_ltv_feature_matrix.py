import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ltv_features = load_challenge("09_ltv_proxy", "ltv_feature_matrix.py").ltv_features


def test_ltv_features_columns():
    out = ltv_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert set(out.columns) == {"player_id", "ggr_30d", "sessions_30d", "avg_bet_30d"}


def test_ltv_features_player_103():
    out = ltv_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    row = out[out.player_id == 103].iloc[0]
    assert row["sessions_30d"] == 1
    assert row["ggr_30d"] == 26.0


def test_ltv_features_all_players_before_snapshot():
    out = ltv_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert set(out["player_id"]) == {101, 102, 103, 104}
