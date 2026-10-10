# Three owners for one bonus

A bonus is not a single table.

| Concern | Owner | Analytics use |
|---------|-------|----------------|
| Definition, eligibility, free-spin config | service-offerings | Which plan existed (`first_deposit`, `no_deposit`, `retention_bonus`, free spins) |
| Claim, bonus balance, expiry, completion | service-wallet | `bonuses_claimed` and the EUR cost of the grant |
| Per-bet turnover and contribution | service-casino | Whether play was burning a wagering requirement; cash vs bonus stake on the round |

Offerings answers "what could this player have been offered". Wallet answers "what were they credited". Casino answers "which bets counted toward wagering". Joining only the catalogue to GGR will mark a player as bonus-driven who never claimed, or miss a claim whose definition was later disabled.

The shared claims are one row each: cid 101 `retention_bonus` 10 EUR, cid 102 `first_deposit` 20 EUR, cid 103 `no_deposit` 30 EUR. Sum claims when a player has more than one.

## Key takeaway

Bonus cost for NGR comes from claims, in EUR. The plan name comes from the definition. The stake split comes from the round.
