import pandas as pd
from shared.datasets import rgs_events_frame
from shared.sql_helpers import query_duckdb
from shared.testing import load_challenge

top_games_by_ggr_sql = load_challenge("05_sql_gaming_analytics", "top_games_sql.py").top_games_by_ggr_sql


def test_top_games():
    df = rgs_events_frame().rename(columns={"round_id": "round_id"})
    rounds = df[["round_id", "player_id", "game_id", "bet_amount", "win_amount", "timestamp"]]
    sql = top_games_by_ggr_sql()
    result = query_duckdb(sql, {"rounds": rounds})
    assert len(result) <= 3
    assert "game_id" in result.columns
