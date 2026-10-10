from shared.testing import load_challenge

classify_metric_source = load_challenge(
    "part_02_pam/01_what_changes", "classify_metric_source.py"
).classify_metric_source


def test_known_services():
    assert classify_metric_source("login_dau") == "service-customers"
    assert classify_metric_source("kyc_status") == "service-customers"
    assert classify_metric_source("deposits") == "service-wallet"
    assert classify_metric_source("bonus_claims") == "service-wallet"
    assert classify_metric_source("game_rounds") == "service-casino"
    assert classify_metric_source("free_spins") == "service-casino"
    assert classify_metric_source("bonus_definitions") == "service-offerings"
    assert classify_metric_source("messages_sent") == "service-communications"
    assert classify_metric_source("daily_gaming_activity") == "service-bo-reports"


def test_unknown_metric():
    assert classify_metric_source("customer_balance") == "unknown"
    assert classify_metric_source("") == "unknown"
