import pandas as pd
import pytest

from shared.datasets import pam_customers_frame, pam_game_rounds_frame, pam_transactions_frame
from shared.testing import load_challenge

anchor_retention = load_challenge(
    "part_02_pam/02_activity_and_cohorts", "anchor_retention.py"
).anchor_retention


def test_registration_day_1():
    rate = anchor_retention(
        pam_customers_frame(),
        pam_game_rounds_frame(),
        pam_transactions_frame(),
        "registration",
        1,
    )
    assert rate == pytest.approx(0.4)


def test_ftd_day_1():
    rate = anchor_retention(
        pam_customers_frame(),
        pam_game_rounds_frame(),
        pam_transactions_frame(),
        "ftd",
        1,
    )
    assert rate == pytest.approx(1 / 3)


def test_registration_day_0_on_sample():
    rate = anchor_retention(
        pam_customers_frame(),
        pam_game_rounds_frame(),
        pam_transactions_frame(),
        "registration",
        0,
    )
    assert rate == pytest.approx(0.0)


def test_unknown_anchor():
    with pytest.raises(ValueError):
        anchor_retention(
            pam_customers_frame(),
            pam_game_rounds_frame(),
            pam_transactions_frame(),
            "login",
            1,
        )


def test_no_deposits_ftd_cohort_is_empty():
    transactions = pam_transactions_frame().iloc[0:0]
    rate = anchor_retention(
        pam_customers_frame(),
        pam_game_rounds_frame(),
        transactions,
        "ftd",
        1,
    )
    assert rate == pytest.approx(0.0)
