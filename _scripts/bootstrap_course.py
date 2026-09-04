#!/usr/bin/env python3
"""Generate all course modules, challenges, and tests."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Module definitions
# ---------------------------------------------------------------------------

MODULES = [
    {
        "id": "01_igaming_domain",
        "title": "iGaming Domain & RGS Events",
        "objectives": [
            "Explain PAM vs RGS and what analytics is feasible with gameplay-only data",
            "Parse and validate RGS event schemas (player, session, round, bet, win)",
            "Compute GGR (Gross Gaming Revenue) from bet and win amounts",
        ],
        "lessons": [
            ("01_pam_vs_rgs.md", "PAM vs RGS", "Understand the two core iGaming platforms."),
            ("02_rgs_event_schema.md", "RGS Event Schema", "Grain, keys, and fields in gameplay events."),
            ("03_ggr_and_revenue_metrics.md", "GGR and Revenue Metrics", "GGR = bets − wins; what requires PAM data."),
        ],
        "challenges": [
            ("validate_rgs_event.py", '''"""
Challenge: Validate RGS Event
Module 01: iGaming Domain & RGS Events

Run: pytest tests/01_igaming_domain/test_validate_rgs_event.py -v
"""

REQUIRED_FIELDS = {"round_id", "player_id", "session_id", "game_id", "timestamp", "bet_amount", "win_amount"}


def validate_rgs_event(event: dict) -> tuple[bool, list[str]]:
    """Return (is_valid, list_of_error_messages)."""
    pass
'''),
            ("compute_ggr.py", '''"""
Challenge: Compute GGR
Module 01: iGaming Domain & RGS Events

Run: pytest tests/01_igaming_domain/test_compute_ggr.py -v
"""

import pandas as pd


def compute_ggr(df: pd.DataFrame) -> pd.DataFrame:
    """Add column ggr = bet_amount - win_amount. Return copy with ggr column."""
    pass


def total_ggr(df: pd.DataFrame) -> float:
    """Return sum of GGR across all rows."""
    pass
'''),
            ("compute_ggr_by_game.py", '''"""
Challenge: Compute GGR by Game
Module 01: iGaming Domain & RGS Events

Run: pytest tests/01_igaming_domain/test_compute_ggr_by_game.py -v
"""

import pandas as pd


def ggr_by_game(df: pd.DataFrame) -> pd.DataFrame:
    """Return DataFrame with columns game_id, total_bets, total_wins, ggr sorted by ggr desc."""
    pass
'''),
        ],
    },
    {
        "id": "02_engagement_metrics",
        "title": "Engagement Metrics",
        "objectives": [
            "Compute DAU, WAU, and MAU from activity logs",
            "Calculate stickiness (DAU / MAU)",
            "Define active player consistently for reporting",
        ],
        "lessons": [
            ("01_dau_wau_mau.md", "DAU, WAU, MAU", "Daily, weekly, and monthly active users."),
            ("02_stickiness.md", "Stickiness", "How often players return: DAU / MAU."),
            ("03_active_player_definitions.md", "Active Player Definitions", "Bet placed vs login vs round played."),
        ],
        "challenges": [
            ("compute_dau.py", '''"""
Challenge: Compute DAU
Module 02: Engagement Metrics

Run: pytest tests/02_engagement_metrics/test_compute_dau.py -v
"""

import pandas as pd


def daily_active_users(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """
    Count unique player_id with activity_date == as_of.date().
    activity columns: player_id, activity_date
    """
    pass
'''),
            ("compute_wau_mau.py", '''"""
Challenge: Compute WAU and MAU
Module 02: Engagement Metrics

Run: pytest tests/02_engagement_metrics/test_compute_wau_mau.py -v
"""

import pandas as pd


def wau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """Unique players active in [as_of - 6 days, as_of] inclusive."""
    pass


def mau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """Unique players active in [as_of - 29 days, as_of] inclusive."""
    pass
'''),
            ("compute_stickiness.py", '''"""
Challenge: Compute Stickiness
Module 02: Engagement Metrics

