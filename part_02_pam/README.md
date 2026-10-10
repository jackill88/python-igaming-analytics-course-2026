# Chapter 2: PAM analytics

Chapter 1 treats gameplay as an RGS event stream and leaves payments, bonuses, and true revenue for later. This chapter keeps those lessons and changes the source of truth.

Diger PAM is the system of record for players, money, casino rounds, and bonus definitions. Diger RGS is one casino provider adapter, alongside Pragmatic, Ezugi, and O2A. Bet and win **money** is recorded in the wallet. Round and session **metadata** is recorded in the casino service.

## What changes

| Question | Chapter 1 | Chapter 2 |
|----------|-----------|-----------|
| Gameplay grain | RGS round events | `game_rounds` in service-casino; money in wallet `transactions` |
| Player key | `player_id` | numeric `cid`, always with `brand_id` |
| Active user | Played a round | Login, play, and deposit are three different counts |
| Cohort anchor | Registration, else first play | Registration, first play, and first deposit (FTD) |
| Revenue | GGR = bets − wins | GGR still from stakes − wins; NGR subtracts bonus cost, provider fee, and tax, in EUR |
| Bonus hunters | Deferred | Claim cost in the wallet, stake split on the round |
| LTV | Future GGR | Future NGR is available as a label; it is still a forecast |
| Churn | Inactive for 30 days | Keep activity churn; add deposit churn |
| Promotions | Play-history recommendations | Bonus plans exist, and the marketing gate can block the send |
| Pipeline | RGS stream into a warehouse | Replicate PAM MySQL. Redis pub/sub is not a warehouse feed |

`customer_balance` is a mutable row plus an audit log. Historical GGR and NGR come from rounds and transactions, not from the current balance.

`service-bo-reports` already rolls gaming, payments, bonuses, and tax into daily tables for the backoffice. Use those tables to reconcile the warehouse. Do not treat them as the feature store, and do not rebuild them as the first analytics project.

## Modules

| Module | Topic |
|--------|-------|
| [01_what_changes](01_what_changes/README.md) | Services, keys, grain, currency |
| [02_activity_and_cohorts](02_activity_and_cohorts/README.md) | Login, play, deposit, cohort anchors, CRM eligibility |
| [03_wallet_revenue](03_wallet_revenue/README.md) | FTD, paying users, ARPU, ARPPU |
| [04_bonus_and_ngr](04_bonus_and_ngr/README.md) | Bonus owners, NGR, bonus GGR share |
| [05_models_and_pipeline](05_models_and_pipeline/README.md) | Features, labels, warehouse sources |

Sample frames live in `shared/datasets.py` (`pam_customers_frame`, `pam_transactions_frame`, `pam_game_rounds_frame`, `pam_bonus_claims_frame`, `pam_login_sessions_frame`, `pam_fx_rates_frame`). Amounts used for revenue are in EUR, the system currency. Customer-currency amounts stay on the transaction for conversion practice.
