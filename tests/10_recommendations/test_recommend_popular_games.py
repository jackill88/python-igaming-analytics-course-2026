from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

recommend_popular_unplayed = load_challenge(
    "10_recommendations", "recommend_popular_games.py"
).recommend_popular_unplayed


def test_recommend_unplayed_player_101():
    recs = recommend_popular_unplayed(rgs_events_frame(), player_id=101, n=1)
    assert recs == ["blackjack_c"]


def test_recommend_excludes_played_games():
    recs = recommend_popular_unplayed(rgs_events_frame(), player_id=101, n=3)
    assert "slots_a" not in recs
    assert "roulette_b" not in recs


def test_recommend_respects_n():
    recs = recommend_popular_unplayed(rgs_events_frame(), player_id=102, n=2)
    assert len(recs) <= 2
    assert len(set(recs)) == len(recs)
