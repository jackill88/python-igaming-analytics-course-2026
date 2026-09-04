# Active Player Definitions

Different teams define "active" differently. Misaligned definitions cause conflicting KPIs.

## Common definitions in iGaming

| Definition | Data source | Pros | Cons |
|------------|-------------|------|------|
| Round played | RGS | Objective, revenue-linked | Misses lobby browsers |
| Bet placed | RGS | Revenue-aligned | Excludes free-play |
| Deposit made | PAM | Monetization signal | Ignores existing balance play |
| Login | PAM | Broad reach | Inflates vs real play |

## With RGS-only data

Recommended default: **player with ≥1 round on date D**.

Build a daily spine:

```
player_daily_activity(player_id, activity_date)
```

Populate from `MIN(DATE(timestamp))` per player per day from round-level events.

## Edge cases

- **Cross-midnight sessions** — attribute activity to the date of each round, not session start
- **Timezone** — store UTC, convert to reporting timezone at aggregate time
- **Test accounts** — filter `is_test = false` if flagged in dim_player

## Key takeaway

Document your active definition in the **data catalog** and reuse it for DAU, retention, and churn labels.
