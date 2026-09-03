# Module 01: iGaming Domain & RGS Events

Explain PAM vs RGS and what analytics is feasible with gameplay-only data

## Learning Objectives

- Explain PAM vs RGS and what analytics is feasible with gameplay-only data
- Parse and validate RGS event schemas (player, session, round, bet, win)
- Compute GGR (Gross Gaming Revenue) from bet and win amounts

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Pam Vs Rgs | [theory/01_pam_vs_rgs.md](theory/01_pam_vs_rgs.md) |
| 2 | Rgs Event Schema | [theory/02_rgs_event_schema.md](theory/02_rgs_event_schema.md) |
| 3 | Ggr And Revenue Metrics | [theory/03_ggr_and_revenue_metrics.md](theory/03_ggr_and_revenue_metrics.md) |

## Quiz

Test your understanding: [quizzes/igaming_domain_quiz.md](quizzes/igaming_domain_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Validate Rgs Event | [challenges/validate_rgs_event.py](challenges/validate_rgs_event.py) |
| Compute Ggr | [challenges/compute_ggr.py](challenges/compute_ggr.py) |
| Compute Ggr By Game | [challenges/compute_ggr_by_game.py](challenges/compute_ggr_by_game.py) |

Run tests:

```bash
pytest tests/01_igaming_domain/ -v
```

## Suggested Study Path

1. Read all theory lessons in order
2. Take the quiz
3. Implement challenges and run pytest
