# Module 02: Activity and Cohorts

Login, play, and deposit answer different questions. So do registration and first deposit.

## Learning Objectives

- Count login DAU, play DAU, and deposit DAU as separate populations
- Compute retention from a registration anchor and from a first-deposit anchor
- Drop closed and self-excluded players, and players who cannot receive marketing email, before a CRM rate

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Three Activity Definitions | [theory/01_three_activity_definitions.md](theory/01_three_activity_definitions.md) |
| 2 | Cohort Anchors | [theory/02_cohort_anchors.md](theory/02_cohort_anchors.md) |
| 3 | Crm Eligibility | [theory/03_crm_eligibility.md](theory/03_crm_eligibility.md) |

## Quiz

Test your understanding: [quizzes/activity_and_cohorts_quiz.md](quizzes/activity_and_cohorts_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Activity Counts | [challenges/activity_counts.py](challenges/activity_counts.py) |
| Anchor Retention | [challenges/anchor_retention.py](challenges/anchor_retention.py) |
| Crm Eligible Players | [challenges/crm_eligible_players.py](challenges/crm_eligible_players.py) |

Run tests:

```bash
pytest tests/part_02_pam/02_activity_and_cohorts/ -v
```

## Suggested Study Path

1. Read all theory lessons in order
2. Take the quiz
3. Implement challenges and run pytest
