# Offline Evaluation

Evaluate recommenders on historical data before A/B tests.

## Holdout scheme

Hide last N interactions per player. Train on earlier history. Predict hidden games.

## Metrics

| Metric | Definition |
|--------|------------|
| Hit rate@K | Fraction of users with ≥1 hit in top K |
| MRR | Mean reciprocal rank of first hit |
| Coverage | % of catalog recommended |
| Diversity | Average dissimilarity within list |

## iGaming specifics

- Weight by **GGR contribution** of recommended games, not just clicks
- Penalize recommending games player already plays heavily (unless cross-sell goal)

## Online validation

Run A/B test: control = popularity, treatment = CF model.

Primary KPI: incremental GGR per exposed user.

## Key takeaway

Offline hit rate **does not guarantee** revenue lift — always plan an A/B test.
