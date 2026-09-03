# Module 11: Analytics Architecture

Design RGS → warehouse → dbt → ML pipeline

## Learning Objectives

- Design RGS → warehouse → dbt → ML pipeline
- Estimate infrastructure costs and feasibility
- Know when to add feature store or real-time scoring

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Rgs To Warehouse | [theory/01_rgs_to_warehouse.md](theory/01_rgs_to_warehouse.md) |
| 2 | Dbt Feature Tables | [theory/02_dbt_feature_tables.md](theory/02_dbt_feature_tables.md) |
| 3 | Batch Vs Realtime Ml | [theory/03_batch_vs_realtime_ml.md](theory/03_batch_vs_realtime_ml.md) |
| 4 | Cost And Feasibility | [theory/04_cost_and_feasibility.md](theory/04_cost_and_feasibility.md) |

## Quiz

Test your understanding: [quizzes/analytics_architecture_quiz.md](quizzes/analytics_architecture_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Estimate Storage | [challenges/estimate_storage.py](challenges/estimate_storage.py) |
| Pipeline Phase Order | [challenges/pipeline_phase_order.py](challenges/pipeline_phase_order.py) |

Run tests:

```bash
pytest tests/11_analytics_architecture/ -v
```

## Suggested Study Path

1. Read all theory lessons in order
2. Take the quiz
3. Implement challenges and run pytest
