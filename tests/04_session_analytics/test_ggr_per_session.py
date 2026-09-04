from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ggr_per_session = load_challenge("04_session_analytics", "ggr_per_session.py").ggr_per_session


def test_ggr_per_session_player_101():
    out = ggr_per_session(rgs_events_frame())
    row = out[(out.player_id == 101) & (out.session_id == "s1")].iloc[0]
    assert row["total_bets"] == 35.0
    assert row["total_wins"] == 15.0
    assert row["ggr"] == 20.0


def test_ggr_per_session_columns():
    out = ggr_per_session(rgs_events_frame())
    assert list(out.columns) == ["player_id", "session_id", "total_bets", "total_wins", "ggr"]


def test_ggr_per_session_row_count():
    out = ggr_per_session(rgs_events_frame())
    assert len(out) == rgs_events_frame()[["player_id", "session_id"]].drop_duplicates().shape[0]
