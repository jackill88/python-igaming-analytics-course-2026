#!/usr/bin/env python3
"""Write module-specific theory lessons (replaces generic bootstrap placeholders)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LESSONS: dict[str, str] = {
    # ------------------------------------------------------------------ 02
    "02_engagement_metrics/theory/01_dau_wau_mau.md": """\
# DAU, WAU, MAU

Active-user metrics answer: **how many unique players were engaged in a period?**

| Metric | Window | Formula |
|--------|--------|---------|
| **DAU** | 1 day | Unique `player_id` active on date D |
| **WAU** | 7 days | Unique players active in [D−6, D] |
| **MAU** | 30 days | Unique players active in [D−29, D] |

## What counts as "active"?

In iGaming with RGS-only data, common definitions:

- **Played at least one round** (strongest gameplay signal)
- **Had a session** (may include lobby time)
- **Logged in** (requires PAM — not available in this course)

Pick one definition and use it consistently across dashboards.

## SQL pattern (daily activity table)

```sql
SELECT activity_date, COUNT(DISTINCT player_id) AS dau
FROM player_daily_activity
WHERE activity_date = '2024-06-01'
GROUP BY activity_date;
```

## Python pattern

```python
import pandas as pd

def dau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    day = as_of.normalize()
    mask = pd.to_datetime(activity["activity_date"]).dt.normalize() == day
    return activity.loc[mask, "player_id"].nunique()
```

## Key takeaway

Always state **active definition**, **timezone**, and **inclusive window bounds** when reporting DAU/WAU/MAU.
""",
    "02_engagement_metrics/theory/02_stickiness.md": """\
# Stickiness

Stickiness measures **how often users return** within a longer window.

```
Stickiness = DAU / MAU
```

| Stickiness | Interpretation |
|------------|----------------|
| ~0.03 | Players visit ~1 day per month (typical casual app) |
| ~0.10 | Strong daily habit |
| ~0.20+ | Very high-frequency product |

## Why it matters in iGaming

- High stickiness → reliable daily revenue base
- Low stickiness + high MAU → many occasional players (weekend spikes)
- Track stickiness by **cohort** and **game category** for product insight

## Example

```python
stickiness = dau(activity, as_of) / mau(activity, as_of)  # guard MAU=0
```

## Related metrics

- **WAU / MAU** — weekly return rate
- **DAU / WAU** — within-week frequency

## Key takeaway

Stickiness is a **ratio of two active-user metrics** — if you change the active definition, both numerator and denominator must use the same rule.
""",
    "02_engagement_metrics/theory/03_active_player_definitions.md": """\
# Active Player Definitions

Different teams define "active" differently. Misaligned definitions cause conflicting KPIs.

## Common definitions in iGaming

| Definition | Data source | Pros | Cons |
|------------|-------------|------|------|
| Round played | RGS | Objective, revenue-linked | Misses lobby browsers |
| Bet placed | RGS | Revenue-aligned | Excludes free-play |
| Deposit made | PAM | Monetization signal | Ignores existing balance play |
| Login | PAM | Broad reach | Inflates vs real play |

## With RGS-only data

Recommended default: **player with ≥1 round on date D**.

Build a daily spine:

```
player_daily_activity(player_id, activity_date)
```

Populate from `MIN(DATE(timestamp))` per player per day from round-level events.

## Edge cases

- **Cross-midnight sessions** — attribute activity to the date of each round, not session start
- **Timezone** — store UTC, convert to reporting timezone at aggregate time
- **Test accounts** — filter `is_test = false` if flagged in dim_player

## Key takeaway

Document your active definition in the **data catalog** and reuse it for DAU, retention, and churn labels.
""",
    # ------------------------------------------------------------------ 03
    "03_cohorts_retention/theory/01_cohort_basics.md": """\
# Cohort Basics

A **cohort** groups players by a shared start event — usually **registration date** or **first bet date**.

```
Cohort = players who registered in the same week/month
```

## Why cohorts?

Aggregate retention hides whether **newer players behave differently** from older ones. Cohort analysis answers:

- Is D7 retention improving release over release?
- Did a product change help May registrants vs April?

## Assigning cohorts

```python
import pandas as pd

reg = pd.to_datetime(players["registration_date"])
cohort_week = reg - pd.to_timedelta(reg.dt.dayofweek, unit="D")  # Monday start
```

