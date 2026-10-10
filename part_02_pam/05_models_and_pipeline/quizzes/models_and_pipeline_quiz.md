# Models and the Pipeline Quiz

8 multiple-choice questions. Answers at the bottom.

---

**1.** days_since_ftd is missing when:

- A) The player has no approved deposit on or before the feature date
- B) The player is in brand_b
- C) GGR is negative
- D) They logged in that day

**2.** deposits_30d counts:

- A) Approved deposits in the 30-day window ending on the feature date
- B) All transaction types in that window
- C) Rounds
- D) Logins

**3.** A round after feature_date:

- A) Still updates bonus_ggr_share for that feature date
- B) Is excluded from that feature row
- C) Sets crm_eligible to 0
- D) Becomes the FTD

**4.** Deposit churn labels players who:

- A) Have never logged in
- B) Deposited recently and then have no approved deposit in the forward window
- C) Have zero GGR ever
- D) Failed KYC

**5.** Activity churn and deposit churn:

- A) Must be the same label
- B) Answer different questions and both can exist
- C) Require a feature store
- D) Replace NGR

**6.** A retention_bonus action is valid only if:

- A) The player fails the marketing gate
- B) The player passes the marketing gate
- C) Redis delivered a balance event
- D) bo-reports has finished its cron

**7.** The warehouse should ingest historical GGR from:

- A) game_rounds
- B) The Redis balance push
- C) customer_balance
- D) Email templates

**8.** bo-reports aggregates are for:

- A) Training features in place of rounds
- B) Reconciliation against warehouse facts
- C) Replacing Solitics
- D) Real-time scoring

---

## Answers

1. A · 2. A · 3. B · 4. B · 5. B · 6. B · 7. A · 8. B
