# Service to fact map

Read a PAM metric by asking which service owns the row. Cross-service joins use `cid` (and `brand_id`).

| Service | Owns | Use it for |
|---------|------|------------|
| service-customers | `customers`, `login_sessions`, KYC, self-exclusion | Registration, login activity, account status |
| service-wallet | `transactions`, `customer_balance`, `bonuses_claimed` | Deposits, withdrawals, bet money, claimed bonus cost |
| service-casino | `game_rounds`, `game_sessions`, free rounds, wagering counter | Play activity, stake split, game and provider |
| service-offerings | Bonus definitions (`first_deposit`, `no_deposit`, `retention_bonus`, free spins) | What was offered, not what the player holds |
| service-communications | `messages_sent`, subscription settings | Sends, and whether marketing mail is allowed |
| service-bo-reports | Daily aggregates (gaming, payments, tax, campaigns) | Reconciliation against the warehouse |

`service-bo-users` serves those aggregates to the backoffice. It shares a schema with bo-reports. The split is operational: heavy cron load stays off the interactive path. Analytics does not need a second copy of that cron fleet.

Bonus **definitions** are not bonus **claims**. A catalogue row in offerings can be disabled without telling you how much a player was credited. That credit is a wallet claim. The per-bet turnover counter is casino-local. One business bonus is three tables.

## Key takeaway

Name the owning service before you name the metric. `daily_gaming_activity` is a backoffice aggregate. `game_rounds` is the fact you model from.