Run: pytest tests/02_engagement_metrics/test_compute_stickiness.py -v
"""

import pandas as pd


def stickiness(activity: pd.DataFrame, as_of: pd.Timestamp) -> float:
    """Return DAU / MAU for as_of. Return 0.0 if MAU is 0."""
    pass
'''),
        ],
    },
    {
        "id": "03_cohorts_retention",
        "title": "Cohorts & Retention",
        "objectives": [
            "Build registration cohort tables",
            "Compute D1, D7, D30 retention rates",
            "Interpret cohort retention curves for product decisions",
        ],
        "lessons": [
            ("01_cohort_basics.md", "Cohort Basics", "Group players by registration period."),
            ("02_retention_metrics.md", "Retention Metrics", "D1, D7, D30 and return definitions."),
            ("03_cohort_tables.md", "Cohort Tables", "Building and reading retention matrices."),
        ],
        "challenges": [
            ("assign_cohort.py", '''"""
Challenge: Assign Cohort
Module 03: Cohorts & Retention

Run: pytest tests/03_cohorts_retention/test_assign_cohort.py -v
"""

import pandas as pd


def assign_registration_cohort(players: pd.DataFrame) -> pd.DataFrame:
    """Add cohort_week column (Monday-start week of registration_date). Return copy."""
    pass
'''),
            ("compute_retention.py", '''"""
Challenge: Compute Retention
Module 03: Cohorts & Retention

Run: pytest tests/03_cohorts_retention/test_compute_retention.py -v
"""

import pandas as pd


def d7_retention(players: pd.DataFrame, activity: pd.DataFrame) -> float:
    """
    Fraction of players who had activity exactly 7 days after registration_date.
    Return 0.0 if no players.
    """
    pass
'''),
            ("build_cohort_table.py", '''"""
Challenge: Build Cohort Table
Module 03: Cohorts & Retention

Run: pytest tests/03_cohorts_retention/test_build_cohort_table.py -v
"""

import pandas as pd


def cohort_retention_table(
    players: pd.DataFrame, activity: pd.DataFrame, days: list[int]
) -> pd.DataFrame:
    """
    Return DataFrame: cohort_week x day_offset with retention rate (0-1).
    Index: cohort_week, columns: d{day} for each day in days.
    """
    pass
'''),
        ],
    },
    {
        "id": "04_session_analytics",
        "title": "Session Analytics",
        "objectives": [
            "Sessionize gameplay events with gap thresholds",
            "Compute session length and bets per session",
            "Analyze session patterns for engagement insights",
        ],
        "lessons": [
            ("01_session_definitions.md", "Session Definitions", "RGS session_id vs derived sessions."),
            ("02_sessionization.md", "Sessionization", "Gap-based session assignment."),
            ("03_session_metrics.md", "Session Metrics", "Duration, rounds, GGR per session."),
        ],
        "challenges": [
            ("sessionize_events.py", '''"""
Challenge: Sessionize Events
Module 04: Session Analytics

Run: pytest tests/04_session_analytics/test_sessionize_events.py -v
"""

import pandas as pd


def sessionize_by_gap(events: pd.DataFrame, gap_minutes: int = 30) -> pd.DataFrame:
    """
    Assign derived_session_id per player when gap > gap_minutes.
    Return events copy with derived_session_id (int, starting at 1 per player).
    Sort by player_id, timestamp before processing.
    """
    pass
'''),
            ("session_duration.py", '''"""
Challenge: Session Duration
Module 04: Session Analytics

Run: pytest tests/04_session_analytics/test_session_duration.py -v
"""

import pandas as pd


def session_durations(events: pd.DataFrame) -> pd.DataFrame:
    """
    Using session_id column. Return player_id, session_id, duration_minutes, round_count.
    duration = max(timestamp) - min(timestamp) in minutes.
    """
    pass
'''),
            ("ggr_per_session.py", '''"""
Challenge: GGR per Session
Module 04: Session Analytics