## Cohort types in iGaming

| Cohort anchor | Use case |
|---------------|----------|
| Registration date | Marketing / onboarding quality |
| First deposit date | Monetization (needs PAM) |
| First bet date | Gameplay engagement (RGS) |

## Key takeaway

Pick the cohort anchor that matches the **question** — registration for acquisition quality, first bet for gameplay retention.
""",
    "03_cohorts_retention/theory/02_retention_metrics.md": """\
# Retention Metrics

Retention measures whether players **return after a reference day**.

| Metric | Definition |
|--------|------------|
| **D1** | Active 1 day after registration (or cohort anchor) |
| **D7** | Active 7 days after registration |
| **D30** | Active 30 days after registration |

```
D7 retention = players active on day 7 / cohort size
```

## Return vs survival

- **Return-based (common):** active exactly on day N (or within a window around N)
- **Survival / rolling:** active at any point in days 1–N

State which you use — they produce different numbers.

## SQL sketch

```sql
SELECT
    cohort_week,
    COUNT(DISTINCT player_id) AS cohort_size,
    COUNT(DISTINCT CASE WHEN days_since_reg = 7 THEN player_id END) AS d7_retained
FROM player_cohort_activity
GROUP BY cohort_week;
```

## iGaming benchmarks

Benchmarks vary by market, product, and channel. Use **internal baselines** and **cohort-over-cohort trends** rather than generic industry numbers.

## Key takeaway

Retention is **cohort size in the denominator** and a **precise day/window definition** in the numerator.
""",
    "03_cohorts_retention/theory/03_cohort_tables.md": """\
# Cohort Tables

A cohort retention table is a matrix:

```
              d1    d7    d14   d30
cohort_week
2024-05-01   45%   22%   18%   12%
2024-05-08   48%   25%   20%   ...
```

Rows = cohorts, columns = days since anchor, values = retention rate.

## Building the table

1. Assign each player to a cohort (registration week)
2. For each `(cohort, day_offset)`, count players active on `cohort_date + offset`
3. Divide by cohort size

## Reading the table

- **Horizontal (across columns):** decay curve for one cohort
- **Vertical (down rows):** whether newer cohorts retain better at D7
- **Diagonal:** calendar-time effects (seasonality, campaigns)

## Visualization

Heatmaps highlight improving (darker later cohorts) vs declining retention.

## Warehouse design

Materialize as `mart_cohort_retention(cohort_week, day_offset, retained_players, cohort_size, retention_rate)`.

Refresh nightly from `player_daily_activity`.

## Key takeaway

Cohort tables are the standard product analytics artifact for **onboarding and engagement quality** over time.
""",
    # ------------------------------------------------------------------ 04
    "04_session_analytics/theory/01_session_definitions.md": """\
# Session Definitions

A **session** is a contiguous period of player activity.

## RGS-provided session_id

Many RGS platforms emit `session_id` with each round. Use it when trustworthy.

Validate:

- Sessions don't span implausible durations (e.g. 48 hours)
- `session_id` resets on logout / timeout rules you expect

## Derived sessions (gap-based)

When `session_id` is missing or unreliable:

```
New session when: timestamp - previous_timestamp > gap_threshold
Typical gap: 30 minutes
```

Partition by `player_id`, order by `timestamp`.

## Session grain vs round grain

| Grain | Use for |
|-------|---------|
| Round | GGR, game analytics |
| Session | Engagement duration, bets per visit |

## Key takeaway

Document whether sessions come from **RGS** or **derived logic** — mixing breaks trend comparisons.
""",
    "04_session_analytics/theory/02_sessionization.md": """\
# Sessionization

Sessionization assigns a **session key** to each event using inactivity gaps.

## Algorithm

1. Sort events by `player_id`, `timestamp`
2. Compute gap from previous event (same player)
3. Increment session counter when gap > threshold
4. Assign `derived_session_id`

## SQL approach (window functions)

```sql
SELECT
    *,
    SUM(CASE WHEN gap_minutes > 30 OR gap_minutes IS NULL THEN 1 ELSE 0 END)
        OVER (PARTITION BY player_id ORDER BY timestamp) AS derived_session_id
FROM with_gaps;
```

