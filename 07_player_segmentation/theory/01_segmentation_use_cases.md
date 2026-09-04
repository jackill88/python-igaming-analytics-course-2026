# Segmentation Use Cases

Segmentation groups players by **behavior** for targeted product and CRM actions.

## Typical iGaming segments

| Segment | Signals | Action |
|---------|---------|--------|
| Whales | High ggr_30d, frequent sessions | VIP host, exclusive games |
| Casuals | Low bet, occasional play | Onboarding offers |
| Weekend players | Activity Fri–Sun only | Weekend promotions |
| Churn-risk | High days_since_last_session, falling sessions | Win-back campaign |
| Bonus hunters | Needs PAM bonus data | Restrict offers |

## Features for clustering

```
days_since_last_session
sessions_30d
avg_bet_30d
ggr_30d
favorite_game_30d (encoded)
```

## Batch vs rules

- **Rules:** `IF ggr_30d > X THEN whale` — interpretable, brittle
- **Clustering:** data-driven groups — needs profiling and naming

## Key takeaway

Segments are useful when each group gets a **different business action** — avoid segmentation for its own sake.