Run: pytest tests/04_session_analytics/test_ggr_per_session.py -v
"""

import pandas as pd


def ggr_per_session(events: pd.DataFrame) -> pd.DataFrame:
    """Return player_id, session_id, total_bets, total_wins, ggr."""
    pass
'''),
        ],
    },
    {
        "id": "05_sql_gaming_analytics",
        "title": "SQL Analytics on Gaming Data",
        "objectives": [
            "Write analytical SQL for top games and player affinity",
            "Use window functions for rolling GGR",
            "Execute SQL with DuckDB against RGS tables",
        ],
        "lessons": [
            ("01_analytical_sql_for_gaming.md", "Analytical SQL for Gaming", "Grain and joins on RGS data."),
            ("02_top_games_and_affinity.md", "Top Games and Affinity", "Rankings and player-game relationships."),
            ("03_window_functions_ggr.md", "Window Functions for GGR", "Rolling sums and running totals."),
        ],
        "challenges": [
            ("top_games_sql.py", '''"""
Challenge: Top Games SQL
Module 05: SQL Analytics on Gaming Data

Run: pytest tests/05_sql_gaming_analytics/test_top_games_sql.py -v
"""


def top_games_by_ggr_sql() -> str:
    """
    Return SQL for top 3 games by total GGR.
    Table: rounds(round_id, player_id, game_id, bet_amount, win_amount, timestamp)
    Columns: game_id, ggr
    """
    pass
'''),
            ("player_favorite_game_sql.py", '''"""
Challenge: Player Favorite Game SQL
Module 05: SQL Analytics on Gaming Data

Run: pytest tests/05_sql_gaming_analytics/test_player_favorite_game_sql.py -v
"""


def player_favorite_game_sql() -> str:
    """
    Return SQL: player_id, favorite_game (most rounds played).
    Table: rounds(round_id, player_id, game_id, bet_amount, win_amount, timestamp)
    Tie-break by game_id ascending.
    """
    pass
'''),
            ("rolling_ggr_sql.py", '''"""
Challenge: Rolling 7-Day GGR SQL
Module 05: SQL Analytics on Gaming Data

Run: pytest tests/05_sql_gaming_analytics/test_rolling_ggr_sql.py -v
"""


def rolling_7d_ggr_sql() -> str:
    """
    Return SQL: activity_date, ggr, rolling_7d_ggr (sum of ggr over 7-day window incl current day).
    Source: daily_ggr(activity_date, ggr)
    Order by activity_date.
    """
    pass
'''),
        ],
    },
    {
        "id": "06_feature_engineering",
        "title": "Feature Engineering",
        "objectives": [
            "Build player_features_daily from RGS events",
            "Compute rolling session and GGR features",
            "Prepare features for ML models",
        ],
        "lessons": [
            ("01_player_features_daily.md", "player_features_daily", "The core feature table pattern."),
            ("02_rolling_windows.md", "Rolling Windows", "7d and 30d behavioral aggregates."),
            ("03_feature_grain_and_leakage.md", "Feature Grain and Leakage", "Point-in-time correctness."),
        ],
        "challenges": [
            ("days_since_last_session.py", '''"""
Challenge: Days Since Last Session
Module 06: Feature Engineering

Run: pytest tests/06_feature_engineering/test_days_since_last_session.py -v
"""

import pandas as pd


def days_since_last_session(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    """
    Return player_id, days_since_last_session for each player active before feature_date.
    If never active, omit player. Days = (feature_date - last_timestamp).days
    """
    pass
'''),
            ("sessions_in_window.py", '''"""
Challenge: Sessions in Window
Module 06: Feature Engineering

Run: pytest tests/06_feature_engineering/test_sessions_in_window.py -v
"""

import pandas as pd


def sessions_7d(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    """Return player_id, sessions_7d counting distinct session_id in last 7 days ending feature_date."""
    pass
'''),
            ("build_player_features.py", '''"""
Challenge: Build Player Features
Module 06: Feature Engineering

