# NGR from components

Chapter 1 defined NGR in words:

```
NGR = GGR − bonuses − taxes − provider fees − payment costs
```

This chapter computes the first three subtractions that PAM tables support, in EUR. Payment costs stay out of the exercise; they depend on the PSP mix and are not on the round.

```
stake_eur        = cash_bet_eur + bonus_bet_eur
ggr_eur          = stake_eur − win_amount_eur
provider_fee_eur = provider_fee_rate × stake_eur
tax_eur          = tax_rate × ggr_eur
ngr_eur          = ggr_eur − bonus_cost_eur − provider_fee_eur − tax_eur
```

`provider_fee_rate` and `tax_rate` are coefficients you pass in (the backoffice stores provider cost coefficients and tax aggregates; do not invent a statutory rate inside the function). Bonus cost is the sum of claim costs for that cid. A player who only has a claim still appears, with GGR 0.

Shared rounds and claims at fee 0.10 and tax 0.20:

| cid | GGR | Bonus cost | Fee | Tax | NGR |
|-----|-----|------------|-----|-----|-----|
| 101 | 26 | 10 | 3.0 | 5.2 | 7.8 |
| 102 | 15 | 20 | 3.0 | 3.0 | −11 |
| 103 | 30 | 30 | 4.0 | 6.0 | −10 |

Cid 103 looks like the best player on GGR and the worst on NGR next to 101. That is the point of the column.

## Key takeaway

Keep GGR. Add NGR beside it. A negative NGR with a large GGR is a bonus-funded result, not a data bug.
