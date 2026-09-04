# Session Definitions

A **session** is a contiguous period of player activity.

## RGS-provided session_id

Many RGS platforms emit `session_id` with each round. Use it when trustworthy.

Validate:

- Sessions don't span implausible durations (e.g. 48 hours)
- `session_id` resets on logout / timeout rules you expect

## Derived sessions (gap-based)

When `session_id` is missing or unreliable:

```
New session when: timestamp - previous_timestamp > gap_threshold
Typical gap: 30 minutes
```

Partition by `player_id`, order by `timestamp`.

## Session grain vs round grain

| Grain | Use for |
|-------|---------|
| Round | GGR, game analytics |
| Session | Engagement duration, bets per visit |

## Key takeaway

Document whether sessions come from **RGS** or **derived logic** — mixing breaks trend comparisons.
