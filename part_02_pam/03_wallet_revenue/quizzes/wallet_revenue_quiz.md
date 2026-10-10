# Wallet Revenue Quiz

8 multiple-choice questions. Answers at the bottom.

---

**1.** A row counts as a successful deposit when:

- A) tx_type is deposit and status is approved
- B) tx_type is deposit, any status
- C) status is approved, any tx_type
- D) amount_eur is positive

**2.** FTD amount is:

- A) The sum of all approved deposits
- B) The amount_eur on the earliest approved deposit
- C) The current customer_balance
- D) The first withdrawal

**3.** Two approved deposits at the same timestamp:

- A) Both become the FTD
- B) The row with the smaller transaction_id is the FTD
- C) The larger amount wins
- D) The player has no FTD

**4.** Paying-user count on the shared sample is:

- A) 5, one per customer
- B) 3, cids with an approved deposit
- C) 1, only EUR wallets
- D) 7, one per transaction

**5.** ARPU in this module divides revenue by:

- A) The active ids the caller supplies
- B) Rows in the FX table
- C) Game rounds
- D) Bonus claims

**6.** ARPPU divides the same revenue by:

- A) Login sessions
- B) Distinct cids with an approved deposit
- C) Brands
- D) Open deposits

**7.** Using deposit totals as ARPU:

- A) Matches GGR by definition
- B) Mixes cash-in with gaming revenue
- C) Is required for NGR
- D) Removes the need for EUR

**8.** An empty active-user list should make ARPU:

- A) Raise ZeroDivisionError
- B) Return 0.0
- C) Return the revenue sum
- D) Return null and skip the test

---

## Answers

1. A · 2. B · 3. B · 4. B · 5. A · 6. B · 7. B · 8. B
