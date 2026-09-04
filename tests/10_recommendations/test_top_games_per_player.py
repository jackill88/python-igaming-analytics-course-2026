from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

top_n_games_per_player = load_challenge(
    "10_recommendations", "top_games_per_player.py"
).top_n_games_per_player


def test_top_n_player_101_rank1():
    out = top_n_games_per_player(rgs_events_frame(), n=2)
    row = out[(out["player_id"] == 101) & (out["rank"] == 1)].iloc[0]
    assert row["game_id"] == "slots_a"


def test_top_n_rank_sequence():
    out = top_n_games_per_player(rgs_events_frame(), n=3)
    for player_id, grp in out.groupby("player_id"):
        assert grp["rank"].tolist() == list(range(1, len(grp) + 1))


def test_top_n_respects_n():
    out = top_n_games_per_player(rgs_events_frame(), n=1)
    assert (out.groupby("player_id").size() <= 1).all()
