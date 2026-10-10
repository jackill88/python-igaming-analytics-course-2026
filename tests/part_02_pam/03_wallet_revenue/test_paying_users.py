import pandas as pd

from shared.datasets import pam_transactions_frame
from shared.testing import load_challenge

paying_user_count = load_challenge(
    "part_02_pam/03_wallet_revenue", "paying_users.py"
).paying_user_count


def test_shared_sample():
    assert paying_user_count(pam_transactions_frame()) == 3


def test_repeat_deposits_count_once():
    extra = pam_transactions_frame()
    assert paying_user_count(pd.concat([extra, extra], ignore_index=True)) == 3


def test_withdrawals_and_rejections_are_not_paying():
    transactions = pd.DataFrame(
        {
            "cid": [1, 1],
            "tx_type": ["withdrawal", "deposit"],
            "status": ["approved", "rejected"],
        }
    )
    assert paying_user_count(transactions) == 0
