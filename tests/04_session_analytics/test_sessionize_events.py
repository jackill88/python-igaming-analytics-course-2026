from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

sessionize_by_gap = load_challenge("04_session_analytics", "sessionize_events.py").sessionize_by_gap


def test_sessionize():
    out = sessionize_by_gap(rgs_events_frame(), gap_minutes=30)
    assert "derived_session_id" in out.columns
    assert out[out.player_id == 101]["derived_session_id"].nunique() >= 1
