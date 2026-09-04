from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

mod = load_challenge("01_igaming_domain", "compute_ggr.py")
compute_ggr = mod.compute_ggr
total_ggr = mod.total_ggr


def test_compute_ggr_adds_column_without_mutating_input():
    df = rgs_events_frame()
    original_cols = list(df.columns)
    out = compute_ggr(df)
    assert list(df.columns) == original_cols
    assert "ggr" in out.columns
    assert out.loc[0, "ggr"] == 10.0
    assert out.loc[1, "ggr"] == -10.0
    assert out.loc[2, "ggr"] == 20.0


def test_total_ggr_shared_sample():
    assert total_ggr(rgs_events_frame()) == -4.0


def test_total_ggr_empty_frame():
    import pandas as pd

    empty = pd.DataFrame(columns=["bet_amount", "win_amount"])
    assert total_ggr(empty) == 0.0
