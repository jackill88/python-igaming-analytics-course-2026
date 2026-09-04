# Top Games and Affinity

## Game popularity

Rank games by:

- **Round count** — engagement volume
- **Unique players** — reach
- **GGR** — revenue contribution
- **Turnover** (total bets) — handle / liquidity

```sql
SELECT game_id,
       COUNT(*) AS rounds,
       COUNT(DISTINCT player_id) AS unique_players,
       SUM(bet_amount - win_amount) AS ggr
FROM rounds
GROUP BY game_id
ORDER BY ggr DESC;
```

## Player–game affinity

For each player, find **favorite game** = most rounds played (tie-break by `game_id`).

Use `ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY cnt DESC, game_id)`.

## Category mix

Join `games` to analyze slots vs table games per player segment.

## Product actions

- Promote high-GGR games to casual segments
- Cross-sell table games to slots-only players
- Retire low-engagement titles from the lobby

## Key takeaway

Popularity (rounds) and profitability (GGR) **diverge** — optimize for the metric that matches the business goal.
