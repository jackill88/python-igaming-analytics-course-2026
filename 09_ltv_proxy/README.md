# Module 09: LTV & Value Proxy

Predict future GGR as LTV proxy with RGS-only data

## Learning Objectives

- Predict future GGR as LTV proxy with RGS-only data
- Evaluate regression models for value forecasting
- Communicate limitations vs true financial LTV

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Ltv Definitions | [theory/01_ltv_definitions.md](theory/01_ltv_definitions.md) |
| 2 | Future Ggr Prediction | [theory/02_future_ggr_prediction.md](theory/02_future_ggr_prediction.md) |
| 3 | Proxy Limitations | [theory/03_proxy_limitations.md](theory/03_proxy_limitations.md) |

## Quiz

Test your understanding: [quizzes/ltv_proxy_quiz.md](quizzes/ltv_proxy_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Label Future Ggr | [challenges/label_future_ggr.py](challenges/label_future_ggr.py) |
| Ltv Feature Matrix | [challenges/ltv_feature_matrix.py](challenges/ltv_feature_matrix.py) |
| Train Ltv Model | [challenges/train_ltv_model.py](challenges/train_ltv_model.py) |

Run tests:

```bash
pytest tests/09_ltv_proxy/ -v
```

## Suggested Study Path

1. Read all theory lessons in order
2. Take the quiz
3. Implement challenges and run pytest