Where `with_gaps` uses `LAG(timestamp)` to compute gap.

## Python approach

See Module 04 challenge `sessionize_by_gap`.

## Choosing the gap threshold

| Threshold | Effect |
|-----------|--------|
| 15 min | More sessions, shorter duration |
| 30 min | Common default |
| 60 min | Fewer, longer sessions |

Run sensitivity analysis before locking a threshold.

## Key takeaway

Sessionization is a **gaps-and-islands** problem — define timeout and partition key before coding.
""",
    "04_session_analytics/theory/03_session_metrics.md": """\
# Session Metrics

Once sessions are defined, aggregate round-level RGS data to session grain.

## Core session metrics

| Metric | Formula |
|--------|---------|
| Session duration | `max(timestamp) - min(timestamp)` |
| Rounds per session | `COUNT(round_id)` |
| Bets per session | `SUM(bet_amount)` |
| GGR per session | `SUM(bet_amount - win_amount)` |
| Games per session | `COUNT(DISTINCT game_id)` |

## Typical distributions

- **Casual players:** many short sessions, few rounds
- **Whales:** fewer, longer sessions, high GGR
- **Weekend players:** session count spikes Fri–Sun

## Use cases

- Responsible gaming: flag unusually long sessions
- Product: optimize lobby → first bet time
- CRM: trigger re-engagement after short, low-GGR sessions

## Example aggregation

```python
sessions = events.groupby(["player_id", "session_id"]).agg(
    duration_minutes=("timestamp", lambda s: (s.max() - s.min()).total_seconds() / 60),
    round_count=("round_id", "count"),
    ggr=("bet_amount", lambda s: (s - events.loc[s.index, "win_amount"]).sum()),
)
```

## Key takeaway

Session metrics bridge **event-level RGS data** and **behavioral player profiles**.
""",
    # ------------------------------------------------------------------ 05
    "05_sql_gaming_analytics/theory/01_analytical_sql_for_gaming.md": """\
# Analytical SQL for Gaming

RGS data lives in round-level fact tables. Analytical SQL transforms it into product and revenue insights.

## Core tables

```sql
rounds(round_id, player_id, session_id, game_id, timestamp, bet_amount, win_amount)
games(game_id, game_name, category, provider)
players(player_id, registration_date, country)
```

## Grain discipline

Every query should declare grain explicitly:

- One row per round → GGR per round
- One row per player per day → daily activity
- One row per player per game → affinity

## Common patterns

```sql
-- GGR by game
SELECT game_id, SUM(bet_amount - win_amount) AS ggr
FROM rounds
GROUP BY game_id;

-- Top players by turnover
SELECT player_id, SUM(bet_amount) AS turnover
FROM rounds
GROUP BY player_id
ORDER BY turnover DESC
LIMIT 100;
```

## DuckDB in this course

Tests run your SQL strings against in-memory DuckDB with sample DataFrames — same patterns apply to Postgres/ClickHouse in production.

## Key takeaway

State **grain**, **filters** (date range, test accounts), and **join keys** before writing gaming SQL.
""",
    "05_sql_gaming_analytics/theory/02_top_games_and_affinity.md": """\
# Top Games and Affinity

## Game popularity

Rank games by:

- **Round count** — engagement volume
- **Unique players** — reach
- **GGR** — revenue contribution
- **Turnover** (total bets) — handle / liquidity

```sql
SELECT game_id,
       COUNT(*) AS rounds,
       COUNT(DISTINCT player_id) AS unique_players,
       SUM(bet_amount - win_amount) AS ggr
FROM rounds
GROUP BY game_id
ORDER BY ggr DESC;
```

## Player–game affinity

For each player, find **favorite game** = most rounds played (tie-break by `game_id`).

Use `ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY cnt DESC, game_id)`.

## Category mix

Join `games` to analyze slots vs table games per player segment.

## Product actions

- Promote high-GGR games to casual segments
- Cross-sell table games to slots-only players
- Retire low-engagement titles from the lobby

## Key takeaway

Popularity (rounds) and profitability (GGR) **diverge** — optimize for the metric that matches the business goal.
""",
    "05_sql_gaming_analytics/theory/03_window_functions_ggr.md": """\
# Window Functions for GGR

