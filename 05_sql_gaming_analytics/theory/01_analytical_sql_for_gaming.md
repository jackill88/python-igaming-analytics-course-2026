# Analytical SQL for Gaming

RGS data lives in round-level fact tables. Analytical SQL transforms it into product and revenue insights.

## Core tables

```sql
rounds(round_id, player_id, session_id, game_id, timestamp, bet_amount, win_amount)
games(game_id, game_name, category, provider)
players(player_id, registration_date, country)
```

## Grain discipline

Every query should declare grain explicitly:

- One row per round → GGR per round
- One row per player per day → daily activity
- One row per player per game → affinity

## Common patterns

```sql
-- GGR by game
SELECT game_id, SUM(bet_amount - win_amount) AS ggr
FROM rounds
GROUP BY game_id;

-- Top players by turnover
SELECT player_id, SUM(bet_amount) AS turnover
FROM rounds
GROUP BY player_id
ORDER BY turnover DESC
LIMIT 100;
```

## DuckDB in this course

Tests run your SQL strings against in-memory DuckDB with sample DataFrames — same patterns apply to Postgres/ClickHouse in production.

## Key takeaway

State **grain**, **filters** (date range, test accounts), and **join keys** before writing gaming SQL.
