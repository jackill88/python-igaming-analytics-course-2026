import pandas as pd
import pytest

from shared.datasets import pam_transactions_frame
from shared.testing import load_challenge

arpu_arppu = load_challenge(
    "part_02_pam/03_wallet_revenue", "arpu_arppu.py"
).arpu_arppu


def _revenue() -> pd.DataFrame:
    return pd.DataFrame({"cid": [101, 102, 103], "revenue_eur": [26.0, 15.0, 30.0]})


def test_shared_denominators():
    arpu, arppu = arpu_arppu(_revenue(), [101, 102, 103, 104, 104], pam_transactions_frame())
    assert arpu == pytest.approx(71 / 4)
    assert arppu == pytest.approx(71 / 3)


def test_empty_active_users():
    arpu, arppu = arpu_arppu(_revenue(), [], pam_transactions_frame())
    assert arpu == pytest.approx(0.0)
    assert arppu == pytest.approx(71 / 3)


def test_no_paying_users():
    transactions = pam_transactions_frame()
    transactions["status"] = "open"
    arpu, arppu = arpu_arppu(_revenue(), [101], transactions)
    assert arpu == pytest.approx(71.0)
    assert arppu == pytest.approx(0.0)
