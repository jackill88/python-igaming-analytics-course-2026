# Deposits and first deposit

A wallet transaction is not automatically revenue and not automatically a deposit.

| Column | Values that matter here |
|--------|-------------------------|
| `tx_type` | `deposit` or `withdrawal` |
| `status` | `approved` is success; `open` is in flight; `rejected` failed |
| `amount` | Customer currency |
| `amount_eur` | System-currency mirror, already converted |
| `created_at` | Event time |

**First deposit (FTD)** is the earliest `created_at` among rows with `tx_type = deposit` and `status = approved`. The EUR amount on that row is the FTD amount, not the sum of later deposits. If two approved deposits share a timestamp, keep the smaller `transaction_id`.

On the shared sample:

| cid | FTD time | FTD amount EUR | Why others drop |
|-----|----------|----------------|-----------------|
| 101 | 2024-05-02 | 117.0 | Later approved deposit, an open deposit, and a withdrawal |
| 102 | 2024-05-20 | 80.0 | Only one approved deposit |
| 103 | 2024-05-16 | 46.8 | Only one approved deposit |
| 105 | — | — | The only deposit is rejected |

Paying users are the distinct `cid` values in that approved-deposit set. The sample has three.

Withdrawals change cash position. They are not negative deposits in this definition, and they do not create an FTD.

## Key takeaway

Say "approved deposit" when you mean money that landed. An initiated deposit inflates funnels and must not inflate ARPPU.
