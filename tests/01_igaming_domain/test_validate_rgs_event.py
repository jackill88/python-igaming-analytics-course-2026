from shared.testing import load_challenge

validate_rgs_event = load_challenge("01_igaming_domain", "validate_rgs_event.py").validate_rgs_event


def test_valid_event():
    event = {
        "round_id": "r1", "player_id": 1, "session_id": "s1", "game_id": "slots_a",
        "timestamp": "2024-06-01", "bet_amount": 10.0, "win_amount": 0.0,
    }
    ok, errs = validate_rgs_event(event)
    assert ok is True
    assert errs == []


def test_missing_field():
    event = {"round_id": "r1", "player_id": 1}
    ok, errs = validate_rgs_event(event)
    assert ok is False
    assert len(errs) > 0


def test_negative_bet():
    event = {
        "round_id": "r1", "player_id": 1, "session_id": "s1", "game_id": "g",
        "timestamp": "2024-06-01", "bet_amount": -1.0, "win_amount": 0.0,
    }
    ok, errs = validate_rgs_event(event)
    assert ok is False
