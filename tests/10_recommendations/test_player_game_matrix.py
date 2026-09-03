from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

player_game_matrix = load_challenge("10_recommendations", "player_game_matrix.py").player_game_matrix


def test_matrix():
    out = player_game_matrix(rgs_events_frame())
    assert out.loc[101, "slots_a"] >= 1
    assert out.fillna(0).min().min() >= 0