Run: pytest tests/06_feature_engineering/test_build_player_features.py -v
"""

import pandas as pd


def build_player_features(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    """
    Return player_id, sessions_7d, avg_bet_7d, ggr_7d, favorite_game_7d
    for players with activity in the 7-day window ending feature_date.
    favorite_game = game with most rounds in window.
    """
    pass
'''),
        ],
    },
    {
        "id": "07_player_segmentation",
        "title": "Player Segmentation",
        "objectives": [
            "Cluster players on behavioral features",
            "Profile and name segments (whales, casuals, churn-risk)",
            "Evaluate segment stability and business utility",
        ],
        "lessons": [
            ("01_segmentation_use_cases.md", "Segmentation Use Cases", "Whales, casuals, bonus hunters."),
            ("02_clustering_algorithms.md", "Clustering Algorithms", "K-Means, GMM, HDBSCAN trade-offs."),
            ("03_segment_profiling.md", "Segment Profiling", "Centroids, lift, and CRM actions."),
        ],
        "challenges": [
            ("prepare_segmentation_features.py", '''"""
Challenge: Prepare Segmentation Features
Module 07: Player Segmentation

Run: pytest tests/07_player_segmentation/test_prepare_segmentation_features.py -v
"""

import pandas as pd


def prepare_features(df: pd.DataFrame, feature_cols: list[str]) -> pd.DataFrame:
    """Return numeric feature matrix; fill NaN with 0; drop non-feature columns."""
    pass
'''),
            ("kmeans_segment.py", '''"""
Challenge: K-Means Segment Players
Module 07: Player Segmentation

Run: pytest tests/07_player_segmentation/test_kmeans_segment.py -v
"""

import pandas as pd


def kmeans_segment(features: pd.DataFrame, n_clusters: int = 3, random_state: int = 42) -> pd.Series:
    """Return Series of cluster labels indexed like features."""
    pass
'''),
            ("profile_segments.py", '''"""
Challenge: Profile Segments
Module 07: Player Segmentation

Run: pytest tests/07_player_segmentation/test_profile_segments.py -v
"""

import pandas as pd


def segment_profile(features: pd.DataFrame, labels: pd.Series) -> pd.DataFrame:
    """Return mean of each numeric column grouped by segment label."""
    pass
'''),
        ],
    },
    {
        "id": "08_churn_prediction",
        "title": "Churn Prediction",
        "objectives": [
            "Label inactive_next_30_days from activity history",
            "Train a gradient boosting churn model",
            "Evaluate with precision/recall and business framing",
        ],
        "lessons": [
            ("01_churn_definition.md", "Churn Definition", "30-day inactivity as target."),
            ("02_churn_features.md", "Churn Features", "Recency, frequency, monetary proxies."),
            ("03_model_training_and_eval.md", "Model Training and Evaluation", "LightGBM, metrics, deployment."),
        ],
        "challenges": [
            ("label_churn.py", '''"""
Challenge: Label Churn Target
Module 08: Churn Prediction

Run: pytest tests/08_churn_prediction/test_label_churn.py -v
"""

import pandas as pd


def label_churn(activity: pd.DataFrame, snapshot_date: pd.Timestamp, horizon_days: int = 30) -> pd.DataFrame:
    """
    For each player active in 30d before snapshot_date, label inactive_next_30_days:
    1 if no activity in (snapshot_date, snapshot_date + horizon_days], else 0.
    Return player_id, inactive_next_30_days.
    """
    pass
'''),
            ("churn_feature_matrix.py", '''"""
Challenge: Churn Feature Matrix
Module 08: Churn Prediction

Run: pytest tests/08_churn_prediction/test_churn_feature_matrix.py -v
"""

import pandas as pd


def build_churn_features(events: pd.DataFrame, snapshot_date: pd.Timestamp) -> pd.DataFrame:
    """
    Return player_id, days_since_last_session, sessions_30d, avg_bet_30d, ggr_30d
    for players with any activity in 30d before snapshot_date.
    """
    pass
'''),
            ("train_churn_model.py", '''"""
Challenge: Train Churn Model
Module 08: Churn Prediction

