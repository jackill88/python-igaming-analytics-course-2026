from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

session_durations = load_challenge("04_session_analytics", "session_duration.py").session_durations


def test_duration():
    out = session_durations(rgs_events_frame())
    assert set(out.columns) >= {"player_id", "session_id", "duration_minutes", "round_count"}
    assert out["duration_minutes"].min() >= 0
