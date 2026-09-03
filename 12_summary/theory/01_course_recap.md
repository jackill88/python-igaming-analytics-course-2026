# Course Recap

You have worked through a complete iGaming analytics learning path built primarily on **RGS (Remote Gaming Server)** gameplay data.

## What you covered

| Phase | Modules | Skills |
|-------|---------|--------|
| Foundations | 01–04 | RGS events, GGR, DAU/WAU/MAU, cohorts, sessions |
| Analytics | 05–06 | SQL on gaming data, `player_features_daily` |
| ML | 07–09 | Segmentation, churn, LTV proxy |
| Product | 10–11 | Recommendations, pipeline architecture |
| Career | 12 | Stakeholder framing, interview prep |

## The RGS-only constraint

Throughout the course you worked without PAM (Player Account Management) data. That means:

- **Yes:** GGR, engagement, retention, churn, behavioral features, gameplay-based LTV proxy
- **Partial:** LTV (proxy via future GGR, not true financial LTV)
- **No:** ARPU, ARPPU, NGR, bonus costs, deposit/withdrawal analytics

## End-to-end flow

```
RGS events
    ↓
Warehouse (Postgres / ClickHouse / Iceberg)
    ↓
dbt feature models (player_features_daily)
    ↓
Batch ML (segmentation, churn, LTV proxy)
    ↓
Predictions table → CRM / product
```

## Completion checklist

- [ ] All pytest tests pass (`pytest -v`)
- [ ] Quizzes completed for each module
- [ ] Can explain GGR, DAU, D7 retention, and churn label from memory
- [ ] Can sketch warehouse → dbt → ML architecture on a whiteboard
