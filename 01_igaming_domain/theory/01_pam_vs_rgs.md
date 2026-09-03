# PAM vs RGS

Online casino platforms split into two core systems. Understanding this split is essential for scoping what analytics you can build.

## PAM — Player Account Management

Customer-facing platform holding:

- Player accounts, registration, KYC
- Wallets, deposits, withdrawals
- Bonuses, VIP levels, CRM campaigns
- Promotions and communication history

**Analytics unlocked:** ARPU, ARPPU, NGR, bonus cost, payment funnels, true financial LTV.

## RGS — Remote Gaming Server

Gameplay platform producing event streams:

| Field | Description |
|-------|-------------|
| `player_id` | Unique player identifier |
| `session_id` | Gameplay session |
| `game_id` | Game played |
| `round_id` | Individual bet round |
| `timestamp` | Event time |
| `bet_amount` | Wager amount |
| `win_amount` | Payout amount |

**Analytics unlocked:** GGR, session analytics, game popularity, behavioral features, churn (activity-based), gameplay LTV proxy.

## Current constraint in this course

The team only has **RGS data**. Initial analytics and ML must rely on gameplay events, not payment or CRM data.

## Implication for your roadmap

Build value with RGS first:

1. Engagement dashboards (DAU, retention)
2. GGR reporting
3. Churn and segmentation models
4. Game recommendations from play history

Defer until PAM is available:

- True LTV and NGR reporting
- Bonus hunter detection (needs bonus data)
- Deposit-triggered next-best-action
