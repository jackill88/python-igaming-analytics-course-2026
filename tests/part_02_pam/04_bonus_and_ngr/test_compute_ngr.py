import pandas as pd
import pytest

from shared.datasets import pam_bonus_claims_frame, pam_game_rounds_frame
from shared.testing import load_challenge

compute_ngr = load_challenge(
    "part_02_pam/04_bonus_and_ngr", "compute_ngr.py"
).compute_ngr


def test_shared_sample():
    out = compute_ngr(pam_game_rounds_frame(), pam_bonus_claims_frame(), 0.10, 0.20)
    out = out.set_index("cid")
    assert out.index.tolist() == [101, 102, 103]
    assert out.loc[101, "ggr_eur"] == pytest.approx(26.0)
    assert out.loc[101, "provider_fee_eur"] == pytest.approx(3.0)
    assert out.loc[101, "tax_eur"] == pytest.approx(5.2)
    assert out.loc[101, "ngr_eur"] == pytest.approx(7.8)
    assert out.loc[102, "ngr_eur"] == pytest.approx(-11.0)
    assert out.loc[103, "ggr_eur"] == pytest.approx(30.0)
    assert out.loc[103, "ngr_eur"] == pytest.approx(-10.0)


def test_claim_without_rounds():
    rounds = pam_game_rounds_frame().iloc[0:0]
    claims = pd.DataFrame({"cid": [9], "bonus_cost_eur": [4.0]})
    out = compute_ngr(rounds, claims, 0.10, 0.20)
    assert out.loc[0, "cid"] == 9
    assert out.loc[0, "ggr_eur"] == pytest.approx(0.0)
    assert out.loc[0, "ngr_eur"] == pytest.approx(-4.0)


def test_columns():
    out = compute_ngr(pam_game_rounds_frame(), pam_bonus_claims_frame(), 0.1, 0.2)
    assert list(out.columns) == [
        "cid",
        "ggr_eur",
        "bonus_cost_eur",
        "provider_fee_eur",
        "tax_eur",
        "ngr_eur",
    ]
