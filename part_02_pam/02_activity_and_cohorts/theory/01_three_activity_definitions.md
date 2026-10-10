# Three activity definitions

Chapter 1 DAU counts players who appear in gameplay events. PAM can count three populations on the same calendar day:

| Definition | Fact | Question it answers |
|------------|------|---------------------|
| Login | `login_sessions.login_at` | Who authenticated |
| Play | `game_rounds.event_ts` | Who settled a round |
| Deposit | wallet `transactions` with `tx_type = deposit` and `status = approved` | Who successfully funded the wallet |

An open or rejected deposit is not a deposit for this count. A withdrawal is not a deposit. A login without a round is not play.

On the shared sample, 2024-06-01 has two logins (cid 101 and 102), one playing cid (101, round `r3`), and one approved deposit (cid 101, transaction `t2`). Reporting a single "DAU" hides that split.

Use the same rule inside a week or a month: unique `cid` with at least one qualifying event in the window. Keep the definition in the metric name (`login_dau`, `play_dau`, `deposit_dau`).

## Key takeaway

Stickiness and retention inherit this choice. A login cohort will look healthier than a play cohort. Say which one you computed.
