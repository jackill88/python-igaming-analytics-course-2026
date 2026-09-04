from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

session_durations = load_challenge("04_session_analytics", "session_duration.py").session_durations


def test_session_duration_player_101():
    out = session_durations(rgs_events_frame())
    row = out[(out.player_id == 101) & (out.session_id == "s1")].iloc[0]
    assert row["duration_minutes"] == 35.0
    assert row["round_count"] == 3


def test_session_duration_columns():
    out = session_durations(rgs_events_frame())
    assert list(out.columns) == ["player_id", "session_id", "duration_minutes", "round_count"]


def test_session_duration_non_negative():
    out = session_durations(rgs_events_frame())
    assert (out["duration_minutes"] >= 0.0).all()
    assert (out["round_count"] >= 1).all()
