from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ggr_by_game = load_challenge("01_igaming_domain", "compute_ggr_by_game.py").ggr_by_game


def test_ggr_by_game():
    out = ggr_by_game(rgs_events_frame())
    assert list(out.columns) == ["game_id", "total_bets", "total_wins", "ggr"]
    assert out.iloc[0]["game_id"] == "roulette_b"
    assert out.iloc[0]["ggr"] == 60.0
