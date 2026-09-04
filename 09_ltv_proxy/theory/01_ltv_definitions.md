# LTV Definitions

**LTV (Lifetime Value)** = total net revenue expected from a player over their relationship.

## True financial LTV

```
LTV ≈ ARPU × average lifetime
```

Requires PAM: deposits, withdrawals, bonuses, fees → **NGR per player**.

## RGS-only proxy

Without payments data, predict:

- **future_ggr_30d** / **future_ggr_90d**
- **future turnover** (total bets)

These rank players by **expected gameplay value**, not true profit.

## When proxy is enough

- Game recommendation ranking
- Segmentation for gameplay campaigns
- Resource allocation among CRM tiers

## When proxy fails

- Bonus-heavy markets (GGR ≠ NGR)
- Payment-fee-sensitive profitability analysis

## Key takeaway

Call it **expected future GGR**, not LTV, when presenting to finance stakeholders.
