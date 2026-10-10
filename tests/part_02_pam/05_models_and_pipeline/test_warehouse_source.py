import pytest

from shared.testing import load_challenge

warehouse_source = load_challenge(
    "part_02_pam/05_models_and_pipeline", "warehouse_source.py"
).warehouse_source


def test_fact_tables():
    assert warehouse_source("player_identity") == "customers"
    assert warehouse_source("login_activity") == "login_sessions"
    assert warehouse_source("historical_ggr") == "game_rounds"
    assert warehouse_source("deposits") == "transactions"
    assert warehouse_source("bonus_cost") == "bonuses_claimed"
    assert warehouse_source("bonus_catalogue") == "bonuses"
    assert warehouse_source("reconciliation_check") == "bo_reports"


def test_redis_push_is_not_ingested():
    assert warehouse_source("realtime_balance_push") is None


def test_unknown_metric():
    with pytest.raises(KeyError):
        warehouse_source("customer_balance")
