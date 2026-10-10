import pandas as pd

from shared.datasets import pam_bonus_claims_frame
from shared.testing import load_challenge

bonus_cost_per_player = load_challenge(
    "part_02_pam/04_bonus_and_ngr", "bonus_cost.py"
).bonus_cost_per_player


def test_shared_sample():
    out = bonus_cost_per_player(pam_bonus_claims_frame()).set_index("cid")
    assert out.loc[101, "bonus_cost_eur"] == 10.0
    assert out.loc[102, "bonus_cost_eur"] == 20.0
    assert out.loc[103, "bonus_cost_eur"] == 30.0


def test_sums_multiple_claims():
    claims = pd.DataFrame({"cid": [101, 101, 102], "bonus_cost_eur": [10.0, 5.0, 1.0]})
    out = bonus_cost_per_player(claims).set_index("cid")
    assert list(bonus_cost_per_player(claims)["cid"]) == [101, 102]
    assert out.loc[101, "bonus_cost_eur"] == 15.0


def test_empty():
    claims = pam_bonus_claims_frame().iloc[0:0]
    out = bonus_cost_per_player(claims)
    assert list(out.columns) == ["cid", "bonus_cost_eur"]
    assert out.empty
