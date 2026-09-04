from shared.datasets import rgs_events_frame
from shared.sql_helpers import query_duckdb
from shared.testing import load_challenge

top_games_by_ggr_sql = load_challenge("05_sql_gaming_analytics", "top_games_sql.py").top_games_by_ggr_sql


def _rounds_table():
    df = rgs_events_frame()
    return df[["round_id", "player_id", "game_id", "bet_amount", "win_amount", "timestamp"]]


def test_top_games_sql_shape_and_columns():
    result = query_duckdb(top_games_by_ggr_sql(), {"rounds": _rounds_table()})
    assert len(result) == 3
    assert list(result.columns) == ["game_id", "ggr"]


def test_top_games_sql_first_is_roulette():
    result = query_duckdb(top_games_by_ggr_sql(), {"rounds": _rounds_table()})
    assert result.iloc[0]["game_id"] == "roulette_b"
    assert float(result.iloc[0]["ggr"]) == 60.0


def test_top_games_sql_sorted_descending():
    result = query_duckdb(top_games_by_ggr_sql(), {"rounds": _rounds_table()})
    assert result["ggr"].tolist() == sorted(result["ggr"].tolist(), reverse=True)
