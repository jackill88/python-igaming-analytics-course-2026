from shared.datasets import rgs_events_frame
from shared.sql_helpers import query_duckdb
from shared.testing import load_challenge

player_favorite_game_sql = load_challenge(
    "05_sql_gaming_analytics", "player_favorite_game_sql.py"
).player_favorite_game_sql


def _rounds_table():
    df = rgs_events_frame()
    return df[["round_id", "player_id", "game_id", "bet_amount", "win_amount", "timestamp"]]


def test_favorite_game_player_101():
    result = query_duckdb(player_favorite_game_sql(), {"rounds": _rounds_table()})
    assert result.loc[result.player_id == 101, "favorite_game"].iloc[0] == "slots_a"


def test_favorite_game_one_row_per_player():
    result = query_duckdb(player_favorite_game_sql(), {"rounds": _rounds_table()})
    assert len(result) == rgs_events_frame()["player_id"].nunique()
    assert result["player_id"].is_unique


def test_favorite_game_tie_break():
    import pandas as pd

    rounds = pd.DataFrame(
        {
            "round_id": ["a", "b", "c", "d"],
            "player_id": [1, 1, 1, 1],
            "game_id": ["game_b", "game_b", "game_a", "game_a"],
            "bet_amount": [1.0, 1.0, 1.0, 1.0],
            "win_amount": [0.0, 0.0, 0.0, 0.0],
            "timestamp": pd.date_range("2024-06-01", periods=4, freq="h"),
        }
    )
    result = query_duckdb(player_favorite_game_sql(), {"rounds": rounds})
    assert result.loc[result.player_id == 1, "favorite_game"].iloc[0] == "game_a"