Window functions compute **rolling** and **running** metrics without collapsing rows.

## Rolling 7-day GGR

```sql
SELECT
    activity_date,
    ggr,
    SUM(ggr) OVER (
        ORDER BY activity_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7d_ggr
FROM daily_ggr
ORDER BY activity_date;
```

## Running total by player

```sql
SELECT
    player_id,
    timestamp,
    SUM(bet_amount - win_amount) OVER (
        PARTITION BY player_id
        ORDER BY timestamp
    ) AS cumulative_ggr
FROM rounds;
```

## Lag for session gaps

```sql
LAG(timestamp) OVER (PARTITION BY player_id ORDER BY timestamp) AS prev_ts
```

## Frame clauses

| Frame | Meaning |
|-------|---------|
| `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` | Last 7 days including today |
| `RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW` | Calendar-aware (engine-dependent) |

## Key takeaway

Windows preserve row grain — use them for **trends and running totals**, `GROUP BY` for **snapshots**.
""",
    # ------------------------------------------------------------------ 06
    "06_feature_engineering/theory/01_player_features_daily.md": """\
# player_features_daily

The central feature table for iGaming ML. One row per `(player_id, feature_date)`.

## Recommended columns

```
player_id
feature_date
days_since_last_session
sessions_7d
sessions_30d
avg_bet_7d
avg_bet_30d
ggr_7d
ggr_30d
favorite_game_7d
rounds_7d
```

## Build pattern (dbt-style)

1. Start from `rounds` fact table
2. Filter events with `timestamp < feature_date` (no leakage)
3. Aggregate rolling 7d / 30d windows ending `feature_date - 1 day` or end-of-day policy
4. Join dimension attributes (country, registration_date)

## Why daily grain?

- Batch scoring nightly for CRM
- Aligns with churn labels (inactive next 30 days)
- Easy to audit point-in-time correctness

## Storage

Partition by `feature_date`. Retain 90–365 days depending on model needs.

## Key takeaway

`player_features_daily` is the **contract between analytics and ML** — version and document every column.
""",
    "06_feature_engineering/theory/02_rolling_windows.md": """\
# Rolling Windows

Rolling features capture **recent behavior** for ML and segmentation.

## Common windows

| Window | Features |
|--------|----------|
| 7d | sessions_7d, ggr_7d, avg_bet_7d |
| 30d | sessions_30d, ggr_30d, avg_bet_30d |
| 90d | Longer-term value signals |

## Point-in-time rule

For feature_date = `2024-06-15`:

```
Include events where timestamp ∈ [2024-06-08 00:00, 2024-06-15 23:59:59]
```

Never include events **after** feature_date (label leakage).

## SQL rolling example

```sql
SELECT player_id, feature_date,
       COUNT(DISTINCT session_id) AS sessions_7d
FROM rounds
WHERE timestamp >= feature_date - INTERVAL 6 DAY
  AND timestamp < feature_date + INTERVAL 1 DAY
GROUP BY player_id, feature_date;
```

## Python

Use pandas `rolling` on daily aggregates, or filter-then-aggregate per snapshot date.

## Key takeaway

Rolling windows must use **consistent inclusive/exclusive bounds** across training and scoring.
""",
    "06_feature_engineering/theory/03_feature_grain_and_leakage.md": """\
# Feature Grain and Leakage

**Leakage** = using information from the future to predict the past. It inflates offline metrics and fails in production.

## Common leakage mistakes in iGaming

| Mistake | Fix |
|---------|-----|
| Include same-day rounds when scoring at midnight | Cutoff timestamp policy |
| Use lifetime GGR as a feature | Use GGR only before feature_date |
| Label churn using activity before snapshot | Label uses activity *after* snapshot only |
| Train/test split by random rows | Split by time or player cohort |

## Train / serve skew

Features computed in notebooks differently from dbt SQL → silent production bugs.

**Mitigation:** single source of truth in warehouse; notebooks read the feature table.

## Feature_date semantics

Document:

- Timezone of `feature_date`
- Whether window ends at start-of-day or end-of-day
- Handling of players with zero history (null vs 0)

## Key takeaway

For every feature, ask: **"Would I know this value at scoring time?"** If not, it's leakage.
""",
    # ------------------------------------------------------------------ 07
    "07_player_segmentation/theory/01_segmentation_use_cases.md": """\
