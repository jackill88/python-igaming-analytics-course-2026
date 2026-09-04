# Python iGaming Analytics Course

A self-paced, test-driven course for **iGaming analytics and applied ML** — RGS gameplay data, player metrics, cohorts, feature engineering, segmentation, churn, LTV proxies, recommendations, and analytics architecture.

## Learning Objectives

After finishing this course, you will be able to:

- Work with RGS event schemas and compute GGR from gameplay data
- Calculate engagement metrics (DAU, WAU, MAU, stickiness) and cohort retention
- Sessionize gameplay events and analyze session-level behavior
- Write analytical SQL for gaming metrics with DuckDB
- Build `player_features_daily` and point-in-time ML features
- Segment players with clustering and train churn / LTV proxy models
- Build offline game recommendation baselines
- Design RGS → warehouse → dbt → ML pipelines and assess feasibility

## Course Structure

| Module | Topic | Challenges |
|--------|-------|------------|
| [01_igaming_domain](01_igaming_domain/README.md) | iGaming Domain & RGS Events | 3 |
| [02_engagement_metrics](02_engagement_metrics/README.md) | Engagement Metrics | 3 |
| [03_cohorts_retention](03_cohorts_retention/README.md) | Cohorts & Retention | 3 |
| [04_session_analytics](04_session_analytics/README.md) | Session Analytics | 3 |
| [05_sql_gaming_analytics](05_sql_gaming_analytics/README.md) | SQL Analytics on Gaming Data | 3 |
| [06_feature_engineering](06_feature_engineering/README.md) | Feature Engineering | 3 |
| [07_player_segmentation](07_player_segmentation/README.md) | Player Segmentation | 3 |
| [08_churn_prediction](08_churn_prediction/README.md) | Churn Prediction | 3 |
| [09_ltv_proxy](09_ltv_proxy/README.md) | LTV & Value Proxy | 3 |
| [10_recommendations](10_recommendations/README.md) | Recommendation Engine | 3 |
| [11_analytics_architecture](11_analytics_architecture/README.md) | Analytics Architecture | 2 |
| [12_summary](12_summary/README.md) | Summary & Stakeholder Positioning | — |

Each module contains:

- **`theory/`** — Markdown lessons with explanations and Python/SQL examples
- **`quizzes/`** — Self-check multiple-choice quizzes
- **`challenges/`** — Python files with empty function stubs for you to implement

Tests live in **`tests/`**, organized by module. One test file per challenge.

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Study a module

Open the module `README.md`, read the theory lessons in order, then attempt the challenges.

### 3. Implement challenges

Each challenge file in `{module}/challenges/` contains function stubs marked with `pass`. Replace them with your solution.

Example workflow for Module 1:

```bash
# Edit: 01_igaming_domain/challenges/compute_ggr.py

# Run tests for one challenge
pytest tests/01_igaming_domain/test_compute_ggr.py -v

# Run all tests for a module
pytest tests/01_igaming_domain/ -v
```

### 4. Track your progress

```bash
# Run the entire test suite
pytest -v
```

When **all tests pass**, you have completed the course.

## Course Navigator App

A Streamlit GUI browses theory lessons, tracks module progress in SQLite, and links to challenges.

```bash
pip install -r requirements-app.txt
streamlit run app/main.py
```

Progress is stored in `data/progress.db` (created on first launch).

### Android app (Flet, offline, theory & quizzes)

An offline Android navigator mirrors the Streamlit UI — browse theory lessons, take **interactive quizzes** (shuffled answers, instant scoring), and track progress locally.

**Prerequisites:** [Flutter SDK](https://docs.flutter.dev/get-started/install/linux) on your `PATH` (e.g. `export PATH="$HOME/flutter/3.44.8/bin:$PATH"`). Run `flet doctor` if the build fails.

```bash
pip install -r requirements-flet.txt

# Development (uses repo course content directly)
flet run flet_app/main.py

# Build APK — run from repo root (requires pyproject.toml)
python flet_app/prepare_assets.py
export PATH="$HOME/flutter/3.44.8/bin:$PATH"   # adjust to your Flutter install
flet build apk
```

The APK is written to `build/apk/`. Progress on a device is stored in the app's private storage.

If you see `Invalid kernel binary format version`, clear stale Dart caches and rebuild:

```bash
rm -rf flet_app/build build
flet build apk
```

## Project Layout

```
.
├── README.md
├── AGENTS.md                 # Domain context and business objectives
├── requirements.txt
├── pytest.ini
├── conftest.py
├── shared/                   # Datasets, DuckDB helpers, test loaders
├── 01_igaming_domain/
│   ├── README.md
│   ├── theory/
│   ├── quizzes/
│   └── challenges/
├── ...
├── tests/
├── app/                      # Streamlit course navigator
├── course_nav/               # Shared discovery + SQLite progress
├── flet_app/                 # Offline Android navigator
└── data/                     # progress.db (created by the app)
```

## How Challenges Work

- **Python / Pandas / ML modules:** Implement the required functions. Signatures and docstrings describe expected behavior.
- **SQL module (05):** Return a SQL string. Tests execute it with **DuckDB** against sample RGS tables.
- **Shared utilities:** Import helpers from `shared` (`shared.datasets`, `shared.sql_helpers`).

Reference solutions for maintainers live in `_scripts/solutions.py` (not required for students).

Regenerate course content:

```bash
python3 _scripts/fix_theory.py                      # theory lessons
python3 _scripts/fix_quizzes_challenges_tests.py    # quizzes, challenges, tests
python3 _scripts/verify_tests.py                    # verify all tests vs solutions
```

## Tech Stack

| Layer | Choice |
|-------|--------|
| Language | Python ≥ 3.10 |
| Testing | pytest |
| Tabular | pandas, pyarrow |
| SQL engine | DuckDB (in-process) |
| ML | scikit-learn, LightGBM |
| Desktop GUI | Streamlit (optional) |
| Mobile GUI | Flet (optional) |

## Practice Datasets

See [12_summary/theory/03_practice_datasets.md](12_summary/theory/03_practice_datasets.md) for external datasets:

- Predict Online Gaming Behavior (Kaggle)
- Cookie Cats (retention / A/B testing)
- Gamelytics Mobile Analytics
- AWS Player Behavior Dataset Generator

## Tips

1. Read the theory lesson before each challenge group.
2. State **grain**, **time domain**, and **RGS vs PAM constraints** before coding.
3. Run `pytest` on a single test file while iterating.
4. Use the quizzes to confirm conceptual understanding.
5. For architecture modules, practice speaking numbers (events/day, retention, SLA) out loud.

## License

Personal learning use. Adapt and extend as you like.
