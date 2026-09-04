# dbt Feature Tables

Phase 2: transform raw rounds into analytics-ready marts.

## Layering

```
stg_rgs_rounds        -- clean, rename, cast
int_player_daily      -- daily aggregates per player
mart_player_features  -- player_features_daily for ML
mart_cohort_retention -- reporting
```

## Example dbt model: player_features_daily

```sql
-- models/mart/player_features_daily.sql
SELECT
    player_id,
    {{ var('feature_date') }} AS feature_date,
    DATE_DIFF('day', MAX(timestamp), {{ var('feature_date') }}) AS days_since_last_session,
    COUNT(DISTINCT session_id) AS sessions_30d,
    AVG(bet_amount) AS avg_bet_30d,
    SUM(bet_amount - win_amount) AS ggr_30d
FROM {{ ref('stg_rgs_rounds') }}
WHERE timestamp >= {{ var('feature_date') }} - INTERVAL 30 DAY
  AND timestamp < {{ var('feature_date') }}
GROUP BY player_id
```

## Testing in dbt

- `unique(player_id, feature_date)`
- `not_null` on key columns
- Referential integrity to `dim_player`

## Why dbt before Feast

Single transformation layer shared by BI and ML. Add feature store only when online serving requires it.

## Key takeaway

dbt models are **versioned, tested SQL** — the right first "feature platform" for iGaming analytics.
