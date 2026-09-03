# Practice Datasets

Use these open datasets to extend your practice beyond the in-repo synthetic RGS samples.

## 1. Predict Online Gaming Behavior (Kaggle)

**Best for:** Segmentation, churn, engagement modeling

- Player behavioral features
- Classification targets (e.g. churn-like labels)
- Good first ML project after Module 08

## 2. Cookie Cats (Mobile gaming)

**Best for:** D1/D7 retention, cohort analysis, A/B testing

- Classic mobile game retention dataset
- Gate removal experiment
- Pairs well with Module 03 (cohorts)

## 3. Gamelytics Mobile Analytics

**Best for:** Event analytics, retention funnels

- Event-level mobile game data
- Session and level progression patterns

## 4. AWS Player Behavior Dataset Generator

**Best for:** Synthetic gaming telemetry closest to RGS event streams

- Configurable player behavior simulation
- Useful when you need volume for pipeline testing
- Closest to real RGS event structure in this list

## How to use them with this course

| Course module | Suggested external dataset |
|---------------|---------------------------|
| 02 Engagement | Gamelytics daily activity |
| 03 Cohorts | Cookie Cats |
| 06 Features | AWS Player Behavior Generator |
| 07 Segmentation | Kaggle Predict Online Gaming Behavior |
| 08 Churn | Kaggle Predict Online Gaming Behavior |
| 10 Recommendations | AWS Player Behavior Generator |

## Synthetic in-repo data

The `shared/datasets.py` module provides:

- `rgs_events_frame()` — core round-level events
- `players_frame()` — registration dates for cohorts
- `daily_activity_frame()` — engagement metrics
- `player_rounds_extended_frame()` — larger sample for ML modules

Run challenges against these first, then scale up with external datasets.
