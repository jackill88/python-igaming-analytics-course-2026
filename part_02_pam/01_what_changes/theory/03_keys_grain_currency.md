# Keys, grain, and currency

## Keys

Players are a numeric `cid`, allocated in blocks, not an auto-increment from a single table. The platform is multi-brand: the same person is not implied across brands, and almost every fact should carry `brand_id`.

Do not join a casino round to a wallet deposit on timestamp alone. Join on `cid` (and brand), then align dates in the analysis.

## Grain

| Fact | Grain | Historical? |
|------|-------|-------------|
| `game_rounds` | One settled round | Yes — append-only for practical purposes, with provider idempotency keys |
| `transactions` | One money movement | Yes |
| `customer_balance` | One mutable row per player | No — it is the current withdrawable, bonus, and casino-bonus balances |
| `customer_balance_log` | Before/after image of a mutation | Yes, as an audit, not as the GGR fact |

Historical GGR is stakes minus wins on rounds (or the matching bet/win transactions). Reading `customer_balance` today and subtracting yesterday's snapshot will drift: the row is locked, rounded, and repaired by reconciliation jobs. It is the wrong source for a backfill.

## Currency

Wallet amounts are `DECIMAL`, stored in the **customer currency** and mirrored in the **system currency, EUR**. Lifetime aggregates use a wider scale than a single transaction.

Report ARPU, NGR, and model labels in EUR unless a stakeholder asks for a brand-local view. Convert with the rate that applied to the transaction (`amount_eur` on the row) or, for an exercise rate card, `amount * eur_per_unit`.

```python
amount_eur = amount * eur_per_unit  # rate card: pam_fx_rates_frame
```

On the shared rate card, 100 GBP is 117 EUR (`eur_per_unit` 1.17). A missing currency is an error, not a silent 1.0.

## Key takeaway

Grain is still one round for GGR. The key is `cid` + `brand_id`. The currency of a cross-brand report is EUR. The table for history is rounds or transactions, never the live balance row.
