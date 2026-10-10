import pandas as pd
import pytest

from shared.datasets import pam_game_rounds_frame
from shared.testing import load_challenge

bonus_ggr_share = load_challenge(
    "part_02_pam/04_bonus_and_ngr", "bonus_ggr_share.py"
).bonus_ggr_share


def test_shared_sample():
    out = bonus_ggr_share(pam_game_rounds_frame()).set_index("cid")
    assert out.loc[101, "ggr_eur"] == pytest.approx(26.0)
    assert out.loc[101, "bonus_ggr_share"] == pytest.approx(5 / 30)
    assert out.loc[101, "bonus_ggr_eur"] == pytest.approx(26 * 5 / 30)
    assert out.loc[102, "bonus_ggr_share"] == pytest.approx(1 / 3)
    assert out.loc[102, "bonus_ggr_eur"] == pytest.approx(5.0)
    assert out.loc[103, "bonus_ggr_share"] == pytest.approx(1.0)
    assert out.loc[103, "bonus_ggr_eur"] == pytest.approx(30.0)


def test_zero_stake():
    rounds = pd.DataFrame(
        {
            "cid": [1],
            "cash_bet_eur": [0.0],
            "bonus_bet_eur": [0.0],
            "win_amount_eur": [0.0],
        }
    )
    out = bonus_ggr_share(rounds)
    assert out.loc[0, "bonus_ggr_share"] == pytest.approx(0.0)
    assert out.loc[0, "ggr_eur"] == pytest.approx(0.0)


def test_empty():
    rounds = pam_game_rounds_frame().iloc[0:0]
    out = bonus_ggr_share(rounds)
    assert list(out.columns) == ["cid", "ggr_eur", "bonus_ggr_eur", "bonus_ggr_share"]
    assert out.empty
