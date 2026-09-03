# GGR and Revenue Metrics

## GGR — Gross Gaming Revenue

The most important casino metric computable from RGS data alone.

```
GGR = Total Bets − Total Wins
```

**Example:**

- Bets: $1,000,000
- Wins: $940,000
- **GGR: $60,000**

At the round level: `ggr = bet_amount - win_amount`. Sum across rounds, players, games, or time periods.

## NGR — Net Gaming Revenue

Requires PAM / financial data:

```
NGR = GGR − Bonuses − Taxes − Provider Fees − Payment Costs
```

Not computable from RGS alone.

## ARPU / ARPPU

| Metric | Formula | Data source |
|--------|---------|---------------|
| ARPU | Revenue / Active Users | Needs PAM revenue |
| ARPPU | Revenue / Paying Users | Needs deposit data |

With RGS only, use **GGR per active player** as a proxy — not true ARPU.

## LTV — Lifetime Value

True LTV: `ARPU × Lifetime` (needs payment data).

RGS proxy: predict **future GGR** or **future turnover** from gameplay features (Module 09).

## Reporting hierarchy

```
Round GGR
  → Session GGR (sum rounds in session)
    → Player daily GGR
      → Game daily GGR
        → Platform daily GGR
```

Always state the grain when reporting revenue numbers.
