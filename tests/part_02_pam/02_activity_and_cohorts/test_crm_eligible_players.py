import pandas as pd

from shared.datasets import pam_customers_frame
from shared.testing import load_challenge

crm_eligible_players = load_challenge(
    "part_02_pam/02_activity_and_cohorts", "crm_eligible_players.py"
).crm_eligible_players


def test_shared_sample():
    out = crm_eligible_players(pam_customers_frame())
    assert list(out.columns) == ["cid"]
    assert out["cid"].tolist() == [101, 102, 104]


def test_does_not_mutate():
    customers = pam_customers_frame()
    before = customers.copy()
    crm_eligible_players(customers)
    pd.testing.assert_frame_equal(customers, before)


def test_none_eligible():
    customers = pam_customers_frame()
    customers["status"] = "closed"
    out = crm_eligible_players(customers)
    assert out.empty
    assert list(out.columns) == ["cid"]
