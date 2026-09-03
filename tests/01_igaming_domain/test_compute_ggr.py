from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

compute_ggr = load_challenge("01_igaming_domain", "compute_ggr.py").compute_ggr
total_ggr = load_challenge("01_igaming_domain", "compute_ggr.py").total_ggr


def test_compute_ggr_column():
    df = rgs_events_frame()
    out = compute_ggr(df)
    assert "ggr" in out.columns
    assert out.loc[0, "ggr"] == 10.0
    assert out.loc[1, "ggr"] == -10.0


def test_total_ggr():
    df = rgs_events_frame()
    assert total_ggr(df) == -4.0
