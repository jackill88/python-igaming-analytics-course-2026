# Bonus GGR share

Rounds in PAM can split the stake into cash and bonus balance. Wins are not tagged by funding source in this teaching table, so attribute GGR in proportion to stake:

```
bonus_ggr_share = bonus_bet_eur / (cash_bet_eur + bonus_bet_eur)
bonus_ggr_eur   = ggr_eur × bonus_ggr_share
```

Sum stakes and GGR per `cid` first, then divide. If total stake is 0, the share is 0.

| cid | Stake | Bonus stake | Share | GGR | Bonus GGR |
|-----|-------|-------------|-------|-----|-----------|
| 101 | 30 | 5 | 5/30 | 26 | 26 × 5/30 |
| 102 | 30 | 10 | 1/3 | 15 | 5 |
| 103 | 40 | 40 | 1 | 30 | 30 |

Cid 103's entire GGR is bonus-funded under this rule. A segmenter that only sees Chapter 1 GGR will call them a whale. A segmenter that sees `bonus_ggr_share` can call them bonus-driven and check NGR before offering more credit.

This share is a stake weight, not a finance ledger. It is good enough to rank players and bad as a journal entry. The claim cost in NGR is the finance number; this ratio explains the GGR.

## Key takeaway

High GGR and high bonus share is the pattern Chapter 1 could not see. Report both.
