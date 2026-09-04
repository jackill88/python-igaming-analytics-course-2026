# Proxy Limitations

Be explicit about what RGS-based LTV models **cannot** do.

## Missing from RGS

| Factor | Impact |
|--------|--------|
| Bonuses | Overstates value of bonus-driven play |
| Deposits / payment fees | True margin unknown |
| Provider fees | Game-level profitability |
| Taxes & regulatory levies | Market-specific |
| Cross-sell to sportsbook | Needs unified PAM |

## Risk of overconfidence

High-GGR players who only play on bonus credit look valuable in RGS but may be **NGR-negative**.

## Communication template

> "This model ranks players by expected **gameplay GGR**. With PAM integration we can convert to **NGR-based LTV** for finance."

## Roadmap

1. Ship GGR proxy (now)
2. Integrate PAM bonus flags (phase 2)
3. True NGR LTV for finance reporting (phase 3)

## Key takeaway

Transparency about limitations builds trust with stakeholders more than overstating model scope.
