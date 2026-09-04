# Session Metrics

Once sessions are defined, aggregate round-level RGS data to session grain.

## Core session metrics

| Metric | Formula |
|--------|---------|
| Session duration | `max(timestamp) - min(timestamp)` |
| Rounds per session | `COUNT(round_id)` |
| Bets per session | `SUM(bet_amount)` |
| GGR per session | `SUM(bet_amount - win_amount)` |
| Games per session | `COUNT(DISTINCT game_id)` |

## Typical distributions

- **Casual players:** many short sessions, few rounds
- **Whales:** fewer, longer sessions, high GGR
- **Weekend players:** session count spikes Fri–Sun

## Use cases

- Responsible gaming: flag unusually long sessions
- Product: optimize lobby → first bet time
- CRM: trigger re-engagement after short, low-GGR sessions

## Example aggregation

```python
sessions = events.groupby(["player_id", "session_id"]).agg(
    duration_minutes=("timestamp", lambda s: (s.max() - s.min()).total_seconds() / 60),
    round_count=("round_id", "count"),
    ggr=("bet_amount", lambda s: (s - events.loc[s.index, "win_amount"]).sum()),
)
```

## Key takeaway

Session metrics bridge **event-level RGS data** and **behavioral player profiles**.