# Segmentation Use Cases

Segmentation groups players by **behavior** for targeted product and CRM actions.

## Typical iGaming segments

| Segment | Signals | Action |
|---------|---------|--------|
| Whales | High ggr_30d, frequent sessions | VIP host, exclusive games |
| Casuals | Low bet, occasional play | Onboarding offers |
| Weekend players | Activity Fri–Sun only | Weekend promotions |
| Churn-risk | High days_since_last_session, falling sessions | Win-back campaign |
| Bonus hunters | Needs PAM bonus data | Restrict offers |

## Features for clustering

```
days_since_last_session
sessions_30d
avg_bet_30d
ggr_30d
favorite_game_30d (encoded)
```

## Batch vs rules

- **Rules:** `IF ggr_30d > X THEN whale` — interpretable, brittle
- **Clustering:** data-driven groups — needs profiling and naming

## Key takeaway

Segments are useful when each group gets a **different business action** — avoid segmentation for its own sake.
""",
    "07_player_segmentation/theory/02_clustering_algorithms.md": """\
# Clustering Algorithms

## K-Means

- **Pros:** Fast, simple, scales well
- **Cons:** Assumes spherical clusters; pick K manually
- **Use when:** Rough behavioral groupings, large player base

```python
from sklearn.cluster import KMeans
KMeans(n_clusters=4, random_state=42, n_init=10)
```

## Gaussian Mixture Models (GMM)

- Soft cluster assignments (probability per segment)
- Better for overlapping groups

## HDBSCAN

- Finds arbitrary shapes; auto-estimates cluster count
- Labels noise points as −1
- Slower; great for exploration

## Preprocessing

1. Select numeric features
2. Handle nulls (fill 0 or median)
3. **Standardize** (`StandardScaler`) — critical for K-Means

## Choosing K

- Elbow method (inertia vs K)
- Silhouette score
- Business interpretability of profiles

## Key takeaway

Clustering finds **structure** — you still must **name segments** and validate with domain experts.
""",
    "07_player_segmentation/theory/03_segment_profiling.md": """\
# Segment Profiling

After clustering, profile each segment to make it actionable.

## Profile table

| Segment | Count | avg_ggr_30d | avg_sessions_30d | top_game |
|---------|-------|-------------|------------------|----------|
| 0 | 12k | 450 | 25 | slots_a |
| 1 | 80k | 5 | 2 | roulette_b |

Compute **mean/median** of each feature per cluster.

## Naming segments

Compare centroids to global averages:

- Segment mean GGR >> global → "Whales"
- High days_since_last_session → "Dormant / churn-risk"

## Stability checks

- Re-cluster monthly — do segment sizes drift wildly?
- Track segment migration (player moves whale → casual)

## Export to CRM

```
player_segments(player_id, segment_id, segment_name, scored_at)
```

Refresh nightly or weekly.

## Key takeaway

A segment without a **profile and recommended action** is just an integer label.
""",
    # ------------------------------------------------------------------ 08
    "08_churn_prediction/theory/01_churn_definition.md": """\
# Churn Definition

In iGaming with RGS data, churn is typically **inactivity**, not account closure.

## Standard definition

```
Churned = no gameplay activity for 30 consecutive days
```

## ML label

```
inactive_next_30_days = 1 if no activity in (snapshot_date, snapshot_date + 30 days]
```

Players must be **active in the lookback window** before snapshot to be eligible (existing players, not brand-new).

## Alternative definitions

| Definition | When to use |
|------------|-------------|
| 14-day inactive | Fast-cycle mobile products |
| 60-day inactive | Low-frequency lottery-style |
| Deposit churn | Needs PAM — no deposit in 30d |

## Class imbalance

Churn datasets are often imbalanced (many non-churners). Use:

- `scale_pos_weight` in LightGBM
- Precision@K for top decile
- Calibration for CRM capacity planning

## Key takeaway

Align churn definition with **CRM action window** — if campaigns react at 14 days idle, don't train on 30-day labels.
""",
    "08_churn_prediction/theory/02_churn_features.md": """\
# Churn Features

Strong churn models use **recency, frequency, and monetary proxies** from RGS.

## Core features

