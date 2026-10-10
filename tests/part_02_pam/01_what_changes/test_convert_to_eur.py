import pandas as pd
import pytest

from shared.datasets import pam_fx_rates_frame
from shared.testing import load_challenge

to_eur = load_challenge("part_02_pam/01_what_changes", "convert_to_eur.py").to_eur


def test_gbp_on_shared_card():
    assert to_eur(100, "GBP", pam_fx_rates_frame()) == pytest.approx(117.0)


def test_eur_identity():
    assert to_eur(80, "EUR", pam_fx_rates_frame()) == pytest.approx(80.0)


def test_missing_currency_raises():
    with pytest.raises(KeyError):
        to_eur(10, "ZAR", pam_fx_rates_frame())


def test_does_not_mutate_rates():
    rates = pam_fx_rates_frame()
    before = rates.copy()
    to_eur(1, "SEK", rates)
    pd.testing.assert_frame_equal(rates, before)