Run: pytest tests/08_churn_prediction/test_train_churn_model.py -v
"""

import pandas as pd


def train_churn_classifier(
    features: pd.DataFrame,
    labels: pd.Series,
    random_state: int = 42,
):
    """Train LightGBM binary classifier on features (drop player_id). Return fitted model."""
    pass
'''),
        ],
    },
    {
        "id": "09_ltv_proxy",
        "title": "LTV & Value Proxy",
        "objectives": [
            "Predict future GGR as LTV proxy with RGS-only data",
            "Evaluate regression models for value forecasting",
            "Communicate limitations vs true financial LTV",
        ],
        "lessons": [
            ("01_ltv_definitions.md", "LTV Definitions", "True LTV vs GGR-based proxy."),
            ("02_future_ggr_prediction.md", "Future GGR Prediction", "Regression targets from gameplay."),
            ("03_proxy_limitations.md", "Proxy Limitations", "What PAM data would unlock."),
        ],
        "challenges": [
            ("label_future_ggr.py", '''"""
Challenge: Label Future GGR
Module 09: LTV & Value Proxy

Run: pytest tests/09_ltv_proxy/test_label_future_ggr.py -v
"""

import pandas as pd


def label_future_ggr(events: pd.DataFrame, snapshot_date: pd.Timestamp, horizon_days: int = 30) -> pd.DataFrame:
    """
    For players active before snapshot_date, sum GGR in (snapshot_date, snapshot_date + horizon_days].
    Return player_id, future_ggr_30d.
    """
    pass
'''),
            ("ltv_feature_matrix.py", '''"""
Challenge: LTV Feature Matrix
Module 09: LTV & Value Proxy

Run: pytest tests/09_ltv_proxy/test_ltv_feature_matrix.py -v
"""

import pandas as pd


def ltv_features(events: pd.DataFrame, snapshot_date: pd.Timestamp) -> pd.DataFrame:
    """Return player_id, ggr_30d, sessions_30d, avg_bet_30d for players active before snapshot."""
    pass
'''),
            ("train_ltv_model.py", '''"""
Challenge: Train LTV Model
Module 09: LTV & Value Proxy

Run: pytest tests/09_ltv_proxy/test_train_ltv_model.py -v
"""

import pandas as pd


def train_ltv_regressor(features: pd.DataFrame, targets: pd.Series, random_state: int = 42):
    """Train LightGBM regressor. Return fitted model."""
    pass
'''),
        ],
    },
    {
        "id": "10_recommendations",
        "title": "Recommendation Engine",
        "objectives": [
            "Build player-game interaction matrices",
            "Apply collaborative filtering for game recommendations",
            "Evaluate recommendation quality offline",
        ],
        "lessons": [
            ("01_rec_use_cases.md", "Recommendation Use Cases", "Games, categories, providers."),
            ("02_collaborative_filtering.md", "Collaborative Filtering", "User-item matrix factorization."),
            ("03_offline_evaluation.md", "Offline Evaluation", "Hit rate, coverage, diversity."),
        ],
        "challenges": [
            ("player_game_matrix.py", '''"""
Challenge: Player-Game Matrix
Module 10: Recommendation Engine

Run: pytest tests/10_recommendations/test_player_game_matrix.py -v
"""

import pandas as pd


def player_game_matrix(events: pd.DataFrame) -> pd.DataFrame:
    """
    Return pivot: rows=player_id, columns=game_id, values=round_count (number of rounds).
    Fill missing with 0.
    """
    pass
'''),
            ("top_games_per_player.py", '''"""
Challenge: Top Games per Player
Module 10: Recommendation Engine

Run: pytest tests/10_recommendations/test_top_games_per_player.py -v
"""

import pandas as pd


def top_n_games_per_player(events: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Return player_id, rank, game_id sorted by round count descending per player."""
    pass
'''),
            ("recommend_popular_games.py", '''"""
Challenge: Recommend Popular Games
Module 10: Recommendation Engine

Run: pytest tests/10_recommendations/test_recommend_popular_games.py -v
"""

import pandas as pd


def recommend_popular_unplayed(events: pd.DataFrame, player_id: int, n: int = 3) -> list[str]:
    """
    Return top n globally popular games (by round count) the player has NOT played.
    Tie-break by game_id ascending.
    """
    pass
