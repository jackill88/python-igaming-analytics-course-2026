import pandas as pd
import pytest

from shared.datasets import pam_customers_frame, pam_game_rounds_frame, pam_transactions_frame
from shared.testing import load_challenge

pam_player_features = load_challenge(
    "part_02_pam/05_models_and_pipeline", "pam_player_features.py"
).pam_player_features


def test_feature_date_excludes_later_rounds_and_open_deposits():
    out = pam_player_features(
        pam_customers_frame(),
        pam_transactions_frame(),
        pam_game_rounds_frame(),
        pd.Timestamp("2024-06-01"),
    )
    assert out["cid"].tolist() == [101, 102, 103, 104, 105]
    row = out.set_index("cid")
    assert row.loc[101, "days_since_ftd"] == 30
    assert row.loc[101, "deposits_30d"] == 1
    assert row.loc[101, "bonus_ggr_share"] == pytest.approx(0.0)
    assert row.loc[101, "crm_eligible"] == 1
    assert row.loc[102, "days_since_ftd"] == 12
    assert row.loc[102, "bonus_ggr_share"] == pytest.approx(1 / 3)
    assert row.loc[103, "days_since_ftd"] == 16
    assert row.loc[103, "bonus_ggr_share"] == pytest.approx(1.0)
    assert row.loc[103, "crm_eligible"] == 0
    assert pd.isna(row.loc[104, "days_since_ftd"])
    assert row.loc[104, "deposits_30d"] == 0
    assert row.loc[104, "crm_eligible"] == 1
    assert pd.isna(row.loc[105, "days_since_ftd"])
    assert row.loc[105, "crm_eligible"] == 0


def test_columns():
    out = pam_player_features(
        pam_customers_frame(),
        pam_transactions_frame(),
        pam_game_rounds_frame(),
        pd.Timestamp("2024-06-01"),
    )
    assert list(out.columns) == [
        "cid",
        "days_since_ftd",
        "deposits_30d",
        "bonus_ggr_share",
        "crm_eligible",
    ]
