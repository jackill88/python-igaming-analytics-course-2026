# Module 08: Churn Prediction

Label inactive_next_30_days from activity history

## Learning Objectives

- Label inactive_next_30_days from activity history
- Train a gradient boosting churn model
- Evaluate with precision/recall and business framing

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Churn Definition | [theory/01_churn_definition.md](theory/01_churn_definition.md) |
| 2 | Churn Features | [theory/02_churn_features.md](theory/02_churn_features.md) |
| 3 | Model Training And Eval | [theory/03_model_training_and_eval.md](theory/03_model_training_and_eval.md) |

## Quiz

Test your understanding: [quizzes/churn_prediction_quiz.md](quizzes/churn_prediction_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Label Churn | [challenges/label_churn.py](challenges/label_churn.py) |
| Churn Feature Matrix | [challenges/churn_feature_matrix.py](challenges/churn_feature_matrix.py) |
| Train Churn Model | [challenges/train_churn_model.py](challenges/train_churn_model.py) |

Run tests:

```bash
pytest tests/08_churn_prediction/ -v
```

## Suggested Study Path

1. Read all theory lessons in order
2. Take the quiz
3. Implement challenges and run pytest
