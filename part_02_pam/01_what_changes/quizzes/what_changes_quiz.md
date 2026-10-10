# What Changes with PAM Quiz

8 multiple-choice questions. Answers at the bottom.

---

**1.** In this platform, Diger RGS is:

- A) The only source of gameplay rounds
- B) One casino provider adapter among others
- C) The wallet ledger
- D) The backoffice report database

**2.** Seamless wallet means:

- A) The game server stores the player's balance
- B) PAM is the source of truth for balance, and providers call in on each money movement
- C) Deposits are settled once a month
- D) Bonus definitions live in the RGS

**3.** Which table is the wrong source for historical GGR?

- A) game_rounds
- B) transactions
- C) customer_balance
- D) A daily aggregate used only to reconcile

**4.** Bonus definitions (what is on offer) are owned by:

- A) service-offerings
- B) service-communications
- C) service-bo-reports
- D) service-geoip

**5.** Claimed bonus balance is owned by:

- A) service-offerings
- B) service-wallet
- C) service-communications
- D) The provider adapter only

**6.** Redis pub/sub on PAM is a poor warehouse feed because:

- A) It is at-most-once
- B) It stores the full MySQL history
- C) It is the system currency
- D) It replaces cid with email

**7.** Cross-brand revenue should be summed in:

- A) Whatever currency the first player used
- B) EUR, the system currency
- C) Integer cents only
- D) Provider tokens

**8.** service-bo-reports is best used by analytics as:

- A) The feature store
- B) A reconciliation source for aggregates the backoffice already computes
- C) The player login table
- D) The FX rate card

---

## Answers

1. B · 2. B · 3. C · 4. A · 5. B · 6. A · 7. B · 8. B
