# Features and labels that PAM adds

Chapter 1 `player_features_daily` stays: sessions, bets, favourite game, gameplay GGR. PAM adds columns. It does not replace the gameplay ones.

| Column | Definition in this module |
|--------|---------------------------|
| `days_since_ftd` | Calendar days from the first approved deposit on or before `feature_date` to `feature_date`. Missing when the player has no such deposit |
| `deposits_30d` | Count of approved deposits on the 30 calendar days ending on `feature_date` (inclusive) |
| `bonus_ggr_share` | Stake-weighted share from module 04, using rounds on or before `feature_date`. 0 when the player has no stake in that window |
| `crm_eligible` | 1 when `status` is `active` and `marketing_email_allowed` is 1, else 0 |

One row per customer. Later rounds must not leak into the row: cid 101's 8 June round is invisible to a 1 June feature date, so that day's bonus share is 0, not 5/30.

**Activity churn** (Chapter 1) remains "no play in the next 30 days". **Deposit churn** is separate: among players with an approved deposit in the 30 days ending on the snapshot, label `no_deposit_next_30_days = 1` when they have no approved deposit in `(snapshot, snapshot + horizon]`. A player can churn from play and still deposit, or the reverse.

**LTV.** The training target can be `future_ngr` over the same horizon you used for `future_ggr`. It is still a forecast. Finance actuals are the summed NGR, not the model output. Call the column expected future NGR when you present it.

## Key takeaway

Add the PAM columns beside the gameplay features. Keep both churn labels. Do not train a single "churn" that mixes inactivity with an empty wallet.
