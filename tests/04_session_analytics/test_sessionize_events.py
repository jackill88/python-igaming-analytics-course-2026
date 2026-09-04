from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

sessionize_by_gap = load_challenge("04_session_analytics", "sessionize_events.py").sessionize_by_gap


def test_sessionize_adds_derived_session_id():
    events = rgs_events_frame()
    out = sessionize_by_gap(events, gap_minutes=30)
    assert "derived_session_id" in out.columns
    assert out["derived_session_id"].min() >= 1


def test_sessionize_player_101_single_session():
    out = sessionize_by_gap(rgs_events_frame(), gap_minutes=30)
    p101 = out[out.player_id == 101]
    assert p101["derived_session_id"].nunique() == 1
    assert p101["derived_session_id"].tolist() == [1, 1, 1]


def test_sessionize_player_102_two_sessions():
    out = sessionize_by_gap(rgs_events_frame(), gap_minutes=30)
    p102 = out[out.player_id == 102]
    assert p102["derived_session_id"].nunique() == 2
    assert p102["derived_session_id"].tolist() == [1, 2]
