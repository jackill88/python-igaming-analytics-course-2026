# Module 03: Wallet Revenue

Deposits, first deposit, and revenue per user once the wallet exists.

## Learning Objectives

- Identify the first approved deposit and ignore open, rejected, and withdrawal rows
- Count paying users from successful deposits
- Compute ARPU and ARPPU from an explicit EUR revenue column

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Deposits And Ftd | [theory/01_deposits_and_ftd.md](theory/01_deposits_and_ftd.md) |
| 2 | Arpu And Arppu | [theory/02_arpu_arppu.md](theory/02_arpu_arppu.md) |

## Quiz

Test your understanding: [quizzes/wallet_revenue_quiz.md](quizzes/wallet_revenue_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| First Deposit | [challenges/first_deposit.py](challenges/first_deposit.py) |
| Paying Users | [challenges/paying_users.py](challenges/paying_users.py) |
| Arpu Arppu | [challenges/arpu_arppu.py](challenges/arpu_arppu.py) |

Run tests:

```bash
pytest tests/part_02_pam/03_wallet_revenue/ -v
```

## Suggested Study Path

1. Read all theory lessons in order
2. Take the quiz
3. Implement challenges and run pytest
