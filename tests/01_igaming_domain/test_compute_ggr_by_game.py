import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ggr_by_game = load_challenge("01_igaming_domain", "compute_ggr_by_game.py").ggr_by_game


def test_ggr_by_game_columns_and_top_game():
    out = ggr_by_game(rgs_events_frame())
    assert list(out.columns) == ["game_id", "total_bets", "total_wins", "ggr"]
    assert out.iloc[0]["game_id"] == "roulette_b"
    assert out.iloc[0]["ggr"] == 60.0
    assert out.iloc[0]["total_bets"] == 60.0
    assert out.iloc[0]["total_wins"] == 0.0


def test_ggr_by_game_sorted_descending():
    out = ggr_by_game(rgs_events_frame())
    assert out["ggr"].tolist() == sorted(out["ggr"].tolist(), reverse=True)


def test_ggr_by_game_empty():
    empty = pd.DataFrame(columns=["game_id", "bet_amount", "win_amount"])
    out = ggr_by_game(empty)
    assert list(out.columns) == ["game_id", "total_bets", "total_wins", "ggr"]
    assert len(out) == 0
