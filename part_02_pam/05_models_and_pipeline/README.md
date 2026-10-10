# Module 05: Models and the Pipeline

What to add to the Chapter 1 models, and which PAM table is allowed to feed them.

## Learning Objectives

- Extend a daily player feature row with FTD recency, recent deposits, bonus share, and CRM eligibility
- Label deposit churn without replacing activity churn
- Choose a warehouse source, and refuse the Redis balance push

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Features And Labels | [theory/01_pam_features_and_labels.md](theory/01_pam_features_and_labels.md) |
| 2 | Marketing Gate | [theory/02_marketing_gate_and_nba.md](theory/02_marketing_gate_and_nba.md) |
| 3 | Warehouse Pipeline | [theory/03_warehouse_pipeline.md](theory/03_warehouse_pipeline.md) |

## Quiz

Test your understanding: [quizzes/models_and_pipeline_quiz.md](quizzes/models_and_pipeline_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Pam Player Features | [challenges/pam_player_features.py](challenges/pam_player_features.py) |
| Label Deposit Churn | [challenges/label_deposit_churn.py](challenges/label_deposit_churn.py) |
| Warehouse Source | [challenges/warehouse_source.py](challenges/warehouse_source.py) |

Run tests:

```bash
pytest tests/part_02_pam/05_models_and_pipeline/ -v
```

## Suggested Study Path

1. Read all theory lessons in order
2. Take the quiz
3. Implement challenges and run pytest
