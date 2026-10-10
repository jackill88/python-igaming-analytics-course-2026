import pandas as pd

from shared.datasets import (
    pam_game_rounds_frame,
    pam_login_sessions_frame,
    pam_transactions_frame,
)
from shared.testing import load_challenge

activity_counts = load_challenge(
    "part_02_pam/02_activity_and_cohorts", "activity_counts.py"
).activity_counts


def test_shared_sample_1_june():
    counts = activity_counts(
        pam_login_sessions_frame(),
        pam_game_rounds_frame(),
        pam_transactions_frame(),
        pd.Timestamp("2024-06-01"),
    )
    assert counts == {"login": 2, "play": 1, "deposit": 1}


def test_open_deposit_does_not_count():
    counts = activity_counts(
        pam_login_sessions_frame(),
        pam_game_rounds_frame(),
        pam_transactions_frame(),
        pd.Timestamp("2024-06-10"),
    )
    assert counts["deposit"] == 0


def test_quiet_day_is_zero():
    counts = activity_counts(
        pam_login_sessions_frame(),
        pam_game_rounds_frame(),
        pam_transactions_frame(),
        pd.Timestamp("2024-01-01"),
    )
    assert counts == {"login": 0, "play": 0, "deposit": 0}