'''),
        ],
    },
    {
        "id": "11_analytics_architecture",
        "title": "Analytics Architecture",
        "objectives": [
            "Design RGS → warehouse → dbt → ML pipeline",
            "Estimate infrastructure costs and feasibility",
            "Know when to add feature store or real-time scoring",
        ],
        "lessons": [
            ("01_rgs_to_warehouse.md", "RGS to Warehouse", "Ingestion, grain, partitioning."),
            ("02_dbt_feature_tables.md", "dbt Feature Tables", "player_features_daily pattern."),
            ("03_batch_vs_realtime_ml.md", "Batch vs Real-Time ML", "When Redis/Feast is worth it."),
            ("04_cost_and_feasibility.md", "Cost and Feasibility", "Stakeholder validation framing."),
        ],
        "challenges": [
            ("estimate_storage.py", '''"""
Challenge: Estimate Storage
Module 11: Analytics Architecture

Run: pytest tests/11_analytics_architecture/test_estimate_storage.py -v
"""


def estimate_daily_storage_gb(
    events_per_day: int,
    bytes_per_event: int = 256,
) -> float:
    """Return estimated GB per day (use 1 GB = 1e9 bytes)."""
    pass
'''),
            ("pipeline_phase_order.py", '''"""
Challenge: Pipeline Phase Order
Module 11: Analytics Architecture

Run: pytest tests/11_analytics_architecture/test_pipeline_phase_order.py -v
"""

RECOMMENDED_PHASES = [
    "warehouse",
    "dbt_features",
    "segmentation_churn_ltv",
    "recommendations",
    "feature_store_eval",
]


def next_phase(completed: list[str]) -> str | None:
    """Return the next recommended phase not yet in completed, or None if all done."""
    pass
