# Module 01: What Changes with PAM

Map PAM services to analytical facts, and choose a historical source that is not the live balance.

## Learning Objectives

- Name which PAM service owns identity, money, rounds, bonus definitions, messages, and backoffice aggregates
- Keep `cid` and `brand_id` together, and convert customer currency to EUR with a supplied rate
- Refuse a mutable balance snapshot as the source of historical GGR

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | From Rgs To Pam | [theory/01_from_rgs_to_pam.md](theory/01_from_rgs_to_pam.md) |
| 2 | Service To Fact Map | [theory/02_service_to_fact_map.md](theory/02_service_to_fact_map.md) |
| 3 | Keys Grain Currency | [theory/03_keys_grain_currency.md](theory/03_keys_grain_currency.md) |

## Quiz

Test your understanding: [quizzes/what_changes_quiz.md](quizzes/what_changes_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Classify Metric Source | [challenges/classify_metric_source.py](challenges/classify_metric_source.py) |
| Historical Ggr Source | [challenges/historical_ggr_source.py](challenges/historical_ggr_source.py) |
| Convert To Eur | [challenges/convert_to_eur.py](challenges/convert_to_eur.py) |

Run tests:

```bash
pytest tests/part_02_pam/01_what_changes/ -v
```

## Suggested Study Path

1. Read all theory lessons in order
2. Take the quiz
3. Implement challenges and run pytest
