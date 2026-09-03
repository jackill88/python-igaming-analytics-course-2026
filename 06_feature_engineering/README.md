# Module 06: Feature Engineering

Build player_features_daily from RGS events

## Learning Objectives

- Build player_features_daily from RGS events
- Compute rolling session and GGR features
- Prepare features for ML models

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | Player Features Daily | [theory/01_player_features_daily.md](theory/01_player_features_daily.md) |
| 2 | Rolling Windows | [theory/02_rolling_windows.md](theory/02_rolling_windows.md) |
| 3 | Feature Grain And Leakage | [theory/03_feature_grain_and_leakage.md](theory/03_feature_grain_and_leakage.md) |

## Quiz

Test your understanding: [quizzes/feature_engineering_quiz.md](quizzes/feature_engineering_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Days Since Last Session | [challenges/days_since_last_session.py](challenges/days_since_last_session.py) |
| Sessions In Window | [challenges/sessions_in_window.py](challenges/sessions_in_window.py) |
| Build Player Features | [challenges/build_player_features.py](challenges/build_player_features.py) |

Run tests:

```bash
pytest tests/06_feature_engineering/ -v
```

## Suggested Study Path

1. Read all theory lessons in order
2. Take the quiz
3. Implement challenges and run pytest
