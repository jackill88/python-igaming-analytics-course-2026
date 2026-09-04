"""
Challenge: Validate RGS Event
Module 01: iGaming Domain & RGS Events

Theory: theory/02_rgs_event_schema.md

Inputs:
  event — dict with round-level RGS fields

Outputs:
  (is_valid, list_of_error_messages) — True and [] when valid

Edge cases:
  - Missing any required field → error per field
  - Negative bet_amount or win_amount → validation error

Example:
  >>> validate_rgs_event({"round_id": "r1", "player_id": 1, ...})
  (True, [])

Run: pytest tests/01_igaming_domain/test_validate_rgs_event.py -v
"""

REQUIRED_FIELDS = {"round_id", "player_id", "session_id", "game_id", "timestamp", "bet_amount", "win_amount"}


def validate_rgs_event(event: dict) -> tuple[bool, list[str]]:
    """Return (is_valid, list_of_error_messages)."""
    pass
