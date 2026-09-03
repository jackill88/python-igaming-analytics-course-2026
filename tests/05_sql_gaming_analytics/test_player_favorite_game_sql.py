from shared.datasets import rgs_events_frame
from shared.sql_helpers import query_duckdb
from shared.testing import load_challenge

player_favorite_game_sql = load_challenge("05_sql_gaming_analytics", "player_favorite_game_sql.py").player_favorite_game_sql


def test_favorite_game():
    rounds = rgs_events_frame()[["round_id", "player_id", "game_id", "bet_amount", "win_amount", "timestamp"]]
    result = query_duckdb(player_favorite_game_sql(), {"rounds": rounds})
    assert "player_id" in result.columns
    assert "favorite_game" in result.columns
