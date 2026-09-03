"""
Challenge: Validate RGS Event
Module 01: iGaming Domain & RGS Events

Run: pytest tests/01_igaming_domain/test_validate_rgs_event.py -v
"""

REQUIRED_FIELDS = {"round_id", "player_id", "session_id", "game_id", "timestamp", "bet_amount", "win_amount"}


def validate_rgs_event(event: dict) -> tuple[bool, list[str]]:
    """
    Return (is_valid, list_of_error_messages).
    Check all REQUIRED_FIELDS are present; bet_amount and win_amount must be >= 0.
    """
    pass
