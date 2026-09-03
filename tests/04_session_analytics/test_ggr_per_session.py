from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ggr_per_session = load_challenge("04_session_analytics", "ggr_per_session.py").ggr_per_session


def test_ggr_session():
    out = ggr_per_session(rgs_events_frame())
    assert "ggr" in out.columns
    assert out["ggr"].sum() == -4.0
