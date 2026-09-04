from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

player_game_matrix = load_challenge(
    "10_recommendations", "player_game_matrix.py"
).player_game_matrix


def test_matrix_shape():
    matrix = player_game_matrix(rgs_events_frame())
    assert matrix.shape == (4, 3)
    assert list(matrix.columns) == ["blackjack_c", "roulette_b", "slots_a"]


def test_matrix_player_101_slots():
    matrix = player_game_matrix(rgs_events_frame())
    assert matrix.loc[101, "slots_a"] == 2
    assert matrix.loc[101, "roulette_b"] == 1
    assert matrix.loc[101, "blackjack_c"] == 0


def test_matrix_no_nan():
    matrix = player_game_matrix(rgs_events_frame())
    assert matrix.isna().sum().sum() == 0
