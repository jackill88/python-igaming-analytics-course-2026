from shared.testing import load_challenge

validate_rgs_event = load_challenge("01_igaming_domain", "validate_rgs_event.py").validate_rgs_event

VALID = {
    "round_id": "r1",
    "player_id": 1,
    "session_id": "s1",
    "game_id": "slots_a",
    "timestamp": "2024-06-01",
    "bet_amount": 10.0,
    "win_amount": 0.0,
}


def test_valid_event():
    ok, errs = validate_rgs_event(VALID)
    assert ok is True
    assert errs == []


def test_missing_required_fields():
    ok, errs = validate_rgs_event({"round_id": "r1", "player_id": 1})
    assert ok is False
    assert "missing field: session_id" in errs
    assert "missing field: game_id" in errs
    assert "missing field: timestamp" in errs


def test_negative_bet_amount():
    event = {**VALID, "bet_amount": -1.0}
    ok, errs = validate_rgs_event(event)
    assert ok is False
    assert "bet_amount must be non-negative" in errs


def test_negative_win_amount():
    event = {**VALID, "win_amount": -5.0}
    ok, errs = validate_rgs_event(event)
    assert ok is False
    assert "win_amount must be non-negative" in errs