| Feature | Signal |
|---------|--------|
| `days_since_last_session` | Recency — top predictor |
| `sessions_7d`, `sessions_30d` | Frequency trend |
| `avg_bet_30d` | Engagement depth |
| `ggr_30d` | Value (can be negative) |
| `favorite_game` | Habit / product stickiness |

## Derived features

- `sessions_7d / sessions_30d` — recent slowdown
- `ggr_7d - ggr_prev_7d` — momentum
- Days since registration — lifecycle stage

## Feature snapshot

All features computed at `snapshot_date` using only prior data.

Join labels from activity **after** snapshot.

## Missing history

New players with <7 days tenure — exclude or use separate model.

## Key takeaway

Churn features are mostly **RFM variants on gameplay** — keep them in `player_features_daily` for reuse.
""",
    "08_churn_prediction/theory/03_model_training_and_eval.md": """\
# Model Training and Evaluation

## Model choice

**LightGBM** or **XGBoost** — handle mixed features, nonlinear patterns, fast training on tabular data.

```python
import lightgbm as lgb

model = lgb.LGBMClassifier(random_state=42)
model.fit(X_train, y_train)
```

## Validation strategy

- **Time-based split:** train on older snapshots, test on recent
- Never random-split rows from the same player across train/test

## Metrics

| Metric | Use |
|--------|-----|
| AUC-ROC | Overall ranking quality |
| Precision@K | Top-K list for CRM calls |
| Recall@K | Coverage of actual churners |
| Calibration | Expected vs actual churn rate in bucket |

## Deployment workflow

```
RGS → warehouse → player_features_daily → nightly score → churn_scores table → CRM
```

Batch is sufficient for most win-back campaigns.

## Key takeaway

Optimize for **CRM capacity** (precision at top decile), not only AUC.
""",
    # ------------------------------------------------------------------ 09
    "09_ltv_proxy/theory/01_ltv_definitions.md": """\
# LTV Definitions

**LTV (Lifetime Value)** = total net revenue expected from a player over their relationship.

## True financial LTV

```
LTV ≈ ARPU × average lifetime
```

Requires PAM: deposits, withdrawals, bonuses, fees → **NGR per player**.

## RGS-only proxy

Without payments data, predict:

- **future_ggr_30d** / **future_ggr_90d**
- **future turnover** (total bets)

These rank players by **expected gameplay value**, not true profit.

## When proxy is enough

- Game recommendation ranking
- Segmentation for gameplay campaigns
- Resource allocation among CRM tiers

## When proxy fails

- Bonus-heavy markets (GGR ≠ NGR)
- Payment-fee-sensitive profitability analysis

## Key takeaway

Call it **expected future GGR**, not LTV, when presenting to finance stakeholders.
""",
    "09_ltv_proxy/theory/02_future_ggr_prediction.md": """\
# Future GGR Prediction

Regression model: features at snapshot → sum of GGR in next N days.

## Label

```python
future_ggr_30d = sum(bet_amount - win_amount) for rounds in (snapshot, snapshot + 30d]
```

## Features

Same as churn: `ggr_30d`, `sessions_30d`, `avg_bet_30d`, tenure, favorite game.

## Model

```python
import lightgbm as lgb

model = lgb.LGBMRegressor(random_state=42)
model.fit(X_train, y_train)
```

## Evaluation

- MAE / RMSE on holdout
- Spearman correlation (ranking quality)
- Decile lift: top decile actual GGR vs bottom

## Use cases

- Prioritize VIP outreach
- Budget allocation by expected value
- Early whale detection

## Key takeaway

LTV proxy models are **ranking tools** — validate that top decile players actually generate more GGR.
""",
    "09_ltv_proxy/theory/03_proxy_limitations.md": """\
# Proxy Limitations

Be explicit about what RGS-based LTV models **cannot** do.

## Missing from RGS

| Factor | Impact |
|--------|--------|
| Bonuses | Overstates value of bonus-driven play |
| Deposits / payment fees | True margin unknown |
| Provider fees | Game-level profitability |
| Taxes & regulatory levies | Market-specific |
| Cross-sell to sportsbook | Needs unified PAM |

## Risk of overconfidence

High-GGR players who only play on bonus credit look valuable in RGS but may be **NGR-negative**.

## Communication template