'''),
        ],
    },
    {
        "id": "12_summary",
        "title": "Summary & Stakeholder Positioning",
        "objectives": [
            "Frame analytics ROI for iGaming stakeholders",
            "Prioritize use cases with RGS-only constraints",
            "Prepare for Analytics Lead / Applied ML interviews",
        ],
        "lessons": [
            ("01_course_recap.md", "Course Recap", "End-to-end skills covered."),
            ("02_stakeholder_framing.md", "Stakeholder Framing", "Feasibility, cost, ROI."),
            ("03_practice_datasets.md", "Practice Datasets", "Kaggle, Cookie Cats, AWS synthetic."),
            ("04_interview_checklist.md", "Interview Checklist", "Metrics, ML, architecture talking points."),
        ],
        "challenges": [],
    },
]


def quiz_content(module_title: str) -> str:
    return f"""# {module_title} Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** With RGS-only data, which metric is directly computable?

- A) NGR  
- B) ARPU  
- C) GGR  
- D) Bonus cost  

**2.** GGR is defined as:

- A) Deposits minus withdrawals  
- B) Bets minus wins  
- C) Revenue minus taxes  
- D) Wins minus bets  

**3.** DAU counts:

- A) Total bets per day  
- B) Unique active players per day  
- C) New registrations per day  
- D) Sessions per day  

**4.** Stickiness is typically:

- A) WAU / MAU  
- B) DAU / MAU  
- C) DAU / WAU  
- D) MAU / DAU  

**5.** D7 retention measures players who:

- A) Deposit on day 7  
- B) Return 7 days after registration  
- C) Play 7 games  
- D) Win on day 7  

**6.** Churn is often defined as:

- A) One losing session  
- B) 30 days inactive  
- C) Negative GGR  
- D) Account closed  

**7.** player_features_daily should use:

- A) Future data for accuracy  
- B) Point-in-time features only  
- C) PAM wallet balances only  
- D) Real-time Feast only  

**8.** With RGS-only data, LTV models should predict:

- A) True financial LTV  
- B) future_ggr or turnover proxy  
- C) Payment processor fees  
- D) CRM email open rate  

**9.** First ML use case to validate ROI is often:

- A) Real-time feature store  
- B) Churn or segmentation  
- C) Blockchain ledger  
- D) Data catalog only  

**10.** A feature store is recommended when:

- A) Day one of analytics  
- B) Multiple models share features and online inference matters  
- C) You have no warehouse  
- D) Only batch reports needed  

---

## Answers

1. C · 2. B · 3. B · 4. B · 5. B · 6. B · 7. B · 8. B · 9. B · 10. B
"""


def lesson_body(title: str, summary: str) -> str:
    return f"""# {title}

{summary}

## Key concepts

- iGaming analytics starts from **RGS gameplay events** when PAM data is unavailable
- State **grain** (player, session, round) before aggregating
- **GGR = bets − wins** is the primary revenue metric from RGS
- Engagement (DAU/WAU/MAU), retention, and churn build on activity definitions
- ML features belong in warehouse tables like `player_features_daily`
- Validate business value before investing in real-time ML infrastructure

## Example

```python
import pandas as pd

events = pd.DataFrame({{
    "bet_amount": [10.0, 5.0, 20.0],
    "win_amount": [0.0, 15.0, 0.0],
}})
events["ggr"] = events["bet_amount"] - events["win_amount"]
print(events["ggr"].sum())  # GGR = 20.0
```

## Practice

Complete the module challenges and run pytest to verify your implementation.
"""


def readme_content(m: dict) -> str:
    lessons_table = "\n".join(
        f"| {i} | {Path(name).stem.split('_', 1)[1].replace('_', ' ').title()} | [theory/{name}](theory/{name}) |"
        for i, (name, _, _) in enumerate(m["lessons"], 1)
    )
    obj_list = "\n".join(f"- {o}" for o in m["objectives"])
    challenges_section = ""
    if m["challenges"]:
        ch_rows = "\n".join(
            f"| {Path(c[0]).stem.replace('_', ' ').title()} | [challenges/{c[0]}](challenges/{c[0]}) |"
            for c in m["challenges"]
        )
        challenges_section = f"""
## Challenges

| Challenge | File |
|-----------|------|
{ch_rows}

Run tests:

```bash
pytest tests/{m['id']}/ -v
```
"""
    quiz_slug = m["id"].split("_", 1)[1]
    return f"""# Module {m['id'].split('_')[0]}: {m['title']}

{m['objectives'][0]}

## Learning Objectives

{obj_list}

## Lessons

| # | Topic | Theory |
|---|-------|--------|
{lessons_table}

## Quiz

Test your understanding: [quizzes/{quiz_slug}_quiz.md](quizzes/{quiz_slug}_quiz.md)
{challenges_section}
## Suggested Study Path

1. Read all theory lessons in order
2. Take the quiz
3. Implement challenges and run pytest
"""


def generate_modules(*, write_theory: bool = False, write_quizzes: bool = False) -> None:
    """Generate module READMEs and challenge stubs.

    Theory lessons are maintained in ``_scripts/fix_theory.py`` — run that script
    separately so bootstrap does not overwrite module-specific lesson content.

    Quizzes, enriched challenge docstrings, and pytest files are maintained in
    ``_scripts/fix_quizzes_challenges_tests.py`` — run that script separately.
    """
    for m in MODULES:
        mid = m["id"]
        mod_dir = ROOT / mid
        write(mod_dir / "README.md", readme_content(m))
        if write_theory:
            for fname, title, summary in m["lessons"]:
                write(mod_dir / "theory" / fname, lesson_body(title, summary))
        if write_quizzes:
            quiz_slug = mid.split("_", 1)[1]
            write(mod_dir / "quizzes" / f"{quiz_slug}_quiz.md", quiz_content(m["title"]))
        for fname, content in m["challenges"]:
            write(mod_dir / "challenges" / fname, content)


if __name__ == "__main__":
    generate_modules()
    print(f"Generated {len(MODULES)} modules under {ROOT}")
    print("Theory: run python3 _scripts/fix_theory.py to (re)generate lesson markdown.")
    print("Quizzes/challenges/tests: run python3 _scripts/fix_quizzes_challenges_tests.py")
