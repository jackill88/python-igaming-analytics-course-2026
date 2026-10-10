Project Context

The company operates in the iGaming / online casino domain.

Two core platforms:

PAM (Player Account Management)

Customer-facing platform holding:

Player accounts
Registration / KYC
Wallets
Deposits
Withdrawals
Bonuses
VIP levels
CRM campaigns
Promotions
Communication history
RGS (Remote Gaming Server)

Gameplay platform producing events such as:

player_id
session_id
game_id
timestamp
bet_amount
win_amount
round_id

Currently:

The team only has access to RGS data.

Therefore initial analytics and ML work must rely primarily on gameplay events rather than payment/CRM data.

Business Objectives Mentioned

The team is interested in:

Player segmentation algorithms
Churn prediction models
LTV and behavioural models
Next-best-action engines
Personalized gamification
Recommendations for games and promotions
Real-time inference services

Additional comment from stakeholders:

We may not need a dedicated Data Engineer. We need somebody who can validate the roadmap, assess feasibility, estimate infrastructure costs, and determine whether we are solving the right problems.

This suggests they need:

Data Architect
Analytics Lead
Applied ML Consultant

more than a pure Data Engineer.

Key Gaming Metrics Learned
Engagement
DAU

Daily Active Users

Unique players active in a day.

WAU

Weekly Active Users

Unique players active in a 7-day period.

MAU

Monthly Active Users

Unique players active in a 30-day period.

Stickiness
DAU / MAU

Measures how often users return.

Retention
D1 Retention

Returned one day after registration.

D7 Retention

Returned seven days later.

D30 Retention

Returned thirty days later.

Typically analyzed using cohort tables.

Churn

Simple definition:

Player inactive for 30 days

ML target:

inactive_next_30_days

Features:

days_since_last_session
sessions_7d
sessions_30d
avg_bet
favorite_game

Typical models:

XGBoost
LightGBM
CatBoost
Revenue Metrics
ARPU

Average Revenue Per User

Revenue / Active Users
ARPPU

Average Revenue Per Paying User

Revenue / Paying Users

Require PAM/payment data.

LTV

Lifetime Value

Simplified:

LTV = ARPU × Lifetime

With only RGS data, only proxy estimates are possible.

GGR

Gross Gaming Revenue

Most important casino metric.

GGR = Bets - Wins

Can be fully calculated from RGS.

Example:

Bet = $1,000,000
Wins = $940,000

GGR = $60,000
NGR

Net Gaming Revenue

NGR =
GGR
- Bonuses
- Taxes
- Provider Fees
- Payment Costs

Requires PAM/financial data.

What Can Be Built Using Only RGS Data

Immediately feasible:

✅ DAU

✅ WAU

✅ MAU

✅ Stickiness

✅ Cohorts

✅ Retention

✅ Churn

✅ GGR

✅ Session analytics

✅ Game popularity

✅ Behavioural features

✅ Segmentation

✅ Recommendations

Partially feasible:

⚠️ LTV

Not feasible:

❌ ARPU

❌ ARPPU

❌ NGR

without PAM/payment systems.

ML Use Cases
1. Player Segmentation

Features:

days_since_last_session
sessions_30d
avg_bet
favorite_game
ggr_30d

Algorithms:

K-Means
HDBSCAN
Gaussian Mixture

Potential segments:

Whales
Casuals
Weekend players
Bonus hunters
High-volatility players
Churn-risk players
2. Churn Prediction

Most obvious first ML use case.

Features:

sessions_7d
sessions_30d
avg_bet
days_since_last_session

Models:

LightGBM
XGBoost
3. LTV Prediction

Predict:

future_ggr
future_turnover
future_value

rather than true financial LTV if only RGS exists.

4. Recommendation Engine

Recommend:

Games
Categories
Providers
Promotions

Possible approaches:

Collaborative Filtering
Matrix Factorization
LightFM
Two-Tower Models
5. Next Best Action

Examples:

Offer bonus
Suggest game
Trigger CRM campaign
Escalate VIP outreach

Usually requires PAM integration.

6. Personalized Gamification

Examples:

Missions
Challenges
Loyalty progression
Reward suggestions

Usually built after segmentation exists.

Online vs Batch ML
Batch Predictions

Good for:

Churn
Segmentation
LTV

Workflow:

RGS
 ↓
Warehouse
 ↓
Features
 ↓
Nightly Model
 ↓
Predictions Table
 ↓
CRM

No real-time inference required.

Real-Time Predictions

Useful for:

Game recommendations
Next-best-action
Personalized promotions
Responsible gaming alerts

Requires low-latency scoring.

Feature Store Discussion
Recommendation

DO NOT start with Feast or a dedicated Feature Store.

Start with:

RGS
 ↓
Warehouse (Postgres/ClickHouse/Iceberg)
 ↓
dbt Feature Tables
 ↓
ML Models
 ↓
Prediction Tables

Example feature table:

player_features_daily

player_id
feature_date
days_since_last_session
sessions_7d
sessions_30d
avg_bet
favorite_game
ggr_30d
Introduce Feature Store Only If
Multiple models share many features
Online inference becomes critical
Training-serving skew becomes painful
Team size grows

Until then:

dbt + Warehouse + Redis

is likely sufficient.

Suggested Initial Architecture

Phase 1:

RGS
 ↓
Data Warehouse

Phase 2:

dbt Feature Models

Phase 3:

Segmentation
Churn
LTV

Phase 4:

Recommendation Engine

Phase 5:

Evaluate Feature Store
Open Datasets for Practice
Best Options
Predict Online Gaming Behavior (Kaggle)
Segmentation
Churn
Engagement
Cookie Cats
D1/D7 retention
Cohorts
A/B testing
Gamelytics Mobile Analytics
Event analytics
Retention
AWS Player Behavior Dataset Generator
Synthetic gaming telemetry
Closest to RGS event streams
Interview / Stakeholder Positioning

Strong position:

For initial RGS-based use cases, a large ML platform is probably unnecessary. We can derive player features directly in the warehouse, validate business value through segmentation and churn models, and only introduce real-time infrastructure or a feature store once recommendation and next-best-action use cases demonstrate measurable ROI.

This aligns with the stakeholder request to validate feasibility and infrastructure costs rather than simply building technology.