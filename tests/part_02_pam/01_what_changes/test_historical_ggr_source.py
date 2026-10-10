from shared.testing import load_challenge

is_historical_ggr_source = load_challenge(
    "part_02_pam/01_what_changes", "historical_ggr_source.py"
).is_historical_ggr_source


def test_historical_tables():
    assert is_historical_ggr_source("game_rounds") is True
    assert is_historical_ggr_source("transactions") is True


def test_balance_snapshot_is_rejected():
    assert is_historical_ggr_source("customer_balance") is False
    assert is_historical_ggr_source("bonuses") is False
    assert is_historical_ggr_source("login_sessions") is False
