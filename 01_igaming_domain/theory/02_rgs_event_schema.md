# RGS Event Schema

Every analytics pipeline starts with a clear **grain** definition.

## Recommended grain: one row per round

```
round_id (PK)
player_id (FK)
session_id
game_id (FK)
timestamp (UTC)
bet_amount >= 0
win_amount >= 0
```

## Derived fields

```python
ggr = bet_amount - win_amount
```

## Validation rules

1. All required fields present
2. `bet_amount >= 0` and `win_amount >= 0`
3. `timestamp` in UTC
4. `(player_id, round_id)` unique — no duplicate rounds

## Session vs round

- **Round:** single bet/spin/hand — finest grain for GGR
- **Session:** group of rounds — use for engagement duration
- RGS may provide `session_id`; you can also derive sessions with gap-based logic (Module 04)

## Example event

```python
{
    "round_id": "r_abc123",
    "player_id": 10042,
    "session_id": "s_xyz789",
    "game_id": "slots_lucky_7",
    "timestamp": "2024-06-01T10:05:00Z",
    "bet_amount": 10.0,
    "win_amount": 0.0,
}
```

## Warehouse table design

| Column | Type | Notes |
|--------|------|-------|
| round_id | STRING | Primary key |
| player_id | INT64 | Partition key candidate |
| event_ts | TIMESTAMP | Event time, UTC |
| bet_amount | DECIMAL | Non-negative |
| win_amount | DECIMAL | Non-negative |

Partition by `DATE(event_ts)` for query performance at scale.
