import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

sessions_7d = load_challenge("06_feature_engineering", "sessions_in_window.py").sessions_7d


def test_sessions_7d_player_103():
    out = sessions_7d(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert out.loc[out.player_id == 103, "sessions_7d"].iloc[0] == 1


def test_sessions_7d_window_excludes_old_activity():
    events = rgs_events_frame()
    out = sessions_7d(events, pd.Timestamp("2024-05-15"))
    assert len(out) == 0


def test_sessions_7d_counts_distinct_sessions():
    events = pd.DataFrame(
        {
            "player_id": [1, 1, 1],
            "session_id": ["a", "b", "b"],
            "timestamp": [
                pd.Timestamp("2024-06-01"),
                pd.Timestamp("2024-06-02"),
                pd.Timestamp("2024-06-02 10:00"),
            ],
            "round_id": ["r1", "r2", "r3"],
            "game_id": ["g"] * 3,
            "bet_amount": [1.0, 1.0, 1.0],
            "win_amount": [0.0, 0.0, 0.0],
        }
    )
    out = sessions_7d(events, pd.Timestamp("2024-06-02"))
    assert out.loc[out.player_id == 1, "sessions_7d"].iloc[0] == 2
