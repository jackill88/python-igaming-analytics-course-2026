# Interview Checklist

Use this checklist before analytics / applied ML interviews in iGaming.

## Domain metrics (must know)

- [ ] **GGR** = bets − wins (from RGS)
- [ ] **NGR** = GGR − bonuses − taxes − fees (needs PAM)
- [ ] **DAU / WAU / MAU** — unique active players
- [ ] **Stickiness** = DAU / MAU
- [ ] **D1 / D7 / D30 retention** — cohort-based
- [ ] **Churn** — commonly 30 days inactive
- [ ] **LTV proxy** — future GGR when PAM unavailable

## ML talking points

- [ ] Churn target: `inactive_next_30_days`
- [ ] Core features: `days_since_last_session`, `sessions_7d`, `avg_bet`, `ggr_30d`
- [ ] Segmentation: K-Means / HDBSCAN on behavioral features
- [ ] Models: LightGBM, XGBoost for churn; regression for LTV proxy
- [ ] Recommendations: collaborative filtering → matrix factorization → two-tower (advanced)

## Architecture talking points

- [ ] Phase 1: RGS → warehouse
- [ ] Phase 2: dbt feature tables (`player_features_daily`)
- [ ] Phase 3: batch ML (churn, segmentation, LTV)
- [ ] Phase 4: recommendations
- [ ] Phase 5: evaluate feature store (Feast) only if needed
- [ ] **Do NOT** start with a feature store

## Whiteboard exercise

Design a nightly churn scoring pipeline:

1. Ingest RGS events (grain: round)
2. Build daily player features in dbt
3. Train LightGBM weekly, score nightly
4. Write predictions to `churn_scores` table
5. CRM consumes top decile for campaigns

State: event volume, retention target, SLA (e.g. scores by 06:00 UTC).

## Questions to ask the interviewer

- What data do we have today — RGS only or PAM too?
- What is the primary business KPI — retention, GGR, or acquisition cost?
- Is inference batch (CRM) or real-time (in-session)?
- What does success look like in 90 days?