> "This model ranks players by expected **gameplay GGR**. With PAM integration we can convert to **NGR-based LTV** for finance."

## Roadmap

1. Ship GGR proxy (now)
2. Integrate PAM bonus flags (phase 2)
3. True NGR LTV for finance reporting (phase 3)

## Key takeaway

Transparency about limitations builds trust with stakeholders more than overstating model scope.
""",
    # ------------------------------------------------------------------ 10
    "10_recommendations/theory/01_rec_use_cases.md": """\
# Recommendation Use Cases

## What to recommend in iGaming

- **Games** — primary RGS use case
- **Categories** — slots, table, live dealer
- **Providers** — studio preferences
- **Promotions** — needs PAM / CRM integration

## Signals from RGS

- Play history (player × game matrix)
- Session context (current game, time of day)
- Similar players' preferences (collaborative filtering)

## Placement

- Lobby "Recommended for you"
- Post-session "Try this next"
- Email / push with deep link to game

## Success metrics

- Click-through rate on recommendation
- First bet within 24h of recommendation
- Incremental GGR vs control group

## Key takeaway

Start with **offline evaluation** on historical play — before real-time serving infrastructure.
""",
    "10_recommendations/theory/02_collaborative_filtering.md": """\
# Collaborative Filtering

Recommend items based on **similar users' behavior**.

## User-item matrix

```
           slots_a  roulette_b  blackjack_c
player_1       12          0            3
player_2        0         45            0
player_3        8          2            0
```

Values = round counts or implicit feedback (played = 1).

## Approaches

| Method | Idea |
|--------|------|
| Item-based CF | Similar games played by same users |
| Matrix factorization | Latent taste factors |
| LightFM | Hybrid (optional side features) |
| Popular baseline | Global top games not yet played |

## Cold start

- **New player:** popular games in their country / device
- **New game:** content-based (category, provider, RTP)

## This course baseline

`recommend_popular_unplayed` — strong first baseline before CF.

## Key takeaway

Always benchmark CF against **popularity baseline** — often 80% of the gain for 20% of the complexity.
""",
    "10_recommendations/theory/03_offline_evaluation.md": """\
# Offline Evaluation

Evaluate recommenders on historical data before A/B tests.

## Holdout scheme

Hide last N interactions per player. Train on earlier history. Predict hidden games.

## Metrics

| Metric | Definition |
|--------|------------|
| Hit rate@K | Fraction of users with ≥1 hit in top K |
| MRR | Mean reciprocal rank of first hit |
| Coverage | % of catalog recommended |
| Diversity | Average dissimilarity within list |

## iGaming specifics

- Weight by **GGR contribution** of recommended games, not just clicks
- Penalize recommending games player already plays heavily (unless cross-sell goal)

## Online validation

Run A/B test: control = popularity, treatment = CF model.

Primary KPI: incremental GGR per exposed user.

## Key takeaway

Offline hit rate **does not guarantee** revenue lift — always plan an A/B test.
""",
    # ------------------------------------------------------------------ 11
    "11_analytics_architecture/theory/01_rgs_to_warehouse.md": """\
# RGS to Warehouse

Phase 1 of the analytics stack: reliable ingestion of gameplay events.

## Source: RGS event stream

Fields: `round_id`, `player_id`, `session_id`, `game_id`, `timestamp`, `bet_amount`, `win_amount`.

Delivery: Kafka, Kinesis, webhook batch, or SFTP CSV dumps.

## Target: warehouse fact table

```sql
CREATE TABLE fct_rounds (
    round_id        VARCHAR PRIMARY KEY,
    player_id       BIGINT,
    session_id      VARCHAR,
    game_id         VARCHAR,
    event_ts        TIMESTAMP,   -- UTC
    bet_amount      DECIMAL(18,2),
    win_amount      DECIMAL(18,2),
    ingested_at     TIMESTAMP
);
```

## Design decisions

| Decision | Recommendation |
|----------|----------------|
| Grain | One row per round |
| Partition | `DATE(event_ts)` |
| Dedup key | `round_id` |
| Late data | Allow 24–72h replay window |
| Format | Parquet / Iceberg for lake; native tables for warehouse |

## Ingestion checklist

- Idempotent loads (upsert on `round_id`)
- Schema validation at landing zone
- Dead-letter queue for malformed events
- Row count + GGR sum reconciliation vs RGS daily report

