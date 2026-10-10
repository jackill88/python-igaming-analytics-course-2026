# ARPU and ARPPU

Chapter 1 could not compute these. The definitions are still easy to misuse, because "revenue" and "user" each need a sentence.

```
ARPU  = revenue_eur / active users
ARPPU = revenue_eur / paying users
```

In this module:

- **revenue_eur** is whatever column you pass (GGR until module 04, NGR after). The functions do not decide the revenue definition. The report does.
- **Active users** are the ids you pass as the active population (play DAU, login MAU, a cohort — pick one and name it).
- **Paying users** are distinct cids with at least one approved deposit in the transaction frame you pass. They are not "active users who paid" unless you filter the frame first.

Empty denominators return 0.0, so a slice with no players does not raise.

Worked numbers, not from a hidden formula: revenue rows of 26, 15, and 30 EUR (sum 71) and four active ids give ARPU 17.75. Three paying users in the shared transaction sample give ARPPU 71/3.

Do not divide deposits by active users and call it ARPU. Deposits are cash in. Casino revenue is GGR or NGR.

## Key takeaway

ARPU without a stated revenue column and a stated activity definition is not a metric. Write both next to the number.
