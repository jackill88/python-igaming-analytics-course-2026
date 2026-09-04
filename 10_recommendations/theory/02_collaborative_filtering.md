# Collaborative Filtering

Recommend items based on **similar users' behavior**.

## User-item matrix

```
           slots_a  roulette_b  blackjack_c
player_1       12          0            3
player_2        0         45            0
player_3        8          2            0
```

Values = round counts or implicit feedback (played = 1).

## Approaches

| Method | Idea |
|--------|------|
| Item-based CF | Similar games played by same users |
| Matrix factorization | Latent taste factors |
| LightFM | Hybrid (optional side features) |
| Popular baseline | Global top games not yet played |

## Cold start

- **New player:** popular games in their country / device
- **New game:** content-based (category, provider, RTP)

## This course baseline

`recommend_popular_unplayed` — strong first baseline before CF.

## Key takeaway

Always benchmark CF against **popularity baseline** — often 80% of the gain for 20% of the complexity.
