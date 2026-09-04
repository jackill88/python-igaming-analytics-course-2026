# RGS to Warehouse

Phase 1 of the analytics stack: reliable ingestion of gameplay events.

## Source: RGS event stream

Fields: `round_id`, `player_id`, `session_id`, `game_id`, `timestamp`, `bet_amount`, `win_amount`.

Delivery: Kafka, Kinesis, webhook batch, or SFTP CSV dumps.

## Target: warehouse fact table

```sql
CREATE TABLE fct_rounds (
    round_id        VARCHAR PRIMARY KEY,
    player_id       BIGINT,
    session_id      VARCHAR,
    game_id         VARCHAR,
    event_ts        TIMESTAMP,   -- UTC
    bet_amount      DECIMAL(18,2),
    win_amount      DECIMAL(18,2),
    ingested_at     TIMESTAMP
);
```

## Design decisions

| Decision | Recommendation |
|----------|----------------|
| Grain | One row per round |
| Partition | `DATE(event_ts)` |
| Dedup key | `round_id` |
| Late data | Allow 24–72h replay window |
| Format | Parquet / Iceberg for lake; native tables for warehouse |

## Ingestion checklist

- Idempotent loads (upsert on `round_id`)
- Schema validation at landing zone
- Dead-letter queue for malformed events
- Row count + GGR sum reconciliation vs RGS daily report

## Key takeaway

Get **round-level facts correct and deduplicated** before building any ML — everything downstream depends on this table.