## Key takeaway

Get **round-level facts correct and deduplicated** before building any ML — everything downstream depends on this table.
""",
    "11_analytics_architecture/theory/02_dbt_feature_tables.md": """\
# dbt Feature Tables

Phase 2: transform raw rounds into analytics-ready marts.

## Layering

```
stg_rgs_rounds        -- clean, rename, cast
int_player_daily      -- daily aggregates per player
mart_player_features  -- player_features_daily for ML
mart_cohort_retention -- reporting
```

## Example dbt model: player_features_daily

```sql
-- models/mart/player_features_daily.sql
SELECT
    player_id,
    {{ var('feature_date') }} AS feature_date,
    DATE_DIFF('day', MAX(timestamp), {{ var('feature_date') }}) AS days_since_last_session,
    COUNT(DISTINCT session_id) AS sessions_30d,
    AVG(bet_amount) AS avg_bet_30d,
    SUM(bet_amount - win_amount) AS ggr_30d
FROM {{ ref('stg_rgs_rounds') }}
WHERE timestamp >= {{ var('feature_date') }} - INTERVAL 30 DAY
  AND timestamp < {{ var('feature_date') }}
GROUP BY player_id
```

## Testing in dbt

- `unique(player_id, feature_date)`
- `not_null` on key columns
- Referential integrity to `dim_player`

## Why dbt before Feast

Single transformation layer shared by BI and ML. Add feature store only when online serving requires it.

## Key takeaway

dbt models are **versioned, tested SQL** — the right first "feature platform" for iGaming analytics.
""",
    "11_analytics_architecture/theory/03_batch_vs_realtime_ml.md": """\
# Batch vs Real-Time ML

## Batch predictions (start here)

**Use for:** churn, segmentation, LTV proxy, daily game rec lists

```
Nightly: features → model → predictions table → CRM export
```

Latency: hours. Infrastructure: warehouse + Python job + cron/Airflow.

## Real-time predictions

**Use for:** in-session game recommendations, responsible gaming alerts, dynamic lobby

```
Event → feature lookup (Redis) → model API → response < 100ms
```

Requires: online feature serving, model API, monitoring.

## Decision matrix

| Question | Batch | Real-time |
|----------|-------|-----------|
| Action waits for user session? | No | Yes |
| Features change second-by-second? | Rarely | Often |
| CRM email next morning OK? | Yes | — |

## Recommended path

1. Batch churn + segmentation (prove ROI)
2. Batch recommendations in email/lobby tile
3. Evaluate real-time only if in-session lift justifies cost

## Key takeaway

**Do not** start with a feature store or real-time inference — validate use cases in batch first.
""",
    "11_analytics_architecture/theory/04_cost_and_feasibility.md": """\
# Cost and Feasibility

Stakeholders need **numbers**, not architecture diagrams alone.

## Storage estimate

```
daily_GB = events_per_day × bytes_per_event / 1e9
```

Example: 10M rounds/day × 256 bytes ≈ **2.56 GB/day** ≈ 77 GB/month raw.

Add 3× for warehouse indexes, aggregates, and backups.

## Compute estimate

| Workload | Order of magnitude |
|----------|-------------------|
| Daily dbt run | Minutes on warehouse |
| Nightly ML score (1M players) | Single VM / small K8s job |
| Real-time API | Always-on pods + Redis |

## Headcount

For RGS-only analytics MVP:

- 1 analytics engineer (dbt + pipelines)
- 0.5 ML engineer (churn + segmentation)
- No dedicated DE if scope stays batch

## Feasibility gates

| Gate | Criterion |
|------|-----------|
| Phase 1 | GGR + DAU dashboards trusted by ops |
| Phase 2 | Churn model beats random at P@10% |
| Phase 3 | Recommendation A/B shows GGR lift |
| Phase 4 | Real-time ROI > infra cost |

## Key takeaway

Your role is to **validate the roadmap and estimate cost** — not to over-build infrastructure on day one.
""",
}


def main() -> None:
    for rel_path, content in LESSONS.items():
        path = ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"Wrote {rel_path}")
    print(f"\nUpdated {len(LESSONS)} theory lessons.")


if __name__ == "__main__":
    main()
