from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

top_n_games_per_player = load_challenge("10_recommendations", "top_games_per_player.py").top_n_games_per_player


def test_top_n():
    out = top_n_games_per_player(rgs_events_frame(), n=2)
    assert set(out.columns) >= {"player_id", "rank", "game_id"}
