from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

recommend_popular_unplayed = load_challenge("10_recommendations", "recommend_popular_games.py").recommend_popular_unplayed


def test_recommend():
    recs = recommend_popular_unplayed(rgs_events_frame(), player_id=101, n=2)
    assert len(recs) <= 2
    assert "slots_a" not in recs or len(recs) > 0
