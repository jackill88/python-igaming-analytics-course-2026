import pandas as pd

from shared.datasets import pam_transactions_frame
from shared.testing import load_challenge

first_deposit = load_challenge(
    "part_02_pam/03_wallet_revenue", "first_deposit.py"
).first_deposit


def test_shared_sample():
    out = first_deposit(pam_transactions_frame()).set_index("cid")
    assert list(out.columns) == ["first_deposit_at", "amount_eur"]
    assert out.index.tolist() == [101, 102, 103]
    assert out.loc[101, "amount_eur"] == 117.0
    assert pd.Timestamp(out.loc[101, "first_deposit_at"]) == pd.Timestamp("2024-05-02 09:00:00")
    assert out.loc[102, "amount_eur"] == 80.0
    assert out.loc[103, "amount_eur"] == 46.8


def test_tie_breaks_on_transaction_id():
    transactions = pd.DataFrame(
        {
            "transaction_id": ["2", "1"],
            "cid": [7, 7],
            "tx_type": ["deposit", "deposit"],
            "status": ["approved", "approved"],
            "amount_eur": [50.0, 10.0],
            "created_at": pd.to_datetime(["2024-05-01 00:00:00", "2024-05-01 00:00:00"]),
        }
    )
    out = first_deposit(transactions)
    assert out.loc[0, "amount_eur"] == 10.0
    assert out.loc[0, "cid"] == 7


def test_no_approved_deposits():
    transactions = pam_transactions_frame()
    transactions["status"] = "rejected"
    out = first_deposit(transactions)
    assert list(out.columns) == ["cid", "first_deposit_at", "amount_eur"]
    assert out.empty
