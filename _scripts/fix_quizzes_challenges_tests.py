#!/usr/bin/env python3
"""Generate module-specific quizzes, enriched challenge stubs, and pytest files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Quizzes — 12 module-specific MCQ sets (10 questions each)
# ---------------------------------------------------------------------------

QUIZZES: dict[str, str] = {
    "01_igaming_domain/quizzes/igaming_domain_quiz.md": """\
# iGaming Domain & RGS Events Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** PAM (Player Account Management) primarily holds:

- A) Round-level bet and win events  
- B) Wallets, KYC, deposits, and bonuses  
- C) Game server RNG seeds  
- D) Provider RTP configuration  

**2.** RGS (Remote Gaming Server) data is best described as:

- A) CRM campaign history  
- B) Gameplay events at round/session grain  
- C) Payment processor settlements  
- D) Marketing attribution logs  

**3.** With RGS-only access, which revenue metric is directly computable?

- A) NGR  
- B) ARPU  
- C) GGR  
- D) Bonus cost  

**4.** GGR (Gross Gaming Revenue) is defined as:

- A) Deposits minus withdrawals  
- B) Bets minus wins  
- C) Revenue minus taxes  
- D) Wins minus bets  

**5.** Which field uniquely identifies a single gameplay round?

- A) session_id  
- B) player_id  
- C) round_id  
- D) game_id  

**6.** NGR differs from GGR because NGR also subtracts:

- A) Player session count  
- B) Bonuses, taxes, and provider fees  
- C) Win amounts only  
- D) Duplicate round_ids  

**7.** The typical grain of an RGS event stream is:

- A) One row per player per month  
- B) One row per round (bet/win)  
- C) One row per deposit  
- D) One row per marketing channel  

**8.** A negative GGR on a single round means:

- A) The player won more than they bet on that round  
- B) The bet_amount field is missing  
- C) The round was voided  
- D) The player churned  

**9.** ARPPU requires data from:

- A) RGS only  
- B) PAM / payment systems  
- C) Game provider APIs only  
- D) Session logs only  

**10.** Before aggregating RGS events, you should first define:

- A) CRM email templates  
- B) Grain (player, session, round) and keys  
- C) VIP tier colors  
- D) App store ranking  

---

## Answers

1. B · 2. B · 3. C · 4. B · 5. C · 6. B · 7. B · 8. A · 9. B · 10. B
""",
    "02_engagement_metrics/quizzes/engagement_metrics_quiz.md": """\
# Engagement Metrics Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** DAU (Daily Active Users) counts:

- A) Total bets placed on a day  
- B) Unique active players on a calendar day  
- C) New registrations on a day  
- D) Total session duration in hours  

**2.** WAU uses an inclusive window of:

- A) 1 day ending on as_of  
- B) 7 days: [as_of − 6 days, as_of]  
- C) 30 days: [as_of − 29 days, as_of]  
- D) Calendar week (Monday–Sunday) regardless of as_of  

**3.** MAU uses an inclusive window of:

- A) 7 days  
- B) 14 days  
- C) 30 days: [as_of − 29 days, as_of]  
- D) Calendar month only  

**4.** Stickiness is typically defined as:

- A) WAU / MAU  
- B) DAU / MAU  
- C) DAU / WAU  
- D) MAU / DAU  

**5.** With RGS-only data, the recommended default "active" definition is:

- A) Player logged in (PAM)  
- B) Player made a deposit  
- C) Player played at least one round  
- D) Player opened the app  

**6.** If MAU = 0, stickiness should:

- A) Raise an error  
- B) Return 0.0  
- C) Return infinity  
- D) Default to 1.0  

**7.** Cross-midnight sessions should attribute activity to:

- A) The session start date only  
- B) The date of each round/event  
- C) UTC week number  
- D) Registration cohort week  

**8.** WAU / MAU measures:

- A) Daily return within a month  
- B) Weekly return within a month  
- C) Monthly return within a year  
- D) Bet frequency per session  

**9.** When reporting DAU/WAU/MAU you must document:

- A) Only the chart color scheme  
- B) Active definition, timezone, and inclusive window bounds  
- C) Provider contract terms  
- D) Player email domains  

**10.** A player active on Mon, Wed, and Fri in the same week contributes how many times to WAU?

- A) 3  
- B) 1  
- C) 7  
- D) 0  

---

## Answers

1. B · 2. B · 3. C · 4. B · 5. C · 6. B · 7. B · 8. B · 9. B · 10. B
""",
    "03_cohorts_retention/quizzes/cohorts_retention_quiz.md": """\
# Cohorts & Retention Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** A registration cohort groups players by:

- A) Favorite game  
- B) Shared registration period (e.g. week of signup)  
- C) Current VIP level  
- D) Last deposit amount  

**2.** D7 retention measures players who:

- A) Deposit on day 7  
- B) Return exactly 7 days after registration  
- C) Play 7 different games  
- D) Win on day 7  

**3.** Cohort analysis is preferred over aggregate retention because:

- A) It requires less data  
- B) It reveals whether newer cohorts behave differently  
- C) It eliminates seasonality entirely  
- D) It replaces the need for DAU  

**4.** A cohort retention table typically has:

- A) Rows = games, columns = providers  
- B) Rows = cohort periods, columns = day offsets (d1, d7, …)  
- C) Rows = players, columns = bet amounts  
- D) Rows = sessions, columns = timestamps  

**5.** Retention rates in cohort tables are usually expressed as:

- A) Absolute player counts only  
- B) Fraction or percentage of the original cohort  
- C) GGR per player  
- D) Session duration in minutes  

**6.** Monday-start cohort weeks are common because:

- A) All casinos register players on Mondays  
- B) They align with weekly reporting calendars  
- C) RGS timestamps are always UTC Mondays  
- D) D7 retention requires Monday registration  

**7.** D1 retention is most sensitive to:

- A) Year-end tax reporting  
- B) First-session experience and onboarding  
- C) Provider fee changes  
- D) Warehouse storage costs  

**8.** If a cohort has zero players, its retention rate should be:

- A) 1.0  
- B) Undefined / 0.0 with guard  
- C) The MAU value  
- D) Negative  

**9.** First-bet cohorts differ from registration cohorts when:

- A) Players register but delay first play  
- B) All players bet on registration day  
- C) PAM is unavailable  
- D) GGR is negative  

**10.** Improving D7 retention without improving D30 suggests:

- A) Long-term engagement still weak  
- B) Permanent product-market fit  
- C) No need for further analysis  
- D) Churn labels are invalid  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. B · 6. B · 7. B · 8. B · 9. A · 10. A
""",
    "04_session_analytics/quizzes/session_analytics_quiz.md": """\
# Session Analytics Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** RGS `session_id` differs from derived sessions because:

- A) RGS sessions are always 30 minutes  
- B) Derived sessions are recomputed from event gaps  
- C) RGS sessions ignore player_id  
- D) Derived sessions require PAM data  

**2.** Gap-based sessionization splits a session when:

- A) The player changes game_id  
- B) Time between consecutive events exceeds a threshold  
- C) GGR turns negative  
- D) round_id duplicates appear  

**3.** Session duration is typically computed as:

- A) Sum of bet amounts  
- B) max(timestamp) − min(timestamp) within the session  
- C) Count of unique game_ids  
- D) Registration date minus first bet  

**4.** A 30-minute gap threshold means a 31-minute pause:

- A) Continues the same session  
- B) Starts a new derived session  
- C) Deletes the events  
- D) Merges two players  

**5.** GGR per session aggregates:

- A) Only win amounts  
- B) Sum(bet_amount) − sum(win_amount) per session  
- C) Average bet across all players  
- D) Deposits minus withdrawals  

**6.** Before sessionization, events should be sorted by:

- A) game_id, then round_id  
- B) player_id, then timestamp  
- C) bet_amount descending  
- D) Random shuffle  

**7.** `derived_session_id` usually:

- A) Resets to 1 for each player  
- B) Is globally unique across all players  
- C) Matches round_id  
- D) Comes from PAM  

**8.** A single-round session has duration:

- A) Always 30 minutes  
- B) Zero minutes (max equals min)  
- C) Undefined  
- D) Equal to average bet  

**9.** Session metrics help answer:

- A) Which provider has the lowest fee  
- B) How long and how intensely players engage per visit  
- C) Tax jurisdiction per player  
- D) Email open rates  

**10.** Using RGS session_id vs derived sessions requires:

- A) Documenting which definition powers each dashboard  
- B) Always preferring PAM login sessions  
- C) Ignoring timestamp ordering  
- D) Dropping round_id  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. B · 6. B · 7. A · 8. B · 9. B · 10. A
""",
    "05_sql_gaming_analytics/quizzes/sql_gaming_analytics_quiz.md": """\
# SQL Analytics on Gaming Data Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** The grain of `rounds(round_id, player_id, game_id, …)` is:

- A) One row per player per day  
- B) One row per round  
- C) One row per session summary  
- D) One row per game catalog entry  

**2.** Top games by GGR in SQL typically use:

- A) `SUM(bet_amount - win_amount) GROUP BY game_id`  
- B) `COUNT(DISTINCT player_id)` only  
- C) `MAX(win_amount)`  
- D) `AVG(deposit_amount)`  

**3.** Player favorite game by round count should break ties by:

- A) Highest GGR first, then random  
- B) game_id ascending (deterministic tie-break)  
- C) Latest timestamp only  
- D) Alphabetical player_id  

**4.** `ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY cnt DESC, game_id ASC)` assigns:

- A) The same rank to all games  
- B) Rank 1 to the most-played game per player  
- C) Global game popularity  
- D) Session duration  

**5.** A rolling 7-day GGR window with `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` includes:

- A) 6 days total  
- B) 7 days including the current row  
- C) 8 days excluding the current row  
- D) Only future days  

**6.** DuckDB is useful in this course because:

- A) It replaces the RGS entirely  
- B) It runs analytical SQL in-memory against pandas DataFrames  
- C) It requires a dedicated cluster  
- D) It only supports NoSQL  

**7.** When joining rounds to a game catalog, use:

- A) player_id  
- B) game_id  
- C) round_id  
- D) session_id  

**8.** Filtering `WHERE activity_date BETWEEN …` before aggregating helps:

- A) Increase storage costs  
- B) Reduce scanned data and improve performance  
- C) Eliminate the need for indexes  
- D) Convert GGR to NGR  

**9.** Window functions differ from `GROUP BY` because:

- A) They remove all row detail  
- B) They can compute running/rolling metrics while keeping row grain  
- C) They only work on strings  
- D) They require PAM data  

**10.** SQL for player-game affinity often starts with:

- A) `SELECT * FROM bonuses`  
- B) Counting rounds or bets per (player_id, game_id)  
- C) Deleting duplicate sessions  
- D) Importing CRM emails  

---

## Answers

1. B · 2. A · 3. B · 4. B · 5. B · 6. B · 7. B · 8. B · 9. B · 10. B
""",
    "06_feature_engineering/quizzes/feature_engineering_quiz.md": """\
# Feature Engineering Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** `player_features_daily` is typically keyed by:

- A) (game_id, feature_date)  
- B) (player_id, feature_date)  
- C) (session_id, round_id)  
- D) (country, month)  

**2.** `days_since_last_session` on snapshot date D should use events:

- A) After D for accuracy  
- B) Strictly before D (point-in-time)  
- C) From the next 30 days  
- D) From PAM wallet history only  

**3.** `sessions_7d` counts:

- A) Total rounds in 7 days  
- B) Distinct session_id in the 7-day window ending on feature_date  
- C) Deposits in 7 days  
- D) Unique game_ids ever played  

**4.** Feature leakage occurs when:

- A) Features use only past data  
- B) Future information influences training labels or features  
- C) NaN values are filled with zero  
- D) player_id is dropped before training  

**5.** A 7-day rolling window ending on 2024-06-03 inclusive spans:

- A) 2024-05-28 through 2024-06-03  
- B) 2024-06-03 through 2024-06-10  
- C) Only 2024-06-03  
- D) The full calendar month  

**6.** `favorite_game_7d` is typically the game with:

- A) Highest single win  
- B) Most rounds in the feature window  
- C) Lowest RTP  
- D) First alphabetically regardless of play  

**7.** `avg_bet_7d` should aggregate:

- A) win_amount only  
- B) mean of bet_amount in the window  
- C) max deposit  
- D) count of players  

**8.** Point-in-time correctness matters most for:

- A) Static game catalog exports  
- B) ML training and nightly batch scoring  
- C) Logo placement on dashboards  
- D) Provider contract PDFs  

**9.** Filling NaN with 0 in feature matrices is:

- A) Always wrong  
- B) A simple baseline when missing means "no activity"  
- C) Equivalent to leakage  
- D) Required for SQL only  

**10.** Before adding a feature store, the recommended pattern is:

- A) Feast on day one  
- B) dbt feature tables in the warehouse  
- C) Spreadsheets emailed nightly  
- D) Real-time Kafka only  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. A · 6. B · 7. B · 8. B · 9. B · 10. B
""",
    "07_player_segmentation/quizzes/player_segmentation_quiz.md": """\
# Player Segmentation Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** Segmentation on RGS data commonly identifies:

- A) Payment processor latency tiers  
- B) Whales, casuals, and churn-risk players  
- C) Tax jurisdictions  
- D) Email domain clusters  

**2.** K-Means requires you to specify:

- A) Only the random seed  
- B) The number of clusters k  
- C) The churn horizon  
- D) Provider fee schedule  

**3.** HDBSCAN is useful when:

- A) You want exactly 3 clusters always  
- B) Cluster count is unknown and noise points exist  
- C) Data has no numeric columns  
- D) You need SQL window functions  

**4.** Before clustering, numeric features should typically be:

- A) Left on different scales without transformation  
- B) Scaled or standardized when magnitudes differ widely  
- C) Converted to player emails  
- D) Dropped entirely  

**5.** Segment profiling computes:

- A) Mean/median of features per cluster label  
- B) Global DAU only  
- C) Provider RTP tables  
- D) Deposit limits  

**6.** A "whale" segment in iGaming usually shows:

- A) Zero sessions and zero GGR  
- B) High GGR and high average bet  
- C) Only bonus-driven play with no rounds  
- D) Negative player_id values  

**7.** `random_state=42` in K-Means ensures:

- A) Different results every run  
- B) Reproducible cluster assignments for the same data  
- C) Automatic optimal k  
- D) Removal of outliers  

**8.** Segmentation outputs feed CRM when:

- A) Segments are interpretable and stable enough to act on  
- B) k equals the number of games  
- C) All players are in one cluster  
- D) Features include future GGR  

**9.** GMM (Gaussian Mixture) differs from K-Means by:

- A) Producing soft cluster probabilities  
- B) Requiring no numeric input  
- C) Only working on categorical data  
- D) Ignoring variance  

**10.** With RGS-only data, segmentation features often include:

- A) Wallet balance and bonus abuse score from PAM  
- B) sessions_30d, avg_bet, ggr_30d, days_since_last_session  
- C) Email click-through rate  
- D) Withdrawal processor ID  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. A · 6. B · 7. B · 8. A · 9. A · 10. B
""",
    "08_churn_prediction/quizzes/churn_prediction_quiz.md": """\
# Churn Prediction Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** A common iGaming churn definition is:

- A) One losing session  
- B) 30 consecutive days without activity  
- C) Negative lifetime GGR  
- D) Account closed in PAM only  

**2.** The ML target `inactive_next_30_days` means:

- A) Player was inactive in the past 30 days  
- B) No activity in the 30 days after the snapshot date  
- C) Player deleted the app yesterday  
- D) GGR was zero on snapshot day  

**3.** Churn features should be computed using data:

- A) Up to and including the snapshot date only  
- B) From the entire future horizon  
- C) From CRM emails sent after snapshot  
- D) From next month's deposits  

**4.** LightGBM/XGBoost are popular for churn because:

- A) They require no features  
- B) They handle tabular heterogeneous features well  
- C) They only work on text  
- D) They output SQL directly  

**5.** `days_since_last_session` is a:

- A) Recency feature  
- B) Provider fee  
- C) Game category label  
- D) Warehouse partition key  

**6.** Precision at top 10% is useful when:

- A) CRM budget limits who you can contact  
- B) You must contact every player  
- C) You have unlimited outreach capacity  
- D) Labels are all zeros  

**7.** Training labels need players who:

- A) Were active in the lookback window before snapshot  
- B) Registered after the snapshot  
- C) Never placed a bet  
- D) Only appear in PAM  

**8.** Class imbalance in churn often leads to:

- A) Always predicting "not churn" with high accuracy but low value  
- B) Perfect recall without effort  
- C) No need for evaluation metrics  
- D) Elimination of feature engineering  

**9.** A churn model deployed nightly typically scores:

- A) Real-time every bet  
- B) Batch predictions into a table for CRM  
- C) Only historical cohorts  
- D) Provider invoices  

**10.** RGS-only churn models cannot directly use:

- A) sessions_30d  
- B) avg_bet_30d  
- C) Deposit frequency and bonus usage  
- D) days_since_last_session  

---

## Answers

1. B · 2. B · 3. A · 4. B · 5. A · 6. A · 7. A · 8. A · 9. B · 10. C
""",
    "09_ltv_proxy/quizzes/ltv_proxy_quiz.md": """\
# LTV & Value Proxy Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** True financial LTV typically requires:

- A) RGS rounds only  
- B) PAM revenue, bonuses, and costs  
- C) Session duration only  
- D) Game thumbnails  

**2.** With RGS-only data, the practical LTV proxy target is:

- A) future_ggr or future turnover  
- B) Exact NGR after tax  
- C) Payment processor fee  
- D) CRM email LTV  

**3.** `future_ggr_30d` labels sum GGR:

- A) Before the snapshot date  
- B) In the period after snapshot through the horizon  
- C) Across all historical time  
- D) From bonus ledger entries  

**4.** LTV regression differs from churn classification because:

- A) It predicts a continuous value  
- B) It never uses gameplay features  
- C) It requires deep learning only  
- D) It ignores player_id grain  

**5.** A player with high past GGR but zero future activity illustrates:

- A) Why past-only features may not predict future value  
- B) Perfect LTV accuracy  
- C) That labels are unnecessary  
- D) PAM integration is automatic  

**6.** LightGBM regressor is appropriate when:

- A) Target is binary churn  
- B) Target is numeric future GGR  
- C) No numeric features exist  
- D) You need SQL parsing  

**7.** Communicating LTV proxy limitations means stating:

- A) It equals audited financial LTV  
- B) It excludes bonuses, tax, and payment costs  
- C) It replaces finance entirely  
- D) It requires no caveats  

**8.** Point-in-time LTV features use history:

- A) Up to snapshot date  
- B) Including the entire future horizon  
- C) From next week's campaigns  
- D) From other operators  

**9.** Negative future GGR in the label window means:

- A) Player won more than they bet in that future window  
- B) Data is always invalid  
- C) The model must classify instead  
- D) round_id is duplicated  

**10.** Stakeholders often accept GGR-based LTV proxies when:

- A) PAM integration is not yet available  
- B) They need exact NGR on day one  
- C) No gameplay data exists  
- D) Only emails are tracked  

---

## Answers

1. B · 2. A · 3. B · 4. A · 5. A · 6. B · 7. B · 8. A · 9. A · 10. A
""",
    "10_recommendations/quizzes/recommendations_quiz.md": """\
# Recommendation Engine Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** A player-game matrix has:

- A) Rows = games, columns = providers  
- B) Rows = players, columns = games, values = interaction strength  
- C) Rows = deposits, columns = withdrawals  
- D) Rows = cohorts, columns = retention days  

**2.** Collaborative filtering recommends items based on:

- A) Only item metadata tags  
- B) Similarity of player interaction patterns  
- C) Random number generation  
- D) Tax jurisdiction  

**3.** A popularity baseline recommends games:

- A) Never played by anyone  
- B) With highest global round counts among unplayed candidates  
- C) Alphabetically first always  
- D) From PAM bonus history only  

**4.** Tie-breaking by `game_id` ascending ensures:

- A) Non-deterministic results  
- B) Reproducible rankings when counts tie  
- C) Higher GGR always  
- D) More clusters in K-Means  

**5.** Offline evaluation metrics include:

- A) Hit rate, coverage, and diversity  
- B) Warehouse disk RPM only  
- C) Provider contract length  
- D) KYC completion rate  

**6.** Recommendations for games the player already played heavily should be:

- A) Always top-ranked  
- B) Deprioritized for discovery use cases  
- C) Excluded from the matrix entirely  
- D) Required by GDPR  

**7.** Matrix factorization (e.g. LightFM) is useful when:

- A) You need implicit feedback from round counts  
- B) You have no player-item interactions  
- C) Only one game exists  
- D) SQL window functions fail  

**8.** Real-time game recommendations require:

- A) Batch-only nightly CSV exports  
- B) Low-latency scoring infrastructure  
- C) No event stream  
- D) PAM-only data  

**9.** `top_n_games_per_player` ranks by:

- A) Round count per (player, game) descending  
- B) Registration date  
- C) Withdrawal amount  
- D) Session_id lexicographic order  

**10.** Cold-start for a new player with no history often falls back to:

- A) Personalized CF from similar players only  
- B) Global popularity or content-based defaults  
- C) Empty recommendations forever  
- D) Churn model scores  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. A · 6. B · 7. A · 8. B · 9. A · 10. B
""",
    "11_analytics_architecture/quizzes/analytics_architecture_quiz.md": """\
# Analytics Architecture Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** Phase 1 of the recommended analytics roadmap is:

- A) Feature store evaluation  
- B) Warehouse ingestion from RGS  
- C) Real-time recommendation API  
- D) Blockchain audit trail  

**2.** dbt feature tables sit between:

- A) CRM and email SMTP  
- B) Raw warehouse tables and ML models  
- C) Game servers and players  
- D) Tax authority and regulator  

**3.** Batch nightly ML scoring is sufficient for:

- A) In-session game recommendations at bet time  
- B) Churn and segmentation CRM lists  
- C) Sub-millisecond fraud on every click  
- D) Live dealer video streaming  

**4.** A feature store (e.g. Feast) is justified when:

- A) Day one of analytics with one report  
- B) Multiple models share features and online inference matters  
- C) No warehouse exists  
- D) Only static PDFs are needed  

**5.** Daily storage estimate uses:

- A) events_per_day × bytes_per_event / 1e9 GB  
- B) MAU × DAU  
- C) GGR × tax rate  
- D) Cluster count × k  

**6.** Redis is often paired with batch ML when:

- A) Low-latency serving of precomputed scores is needed  
- B) Replacing the warehouse entirely  
- C) Storing raw video  
- D) Eliminating dbt  

**7.** Training-serving skew happens when:

- A) Training and production features are computed differently  
- B) Models use the same SQL in both paths  
- C) player_id is consistent  
- D) Random seed is fixed  

**8.** For RGS-only MVP, headcount often includes:

- A) 10 dedicated data engineers day one  
- B) 1 analytics engineer + fractional ML support  
- C) No analytics roles  
- D) Only frontend designers  

**9.** Feasibility gate for Phase 2 ML might require:

- A) Churn model beats random at precision@k  
- B) Unlimited CRM budget proof  
- C) PAM integration complete  
- D) Feature store in production  

**10.** The stakeholder ask to "validate roadmap and cost" means:

- A) Build every tool immediately  
- B) Prove business value before scaling infrastructure  
- C) Skip metrics entirely  
- D) Outsource all modeling  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. A · 6. A · 7. A · 8. B · 9. A · 10. B
""",
    "12_summary/quizzes/summary_quiz.md": """\
# Summary & Stakeholder Positioning Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** With RGS-only data, the team can immediately build:

- A) NGR dashboards  
- B) GGR, DAU, retention, churn, and segmentation  
- C) ARPPU reporting  
- D) Bonus cost allocation  

**2.** The strongest first ML use case to validate ROI is often:

- A) Real-time feature store  
- B) Churn prediction or player segmentation  
- C) Blockchain ledger  
- D) Data catalog only  

**3.** When pitching to stakeholders, lead with:

- A) Tool brand names  
- B) Feasibility, cost estimate, and business metric impact  
- C) Cluster algorithm math only  
- D) Number of Jupyter notebooks  

**4.** Cookie Cats dataset is useful for practicing:

- A) Payment reconciliation  
- B) Mobile retention and A/B testing concepts  
- C) Provider RTP certification  
- D) KYC document parsing  

**5.** AWS Player Behavior Dataset Generator resembles:

- A) CRM email logs  
- B) Synthetic gaming telemetry close to RGS streams  
- C) Tax filings  
- D) App store reviews  

**6.** A GGR-based LTV proxy should be communicated as:

- A) Identical to finance LTV  
- B) Directional value estimate until PAM data arrives  
- C) Not useful ever  
- D) Replacement for cohort analysis  

**7.** Interview talking points should connect:

- A) Metrics → features → models → architecture trade-offs  
- B) Only favorite Python libraries  
- C) Only marketing slogans  
- D) Unrelated hobby projects  

**8.** Over-building real-time ML before proving batch value risks:

- A) Nothing — cost never matters  
- B) High infra cost without demonstrated ROI  
- C) Lower cloud bills automatically  
- D) Eliminating the need for metrics  

**9.** `player_features_daily` in dbt exemplifies:

- A) Skipping the warehouse  
- B) Reusable feature layer before ML  
- C) PAM-only architecture  
- D) Avoiding point-in-time rules  

**10.** The course's core positioning for an Analytics Lead role is:

- A) Deploy Feast on day one  
- B) Validate problems, estimate cost, deliver RGS-based value incrementally  
- C) Ignore business stakeholders  
- D) Focus only on table game rules  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. B · 6. B · 7. A · 8. B · 9. B · 10. B
""",
}


# ---------------------------------------------------------------------------
# Challenges — 32 enriched stubs (pass bodies, rich module docstrings)
# ---------------------------------------------------------------------------

CHALLENGES: dict[str, str] = {
    "01_igaming_domain/challenges/validate_rgs_event.py": '''\
"""
Challenge: Validate RGS Event
Module 01: iGaming Domain & RGS Events

Theory: theory/02_rgs_event_schema.md

Inputs:
  event — dict with round-level RGS fields

Outputs:
  (is_valid, list_of_error_messages) — True and [] when valid

Edge cases:
  - Missing any required field → error per field
  - Negative bet_amount or win_amount → validation error

Example:
  >>> validate_rgs_event({"round_id": "r1", "player_id": 1, ...})
  (True, [])

Run: pytest tests/01_igaming_domain/test_validate_rgs_event.py -v
"""

REQUIRED_FIELDS = {"round_id", "player_id", "session_id", "game_id", "timestamp", "bet_amount", "win_amount"}


def validate_rgs_event(event: dict) -> tuple[bool, list[str]]:
    """Return (is_valid, list_of_error_messages)."""
    pass
''',
    "01_igaming_domain/challenges/compute_ggr.py": '''\
"""
Challenge: Compute GGR
Module 01: iGaming Domain & RGS Events

Theory: theory/03_ggr_and_revenue_metrics.md

Inputs:
  df — DataFrame with bet_amount, win_amount columns

Outputs:
  compute_ggr — copy of df with ggr column (bet − win)
  total_ggr — scalar sum of GGR across all rows

Edge cases:
  - Preserve original columns; do not mutate input
  - Wins exceeding bets yield negative per-row GGR

Example:
  >>> total_ggr(rgs_events)  # shared sample total is -4.0

Run: pytest tests/01_igaming_domain/test_compute_ggr.py -v
"""

import pandas as pd


def compute_ggr(df: pd.DataFrame) -> pd.DataFrame:
    """Add column ggr = bet_amount - win_amount. Return copy with ggr column."""
    pass


def total_ggr(df: pd.DataFrame) -> float:
    """Return sum of GGR across all rows."""
    pass
''',
    "01_igaming_domain/challenges/compute_ggr_by_game.py": '''\
"""
Challenge: Compute GGR by Game
Module 01: iGaming Domain & RGS Events

Theory: theory/03_ggr_and_revenue_metrics.md

Inputs:
  df — RGS events with game_id, bet_amount, win_amount

Outputs:
  DataFrame: game_id, total_bets, total_wins, ggr — sorted by ggr descending

Edge cases:
  - Multiple games; roulette_b is top game in shared sample (ggr=60.0)
  - Empty input → empty result with correct columns

Example:
  >>> ggr_by_game(events).iloc[0]["game_id"]
  'roulette_b'

Run: pytest tests/01_igaming_domain/test_compute_ggr_by_game.py -v
"""

import pandas as pd


def ggr_by_game(df: pd.DataFrame) -> pd.DataFrame:
    """Return DataFrame with columns game_id, total_bets, total_wins, ggr sorted by ggr desc."""
    pass
''',
    "02_engagement_metrics/challenges/compute_dau.py": '''\
"""
Challenge: Compute DAU
Module 02: Engagement Metrics

Theory: theory/01_dau_wau_mau.md

Inputs:
  activity — player_id, activity_date
  as_of — snapshot timestamp (compare normalized calendar date)

Outputs:
  int — count of unique player_id active on as_of date

Edge cases:
  - Multiple rows per player on same day count once
  - No activity on date → 0

Example:
  >>> daily_active_users(activity, pd.Timestamp("2024-06-01"))
  2

Run: pytest tests/02_engagement_metrics/test_compute_dau.py -v
"""

import pandas as pd


def daily_active_users(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """
    Count unique player_id with activity_date == as_of.date().
    activity columns: player_id, activity_date
    """
    pass
''',
    "02_engagement_metrics/challenges/compute_wau_mau.py": '''\
"""
Challenge: Compute WAU and MAU
Module 02: Engagement Metrics

Theory: theory/01_dau_wau_mau.md

Inputs:
  activity — player_id, activity_date
  as_of — end of rolling window (inclusive)

Outputs:
  wau — unique players in [as_of − 6d, as_of]
  mau — unique players in [as_of − 29d, as_of]

Edge cases:
  - Inclusive bounds on both ends
  - Shared sample: wau(as_of=2024-06-05) == 4

Example:
  >>> wau(daily_activity, pd.Timestamp("2024-06-05"))
  4

Run: pytest tests/02_engagement_metrics/test_compute_wau_mau.py -v
"""

import pandas as pd


def wau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """Unique players active in [as_of - 6 days, as_of] inclusive."""
    pass


def mau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    """Unique players active in [as_of - 29 days, as_of] inclusive."""
    pass
''',
    "02_engagement_metrics/challenges/compute_stickiness.py": '''\
"""
Challenge: Compute Stickiness
Module 02: Engagement Metrics

Theory: theory/02_stickiness.md

Inputs:
  activity — player_id, activity_date
  as_of — date for DAU numerator and MAU denominator

Outputs:
  float — DAU / MAU; 0.0 when MAU is 0

Edge cases:
  - Guard division by zero
  - Shared sample: stickiness on 2024-06-05 == 0.25 (DAU=1, MAU=4)

Example:
  >>> stickiness(activity, pd.Timestamp("2024-06-05"))
  0.25

Run: pytest tests/02_engagement_metrics/test_compute_stickiness.py -v
"""

import pandas as pd


def stickiness(activity: pd.DataFrame, as_of: pd.Timestamp) -> float:
    """Return DAU / MAU for as_of. Return 0.0 if MAU is 0."""
    pass
''',
    "03_cohorts_retention/challenges/assign_cohort.py": '''\
"""
Challenge: Assign Cohort
Module 03: Cohorts & Retention

Theory: theory/01_cohort_basics.md

Inputs:
  players — player_id, registration_date

Outputs:
  Copy with cohort_week — Monday-start week of registration_date

Edge cases:
  - Wednesday registration maps to preceding Monday
  - Preserve all original columns

Example:
  >>> assign_registration_cohort(players).loc[players.player_id==101, "cohort_week"].iloc[0]
  Timestamp('2024-04-29')

Run: pytest tests/03_cohorts_retention/test_assign_cohort.py -v
"""

import pandas as pd


def assign_registration_cohort(players: pd.DataFrame) -> pd.DataFrame:
    """Add cohort_week column (Monday-start week of registration_date). Return copy."""
    pass
''',
    "03_cohorts_retention/challenges/compute_retention.py": '''\
"""
Challenge: Compute Retention
Module 03: Cohorts & Retention

Theory: theory/02_retention_metrics.md

Inputs:
  players — player_id, registration_date
  activity — player_id, activity_date

Outputs:
  float — fraction with activity exactly 7 days after registration_date

Edge cases:
  - Empty players → 0.0
  - Compare normalized calendar dates

Example:
  >>> d7_retention(players_frame(), daily_activity_frame())
  0.0

Run: pytest tests/03_cohorts_retention/test_compute_retention.py -v
"""

import pandas as pd


def d7_retention(players: pd.DataFrame, activity: pd.DataFrame) -> float:
    """
    Fraction of players who had activity exactly 7 days after registration_date.
    Return 0.0 if no players.
    """
    pass
''',
    "03_cohorts_retention/challenges/build_cohort_table.py": '''\
"""
Challenge: Build Cohort Table
Module 03: Cohorts & Retention

Theory: theory/03_cohort_tables.md

Inputs:
  players — player_id, registration_date
  activity — player_id, activity_date
  days — list of offsets (e.g. [1, 7, 30])

Outputs:
  DataFrame indexed by cohort_week, columns d{day} with retention rates 0–1

Edge cases:
  - Cohort size denominator is players in that registration week
  - Empty cohort → 0.0 rates

Example:
  >>> table = cohort_retention_table(players, activity, [1, 7])
  >>> "d7" in table.columns

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
''',
    "04_session_analytics/challenges/sessionize_events.py": '''\
"""
Challenge: Sessionize Events
Module 04: Session Analytics

Theory: theory/02_sessionization.md

Inputs:
  events — player_id, timestamp (and other RGS columns)
  gap_minutes — split threshold (default 30)

Outputs:
  events copy with derived_session_id — int starting at 1 per player

Edge cases:
  - Sort by player_id, timestamp before processing
  - Gap > threshold starts new session (exactly 30 min does NOT split)
  - Player 102 has 2 derived sessions in shared sample

Example:
  >>> out = sessionize_by_gap(events, gap_minutes=30)
  >>> out[out.player_id == 102]["derived_session_id"].nunique()
  2

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
''',
    "04_session_analytics/challenges/session_duration.py": '''\
"""
Challenge: Session Duration
Module 04: Session Analytics

Theory: theory/03_session_metrics.md

Inputs:
  events — player_id, session_id, timestamp, round_id

Outputs:
  player_id, session_id, duration_minutes, round_count

Edge cases:
  - Single-event session → duration 0.0
  - Player 101 session s1 → 35.0 minutes, 3 rounds in shared sample

Example:
  >>> session_durations(events).query("player_id==101 and session_id=='s1'")
  duration_minutes=35.0, round_count=3

Run: pytest tests/04_session_analytics/test_session_duration.py -v
"""

import pandas as pd


def session_durations(events: pd.DataFrame) -> pd.DataFrame:
    """
    Using session_id column. Return player_id, session_id, duration_minutes, round_count.
    duration = max(timestamp) - min(timestamp) in minutes.
    """
    pass
''',
    "04_session_analytics/challenges/ggr_per_session.py": '''\
"""
Challenge: GGR per Session
Module 04: Session Analytics

Theory: theory/03_session_metrics.md

Inputs:
  events — player_id, session_id, bet_amount, win_amount

Outputs:
  player_id, session_id, total_bets, total_wins, ggr

Edge cases:
  - Aggregate all rounds within session
  - Player 101 s1 → ggr=20.0 in shared sample

Example:
  >>> ggr_per_session(events).query("player_id==101")["ggr"].iloc[0]
  20.0

Run: pytest tests/04_session_analytics/test_ggr_per_session.py -v
"""

import pandas as pd


def ggr_per_session(events: pd.DataFrame) -> pd.DataFrame:
    """Return player_id, session_id, total_bets, total_wins, ggr."""
    pass
''',
    "05_sql_gaming_analytics/challenges/top_games_sql.py": '''\
"""
Challenge: Top Games SQL
Module 05: SQL Analytics on Gaming Data

Theory: theory/02_top_games_and_affinity.md

Inputs:
  None — return SQL string only

Outputs:
  SQL returning game_id, ggr for top 3 games by total GGR

Edge cases:
  - Table: rounds(round_id, player_id, game_id, bet_amount, win_amount, timestamp)
  - Order by ggr DESC; LIMIT 3

Example:
  >>> query_duckdb(top_games_by_ggr_sql(), {"rounds": events})
  first row: roulette_b, ggr=60.0

Run: pytest tests/05_sql_gaming_analytics/test_top_games_sql.py -v
"""


def top_games_by_ggr_sql() -> str:
    """
    Return SQL for top 3 games by total GGR.
    Table: rounds(round_id, player_id, game_id, bet_amount, win_amount, timestamp)
    Columns: game_id, ggr
    """
    pass
''',
    "05_sql_gaming_analytics/challenges/player_favorite_game_sql.py": '''\
"""
Challenge: Player Favorite Game SQL
Module 05: SQL Analytics on Gaming Data

Theory: theory/02_top_games_and_affinity.md

Inputs:
  None — return SQL string only

Outputs:
  SQL: player_id, favorite_game (most rounds played; tie-break game_id ASC)

Edge cases:
  - Use window function or equivalent ranking
  - One favorite per player

Example:
  >>> result.query("player_id==101")["favorite_game"].iloc[0]
  'slots_a'

Run: pytest tests/05_sql_gaming_analytics/test_player_favorite_game_sql.py -v
"""


def player_favorite_game_sql() -> str:
    """
    Return SQL: player_id, favorite_game (most rounds played).
    Table: rounds(round_id, player_id, game_id, bet_amount, win_amount, timestamp)
    Tie-break by game_id ascending.
    """
    pass
''',
    "05_sql_gaming_analytics/challenges/rolling_ggr_sql.py": '''\
"""
Challenge: Rolling 7-Day GGR SQL
Module 05: SQL Analytics on Gaming Data

Theory: theory/03_window_functions_ggr.md

Inputs:
  None — return SQL string only

Outputs:
  SQL: activity_date, ggr, rolling_7d_ggr ordered by activity_date

Edge cases:
  - 7-day window includes current row (6 preceding + current)
  - Source table: daily_ggr(activity_date, ggr)

Example:
  >>> result.iloc[6]["rolling_7d_ggr"]  # 7 days × 10.0
  70.0

Run: pytest tests/05_sql_gaming_analytics/test_rolling_ggr_sql.py -v
"""


def rolling_7d_ggr_sql() -> str:
    """
    Return SQL: activity_date, ggr, rolling_7d_ggr (sum of ggr over 7-day window incl current day).
    Source: daily_ggr(activity_date, ggr)
    Order by activity_date.
    """
    pass
''',
    "06_feature_engineering/challenges/days_since_last_session.py": '''\
"""
Challenge: Days Since Last Session
Module 06: Feature Engineering

Theory: theory/01_player_features_daily.md

Inputs:
  events — player_id, timestamp
  feature_date — snapshot (exclude events >= feature_date)

Outputs:
  player_id, days_since_last_session

Edge cases:
  - Players with no activity before feature_date are omitted
  - Integer day difference via .days

Example:
  >>> days_since_last_session(events, pd.Timestamp("2024-06-04")).query("player_id==101")
  days_since_last_session == 3

Run: pytest tests/06_feature_engineering/test_days_since_last_session.py -v
"""

import pandas as pd


def days_since_last_session(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    """
    Return player_id, days_since_last_session for each player active before feature_date.
    If never active, omit player. Days = (feature_date - last_timestamp).days
    """
    pass
''',
    "06_feature_engineering/challenges/sessions_in_window.py": '''\
"""
Challenge: Sessions in Window
Module 06: Feature Engineering

Theory: theory/02_rolling_windows.md

Inputs:
  events — player_id, session_id, timestamp
  feature_date — end of 7-day window (inclusive)

Outputs:
  player_id, sessions_7d — distinct session count in window

Edge cases:
  - Window [feature_date − 6d, feature_date] inclusive
  - Player with no events in window omitted

Example:
  >>> sessions_7d(events, pd.Timestamp("2024-06-03")).query("player_id==103")["sessions_7d"].iloc[0]
  1

Run: pytest tests/06_feature_engineering/test_sessions_in_window.py -v
"""

import pandas as pd


def sessions_7d(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    """Return player_id, sessions_7d counting distinct session_id in last 7 days ending feature_date."""
    pass
''',
    "06_feature_engineering/challenges/build_player_features.py": '''\
"""
Challenge: Build Player Features
Module 06: Feature Engineering

Theory: theory/03_feature_grain_and_leakage.md

Inputs:
  events — full RGS events
  feature_date — end of 7-day feature window (inclusive)

Outputs:
  player_id, sessions_7d, avg_bet_7d, ggr_7d, favorite_game_7d

Edge cases:
  - Only players with activity in window
  - favorite_game = game with most rounds; tie-break game_id ascending

Example:
  >>> feats = build_player_features(events, pd.Timestamp("2024-06-03"))
  >>> set(feats.columns) >= {"sessions_7d", "ggr_7d", "favorite_game_7d"}

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
''',
    "07_player_segmentation/challenges/prepare_segmentation_features.py": '''\
"""
Challenge: Prepare Segmentation Features
Module 07: Player Segmentation

Theory: theory/02_clustering_algorithms.md

Inputs:
  df — feature table with numeric and non-feature columns
  feature_cols — list of column names to keep

Outputs:
  Numeric matrix with selected columns; NaN → 0

Edge cases:
  - Drop columns not in feature_cols
  - Preserve row count and index

Example:
  >>> prepare_features(df, ["sessions_30d", "ggr_30d"]).isna().sum().sum()
  0

Run: pytest tests/07_player_segmentation/test_prepare_segmentation_features.py -v
"""

import pandas as pd


def prepare_features(df: pd.DataFrame, feature_cols: list[str]) -> pd.DataFrame:
    """Return numeric feature matrix; fill NaN with 0; drop non-feature columns."""
    pass
''',
    "07_player_segmentation/challenges/kmeans_segment.py": '''\
"""
Challenge: K-Means Segment Players
Module 07: Player Segmentation

Theory: theory/02_clustering_algorithms.md

Inputs:
  features — numeric DataFrame (one row per player)
  n_clusters — k (default 3)
  random_state — reproducibility (default 42)

Outputs:
  Series of integer cluster labels indexed like features

Edge cases:
  - n_clusters must not exceed n_samples
  - Well-separated blobs → nunique() == n_clusters

Example:
  >>> kmeans_segment(features, n_clusters=2, random_state=42).nunique()
  2

Run: pytest tests/07_player_segmentation/test_kmeans_segment.py -v
"""

import pandas as pd


def kmeans_segment(features: pd.DataFrame, n_clusters: int = 3, random_state: int = 42) -> pd.Series:
    """Return Series of cluster labels indexed like features."""
    pass
''',
    "07_player_segmentation/challenges/profile_segments.py": '''\
"""
Challenge: Profile Segments
Module 07: Player Segmentation

Theory: theory/03_segment_profiling.md

Inputs:
  features — numeric feature DataFrame
  labels — cluster assignment Series (same index)

Outputs:
  Mean of each numeric column grouped by segment label

Edge cases:
  - Index of labels aligns with features rows
  - Single-column features still produce valid profile

Example:
  >>> profile = segment_profile(features, labels)
  >>> profile.loc[0, "ggr_30d"]  # mean GGR for cluster 0

Run: pytest tests/07_player_segmentation/test_profile_segments.py -v
"""

import pandas as pd


def segment_profile(features: pd.DataFrame, labels: pd.Series) -> pd.DataFrame:
    """Return mean of each numeric column grouped by segment label."""
    pass
''',
    "08_churn_prediction/challenges/label_churn.py": '''\
"""
Challenge: Label Churn Target
Module 08: Churn Prediction

Theory: theory/01_churn_definition.md

Inputs:
  activity — player_id, activity_date
  snapshot_date — label observation date
  horizon_days — forward inactivity window (default 30)

Outputs:
  player_id, inactive_next_30_days (1 = no future activity in horizon)

Edge cases:
  - Include players active in 30d before snapshot only
  - Future window: (snapshot_date, snapshot_date + horizon_days]

Example:
  >>> label_churn(activity, snapshot)["inactive_next_30_days"].tolist()

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
''',
    "08_churn_prediction/challenges/churn_feature_matrix.py": '''\
"""
Challenge: Churn Feature Matrix
Module 08: Churn Prediction

Theory: theory/02_churn_features.md

Inputs:
  events — RGS events with timestamp, session_id, bet/win amounts
  snapshot_date — feature cutoff (inclusive for history)

Outputs:
  player_id, days_since_last_session, sessions_30d, avg_bet_30d, ggr_30d

Edge cases:
  - History window: 30 days ending snapshot_date
  - Only players with activity in that window

Example:
  >>> build_churn_features(events, pd.Timestamp("2024-06-03"))

Run: pytest tests/08_churn_prediction/test_churn_feature_matrix.py -v
"""

import pandas as pd


def build_churn_features(events: pd.DataFrame, snapshot_date: pd.Timestamp) -> pd.DataFrame:
    """
    Return player_id, days_since_last_session, sessions_30d, avg_bet_30d, ggr_30d
    for players with any activity in 30d before snapshot_date.
    """
    pass
''',
    "08_churn_prediction/challenges/train_churn_model.py": '''\
"""
Challenge: Train Churn Model
Module 08: Churn Prediction

Theory: theory/03_model_training_and_eval.md

Inputs:
  features — includes player_id + numeric features
  labels — binary inactive_next_30_days
  random_state — default 42

Outputs:
  Fitted LightGBM classifier (drop player_id before fit)

Edge cases:
  - Model must expose .predict and .predict_proba
  - Small synthetic data should fit without error

Example:
  >>> model = train_churn_classifier(features, labels)
  >>> model.predict(features.drop(columns=["player_id"]))

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
''',
    "09_ltv_proxy/challenges/label_future_ggr.py": '''\
"""
Challenge: Label Future GGR
Module 09: LTV & Value Proxy

Theory: theory/02_future_ggr_prediction.md

Inputs:
  events — RGS events
  snapshot_date — start of label window (exclusive for past)
  horizon_days — forward window length (default 30)

Outputs:
  player_id, future_ggr_30d — sum of GGR in forward window

Edge cases:
  - Label period: (snapshot_date, snapshot_date + horizon_days]
  - Players with no future rounds omitted from result

Example:
  >>> label_future_ggr(events, pd.Timestamp("2024-06-01"))["future_ggr_30d"].sum()

Run: pytest tests/09_ltv_proxy/test_label_future_ggr.py -v
"""

import pandas as pd


def label_future_ggr(events: pd.DataFrame, snapshot_date: pd.Timestamp, horizon_days: int = 30) -> pd.DataFrame:
    """
    For players active before snapshot_date, sum GGR in (snapshot_date, snapshot_date + horizon_days].
    Return player_id, future_ggr_30d.
    """
    pass
''',
    "09_ltv_proxy/challenges/ltv_feature_matrix.py": '''\
"""
Challenge: LTV Feature Matrix
Module 09: LTV & Value Proxy

Theory: theory/01_ltv_definitions.md

Inputs:
  events — RGS events
  snapshot_date — feature cutoff (inclusive)

Outputs:
  player_id, ggr_30d, sessions_30d, avg_bet_30d for players active before snapshot

Edge cases:
  - 30-day lookback ending at snapshot_date
  - Point-in-time: no future events in features

Example:
  >>> ltv_features(events, pd.Timestamp("2024-06-03"))

Run: pytest tests/09_ltv_proxy/test_ltv_feature_matrix.py -v
"""

import pandas as pd


def ltv_features(events: pd.DataFrame, snapshot_date: pd.Timestamp) -> pd.DataFrame:
    """Return player_id, ggr_30d, sessions_30d, avg_bet_30d for players active before snapshot."""
    pass
''',
    "09_ltv_proxy/challenges/train_ltv_model.py": '''\
"""
Challenge: Train LTV Model
Module 09: LTV & Value Proxy

Theory: theory/03_proxy_limitations.md

Inputs:
  features — numeric columns (+ optional player_id)
  targets — future_ggr_30d Series
  random_state — default 42

Outputs:
  Fitted LightGBM regressor

Edge cases:
  - Drop player_id before training
  - Must expose .predict for regression

Example:
  >>> model = train_ltv_regressor(features, targets)
  >>> len(model.predict(features.drop(columns=["player_id"])))

Run: pytest tests/09_ltv_proxy/test_train_ltv_model.py -v
"""

import pandas as pd


def train_ltv_regressor(features: pd.DataFrame, targets: pd.Series, random_state: int = 42):
    """Train LightGBM regressor. Return fitted model."""
    pass
''',
    "10_recommendations/challenges/player_game_matrix.py": '''\
"""
Challenge: Player-Game Matrix
Module 10: Recommendation Engine

Theory: theory/02_collaborative_filtering.md

Inputs:
  events — player_id, game_id (round-level)

Outputs:
  Pivot: rows=player_id, columns=game_id, values=round_count; fill NaN with 0

Edge cases:
  - Count every round row
  - Shared sample: shape (4 players, 3 games)

Example:
  >>> player_game_matrix(events).loc[101, "slots_a"]
  2

Run: pytest tests/10_recommendations/test_player_game_matrix.py -v
"""

import pandas as pd


def player_game_matrix(events: pd.DataFrame) -> pd.DataFrame:
    """
    Return pivot: rows=player_id, columns=game_id, values=round_count (number of rounds).
    Fill missing with 0.
    """
    pass
''',
    "10_recommendations/challenges/top_games_per_player.py": '''\
"""
Challenge: Top Games per Player
Module 10: Recommendation Engine

Theory: theory/02_collaborative_filtering.md

Inputs:
  events — player_id, game_id
  n — top-N per player (default 3)

Outputs:
  player_id, rank, game_id sorted by round count desc; tie-break game_id asc

Edge cases:
  - rank starts at 1 per player
  - Fewer than n games → return available only

Example:
  >>> top_n_games_per_player(events, n=2).query("player_id==101 and rank==1")["game_id"].iloc[0]
  'slots_a'

Run: pytest tests/10_recommendations/test_top_games_per_player.py -v
"""

import pandas as pd


def top_n_games_per_player(events: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Return player_id, rank, game_id sorted by round count descending per player."""
    pass
''',
    "10_recommendations/challenges/recommend_popular_games.py": '''\
"""
Challenge: Recommend Popular Games
Module 10: Recommendation Engine

Theory: theory/03_offline_evaluation.md

Inputs:
  events — all player rounds
  player_id — target player
  n — number of recommendations

Outputs:
  list[str] — top globally popular games (by round count) not yet played by player

Edge cases:
  - Tie-break by game_id ascending
  - Player 101 → blackjack_c is top unplayed in shared sample

Example:
  >>> recommend_popular_unplayed(events, player_id=101, n=1)
  ['blackjack_c']

Run: pytest tests/10_recommendations/test_recommend_popular_games.py -v
"""

import pandas as pd


def recommend_popular_unplayed(events: pd.DataFrame, player_id: int, n: int = 3) -> list[str]:
    """
    Return top n globally popular games (by round count) the player has NOT played.
    Tie-break by game_id ascending.
    """
    pass
''',
    "11_analytics_architecture/challenges/estimate_storage.py": '''\
"""
Challenge: Estimate Storage
Module 11: Analytics Architecture

Theory: theory/04_cost_and_feasibility.md

Inputs:
  events_per_day — daily round/event volume
  bytes_per_event — average row size (default 256)

Outputs:
  float — estimated GB per day (1 GB = 1e9 bytes)

Edge cases:
  - Linear scaling with volume
  - 10_000_000 × 256 / 1e9 == 2.56

Example:
  >>> estimate_daily_storage_gb(10_000_000)
  2.56

Run: pytest tests/11_analytics_architecture/test_estimate_storage.py -v
"""


def estimate_daily_storage_gb(
    events_per_day: int,
    bytes_per_event: int = 256,
) -> float:
    """Return estimated GB per day (use 1 GB = 1e9 bytes)."""
    pass
''',
    "11_analytics_architecture/challenges/pipeline_phase_order.py": '''\
"""
Challenge: Pipeline Phase Order
Module 11: Analytics Architecture

Theory: theory/01_rgs_to_warehouse.md, theory/03_batch_vs_realtime_ml.md

Inputs:
  completed — list of phase names already finished

Outputs:
  Next recommended phase string, or None if all complete

Edge cases:
  - Ignore unknown completed phases
  - Order: warehouse → dbt_features → segmentation_churn_ltv → recommendations → feature_store_eval

Example:
  >>> next_phase([])
  'warehouse'

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
''',
}


# ---------------------------------------------------------------------------
# Tests — 32 pytest modules (specific assertions; pass with solutions.py)
# ---------------------------------------------------------------------------

TESTS: dict[str, str] = {
    "tests/01_igaming_domain/test_validate_rgs_event.py": '''\
from shared.testing import load_challenge

validate_rgs_event = load_challenge("01_igaming_domain", "validate_rgs_event.py").validate_rgs_event

VALID = {
    "round_id": "r1",
    "player_id": 1,
    "session_id": "s1",
    "game_id": "slots_a",
    "timestamp": "2024-06-01",
    "bet_amount": 10.0,
    "win_amount": 0.0,
}


def test_valid_event():
    ok, errs = validate_rgs_event(VALID)
    assert ok is True
    assert errs == []


def test_missing_required_fields():
    ok, errs = validate_rgs_event({"round_id": "r1", "player_id": 1})
    assert ok is False
    assert "missing field: session_id" in errs
    assert "missing field: game_id" in errs
    assert "missing field: timestamp" in errs


def test_negative_bet_amount():
    event = {**VALID, "bet_amount": -1.0}
    ok, errs = validate_rgs_event(event)
    assert ok is False
    assert "bet_amount must be non-negative" in errs


def test_negative_win_amount():
    event = {**VALID, "win_amount": -5.0}
    ok, errs = validate_rgs_event(event)
    assert ok is False
    assert "win_amount must be non-negative" in errs
''',
    "tests/01_igaming_domain/test_compute_ggr.py": '''\
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

mod = load_challenge("01_igaming_domain", "compute_ggr.py")
compute_ggr = mod.compute_ggr
total_ggr = mod.total_ggr


def test_compute_ggr_adds_column_without_mutating_input():
    df = rgs_events_frame()
    original_cols = list(df.columns)
    out = compute_ggr(df)
    assert list(df.columns) == original_cols
    assert "ggr" in out.columns
    assert out.loc[0, "ggr"] == 10.0
    assert out.loc[1, "ggr"] == -10.0
    assert out.loc[2, "ggr"] == 20.0


def test_total_ggr_shared_sample():
    assert total_ggr(rgs_events_frame()) == -4.0


def test_total_ggr_empty_frame():
    import pandas as pd

    empty = pd.DataFrame(columns=["bet_amount", "win_amount"])
    assert total_ggr(empty) == 0.0
''',
    "tests/01_igaming_domain/test_compute_ggr_by_game.py": '''\
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ggr_by_game = load_challenge("01_igaming_domain", "compute_ggr_by_game.py").ggr_by_game


def test_ggr_by_game_columns_and_top_game():
    out = ggr_by_game(rgs_events_frame())
    assert list(out.columns) == ["game_id", "total_bets", "total_wins", "ggr"]
    assert out.iloc[0]["game_id"] == "roulette_b"
    assert out.iloc[0]["ggr"] == 60.0
    assert out.iloc[0]["total_bets"] == 60.0
    assert out.iloc[0]["total_wins"] == 0.0


def test_ggr_by_game_sorted_descending():
    out = ggr_by_game(rgs_events_frame())
    assert out["ggr"].tolist() == sorted(out["ggr"].tolist(), reverse=True)


def test_ggr_by_game_empty():
    empty = pd.DataFrame(columns=["game_id", "bet_amount", "win_amount"])
    out = ggr_by_game(empty)
    assert list(out.columns) == ["game_id", "total_bets", "total_wins", "ggr"]
    assert len(out) == 0
''',
    "tests/02_engagement_metrics/test_compute_dau.py": '''\
import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

daily_active_users = load_challenge("02_engagement_metrics", "compute_dau.py").daily_active_users


def test_dau_on_active_day():
    activity = daily_activity_frame()
    assert daily_active_users(activity, pd.Timestamp("2024-06-01")) == 2


def test_dau_counts_unique_players():
    activity = daily_activity_frame()
    assert daily_active_users(activity, pd.Timestamp("2024-06-05")) == 1


def test_dau_no_activity():
    activity = daily_activity_frame()
    assert daily_active_users(activity, pd.Timestamp("2024-06-04")) == 0
''',
    "tests/02_engagement_metrics/test_compute_wau_mau.py": '''\
import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

mod = load_challenge("02_engagement_metrics", "compute_wau_mau.py")
wau = mod.wau
mau = mod.mau


def test_wau_shared_sample():
    activity = daily_activity_frame()
    assert wau(activity, pd.Timestamp("2024-06-05")) == 4


def test_mau_shared_sample():
    activity = daily_activity_frame()
    assert mau(activity, pd.Timestamp("2024-06-05")) == 4


def test_wau_single_day_window():
    activity = pd.DataFrame(
        {"player_id": [1, 1, 2], "activity_date": pd.to_datetime(["2024-06-01"] * 3)}
    )
    assert wau(activity, pd.Timestamp("2024-06-01")) == 2
''',
    "tests/02_engagement_metrics/test_compute_stickiness.py": '''\
import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

stickiness = load_challenge("02_engagement_metrics", "compute_stickiness.py").stickiness


def test_stickiness_shared_sample():
    activity = daily_activity_frame()
    assert stickiness(activity, pd.Timestamp("2024-06-05")) == 0.25


def test_stickiness_zero_mau():
    activity = pd.DataFrame(
        {"player_id": [1], "activity_date": pd.to_datetime(["2023-01-01"])}
    )
    assert stickiness(activity, pd.Timestamp("2024-06-01")) == 0.0


def test_stickiness_perfect_daily():
    activity = pd.DataFrame(
        {
            "player_id": [1] * 30,
            "activity_date": pd.date_range("2024-06-01", periods=30),
        }
    )
    assert stickiness(activity, pd.Timestamp("2024-06-30")) == 1.0
''',
    "tests/03_cohorts_retention/test_assign_cohort.py": '''\
import pandas as pd
from shared.datasets import players_frame
from shared.testing import load_challenge

assign_registration_cohort = load_challenge(
    "03_cohorts_retention", "assign_cohort.py"
).assign_registration_cohort


def test_cohort_week_monday_start():
    out = assign_registration_cohort(players_frame())
    assert pd.Timestamp(out.loc[out.player_id == 101, "cohort_week"].iloc[0]) == pd.Timestamp(
        "2024-04-29"
    )
    assert pd.Timestamp(out.loc[out.player_id == 104, "cohort_week"].iloc[0]) == pd.Timestamp(
        "2024-05-27"
    )


def test_assign_cohort_preserves_columns():
    players = players_frame()
    out = assign_registration_cohort(players)
    assert "cohort_week" in out.columns
    assert set(players.columns).issubset(out.columns)
    assert len(out) == len(players)
''',
    "tests/03_cohorts_retention/test_compute_retention.py": '''\
import pandas as pd
from shared.datasets import daily_activity_frame, players_frame
from shared.testing import load_challenge

d7_retention = load_challenge("03_cohorts_retention", "compute_retention.py").d7_retention


def test_d7_retention_shared_sample():
    assert d7_retention(players_frame(), daily_activity_frame()) == 0.0


def test_d7_retention_perfect_cohort():
    players = pd.DataFrame(
        {"player_id": [1, 2], "registration_date": pd.to_datetime(["2024-06-01", "2024-06-01"])}
    )
    activity = pd.DataFrame(
        {"player_id": [1, 2], "activity_date": pd.to_datetime(["2024-06-08", "2024-06-08"])}
    )
    assert d7_retention(players, activity) == 1.0


def test_d7_retention_empty_players():
    empty = pd.DataFrame(columns=["player_id", "registration_date"])
    activity = daily_activity_frame()
    assert d7_retention(empty, activity) == 0.0
''',
    "tests/03_cohorts_retention/test_build_cohort_table.py": '''\
import pandas as pd
from shared.datasets import daily_activity_frame, players_frame
from shared.testing import load_challenge

cohort_retention_table = load_challenge(
    "03_cohorts_retention", "build_cohort_table.py"
).cohort_retention_table


def test_cohort_table_columns():
    out = cohort_retention_table(players_frame(), daily_activity_frame(), [1, 7])
    assert list(out.columns) == ["d1", "d7"]
    assert len(out.index) >= 1


def test_cohort_table_d1_zero_for_may_cohort():
    out = cohort_retention_table(players_frame(), daily_activity_frame(), [1])
    cohort = pd.Timestamp("2024-04-29")
    if cohort in out.index:
        assert out.loc[cohort, "d1"] == 0.0


def test_cohort_table_retention_bounds():
    out = cohort_retention_table(players_frame(), daily_activity_frame(), [1, 7, 30])
    assert (out.values >= 0.0).all()
    assert (out.values <= 1.0).all()
''',
    "tests/04_session_analytics/test_sessionize_events.py": '''\
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

sessionize_by_gap = load_challenge("04_session_analytics", "sessionize_events.py").sessionize_by_gap


def test_sessionize_adds_derived_session_id():
    events = rgs_events_frame()
    out = sessionize_by_gap(events, gap_minutes=30)
    assert "derived_session_id" in out.columns
    assert out["derived_session_id"].min() >= 1


def test_sessionize_player_101_single_session():
    out = sessionize_by_gap(rgs_events_frame(), gap_minutes=30)
    p101 = out[out.player_id == 101]
    assert p101["derived_session_id"].nunique() == 1
    assert p101["derived_session_id"].tolist() == [1, 1, 1]


def test_sessionize_player_102_two_sessions():
    out = sessionize_by_gap(rgs_events_frame(), gap_minutes=30)
    p102 = out[out.player_id == 102]
    assert p102["derived_session_id"].nunique() == 2
    assert p102["derived_session_id"].tolist() == [1, 2]
''',
    "tests/04_session_analytics/test_session_duration.py": '''\
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

session_durations = load_challenge("04_session_analytics", "session_duration.py").session_durations


def test_session_duration_player_101():
    out = session_durations(rgs_events_frame())
    row = out[(out.player_id == 101) & (out.session_id == "s1")].iloc[0]
    assert row["duration_minutes"] == 35.0
    assert row["round_count"] == 3


def test_session_duration_columns():
    out = session_durations(rgs_events_frame())
    assert list(out.columns) == ["player_id", "session_id", "duration_minutes", "round_count"]


def test_session_duration_non_negative():
    out = session_durations(rgs_events_frame())
    assert (out["duration_minutes"] >= 0.0).all()
    assert (out["round_count"] >= 1).all()
''',
    "tests/04_session_analytics/test_ggr_per_session.py": '''\
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ggr_per_session = load_challenge("04_session_analytics", "ggr_per_session.py").ggr_per_session


def test_ggr_per_session_player_101():
    out = ggr_per_session(rgs_events_frame())
    row = out[(out.player_id == 101) & (out.session_id == "s1")].iloc[0]
    assert row["total_bets"] == 35.0
    assert row["total_wins"] == 15.0
    assert row["ggr"] == 20.0


def test_ggr_per_session_columns():
    out = ggr_per_session(rgs_events_frame())
    assert list(out.columns) == ["player_id", "session_id", "total_bets", "total_wins", "ggr"]


def test_ggr_per_session_row_count():
    out = ggr_per_session(rgs_events_frame())
    assert len(out) == rgs_events_frame()[["player_id", "session_id"]].drop_duplicates().shape[0]
''',
    "tests/05_sql_gaming_analytics/test_top_games_sql.py": '''\
from shared.datasets import rgs_events_frame
from shared.sql_helpers import query_duckdb
from shared.testing import load_challenge

top_games_by_ggr_sql = load_challenge("05_sql_gaming_analytics", "top_games_sql.py").top_games_by_ggr_sql


def _rounds_table():
    df = rgs_events_frame()
    return df[["round_id", "player_id", "game_id", "bet_amount", "win_amount", "timestamp"]]


def test_top_games_sql_shape_and_columns():
    result = query_duckdb(top_games_by_ggr_sql(), {"rounds": _rounds_table()})
    assert len(result) == 3
    assert list(result.columns) == ["game_id", "ggr"]


def test_top_games_sql_first_is_roulette():
    result = query_duckdb(top_games_by_ggr_sql(), {"rounds": _rounds_table()})
    assert result.iloc[0]["game_id"] == "roulette_b"
    assert float(result.iloc[0]["ggr"]) == 60.0


def test_top_games_sql_sorted_descending():
    result = query_duckdb(top_games_by_ggr_sql(), {"rounds": _rounds_table()})
    assert result["ggr"].tolist() == sorted(result["ggr"].tolist(), reverse=True)
''',
    "tests/05_sql_gaming_analytics/test_player_favorite_game_sql.py": '''\
from shared.datasets import rgs_events_frame
from shared.sql_helpers import query_duckdb
from shared.testing import load_challenge

player_favorite_game_sql = load_challenge(
    "05_sql_gaming_analytics", "player_favorite_game_sql.py"
).player_favorite_game_sql


def _rounds_table():
    df = rgs_events_frame()
    return df[["round_id", "player_id", "game_id", "bet_amount", "win_amount", "timestamp"]]


def test_favorite_game_player_101():
    result = query_duckdb(player_favorite_game_sql(), {"rounds": _rounds_table()})
    assert result.loc[result.player_id == 101, "favorite_game"].iloc[0] == "slots_a"


def test_favorite_game_one_row_per_player():
    result = query_duckdb(player_favorite_game_sql(), {"rounds": _rounds_table()})
    assert len(result) == rgs_events_frame()["player_id"].nunique()
    assert result["player_id"].is_unique


def test_favorite_game_tie_break():
    import pandas as pd

    rounds = pd.DataFrame(
        {
            "round_id": ["a", "b", "c", "d"],
            "player_id": [1, 1, 1, 1],
            "game_id": ["game_b", "game_b", "game_a", "game_a"],
            "bet_amount": [1.0, 1.0, 1.0, 1.0],
            "win_amount": [0.0, 0.0, 0.0, 0.0],
            "timestamp": pd.date_range("2024-06-01", periods=4, freq="h"),
        }
    )
    result = query_duckdb(player_favorite_game_sql(), {"rounds": rounds})
    assert result.loc[result.player_id == 1, "favorite_game"].iloc[0] == "game_a"
''',
    "tests/05_sql_gaming_analytics/test_rolling_ggr_sql.py": '''\
import pandas as pd
from shared.sql_helpers import query_duckdb
from shared.testing import load_challenge

rolling_7d_ggr_sql = load_challenge("05_sql_gaming_analytics", "rolling_ggr_sql.py").rolling_7d_ggr_sql


def test_rolling_ggr_columns():
    daily = pd.DataFrame(
        {"activity_date": pd.date_range("2024-06-01", periods=10), "ggr": [10.0] * 10}
    )
    result = query_duckdb(rolling_7d_ggr_sql(), {"daily_ggr": daily})
    assert list(result.columns) == ["activity_date", "ggr", "rolling_7d_ggr"]


def test_rolling_ggr_seventh_day():
    daily = pd.DataFrame(
        {"activity_date": pd.date_range("2024-06-01", periods=10), "ggr": [10.0] * 10}
    )
    result = query_duckdb(rolling_7d_ggr_sql(), {"daily_ggr": daily})
    assert float(result.iloc[6]["rolling_7d_ggr"]) == 70.0


def test_rolling_ggr_first_day():
    daily = pd.DataFrame(
        {"activity_date": pd.date_range("2024-06-01", periods=10), "ggr": [10.0] * 10}
    )
    result = query_duckdb(rolling_7d_ggr_sql(), {"daily_ggr": daily})
    assert float(result.iloc[0]["rolling_7d_ggr"]) == 10.0
''',
    "tests/06_feature_engineering/test_days_since_last_session.py": '''\
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

days_since_last_session = load_challenge(
    "06_feature_engineering", "days_since_last_session.py"
).days_since_last_session


def test_days_since_player_101():
    out = days_since_last_session(rgs_events_frame(), pd.Timestamp("2024-06-04"))
    assert out.loc[out.player_id == 101, "days_since_last_session"].iloc[0] == 3


def test_days_since_excludes_feature_date_events():
    out = days_since_last_session(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert 104 not in set(out["player_id"])


def test_days_since_columns():
    out = days_since_last_session(rgs_events_frame(), pd.Timestamp("2024-06-05"))
    assert list(out.columns) == ["player_id", "days_since_last_session"]
    assert (out["days_since_last_session"] >= 0).all()
''',
    "tests/06_feature_engineering/test_sessions_in_window.py": '''\
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

sessions_7d = load_challenge("06_feature_engineering", "sessions_in_window.py").sessions_7d


def test_sessions_7d_player_103():
    out = sessions_7d(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert out.loc[out.player_id == 103, "sessions_7d"].iloc[0] == 1


def test_sessions_7d_window_excludes_old_activity():
    events = rgs_events_frame()
    out = sessions_7d(events, pd.Timestamp("2024-05-15"))
    assert len(out) == 0


def test_sessions_7d_counts_distinct_sessions():
    import pandas as pd

    events = pd.DataFrame(
        {
            "player_id": [1, 1, 1],
            "session_id": ["a", "b", "b"],
            "timestamp": pd.to_datetime(["2024-06-01", "2024-06-02", "2024-06-02 10:00"]),
            "round_id": ["r1", "r2", "r3"],
            "game_id": ["g"] * 3,
            "bet_amount": [1.0, 1.0, 1.0],
            "win_amount": [0.0, 0.0, 0.0],
        }
    )
    out = sessions_7d(events, pd.Timestamp("2024-06-02"))
    assert out.loc[out.player_id == 1, "sessions_7d"].iloc[0] == 2
''',
    "tests/06_feature_engineering/test_build_player_features.py": '''\
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

build_player_features = load_challenge(
    "06_feature_engineering", "build_player_features.py"
).build_player_features


def test_player_features_columns_and_players():
    out = build_player_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert set(out.columns) == {
        "player_id",
        "sessions_7d",
        "avg_bet_7d",
        "ggr_7d",
        "favorite_game_7d",
    }
    assert set(out["player_id"]) == {101, 102, 103, 104}


def test_player_features_player_101():
    out = build_player_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    row = out[out.player_id == 101].iloc[0]
    assert row["sessions_7d"] == 1
    assert row["favorite_game_7d"] == "slots_a"
    assert row["ggr_7d"] == 20.0


def test_player_features_avg_bet():
    out = build_player_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    row = out[out.player_id == 101].iloc[0]
    assert abs(row["avg_bet_7d"] - 35.0 / 3) < 1e-6
''',
    "tests/07_player_segmentation/test_prepare_segmentation_features.py": '''\
import pandas as pd
from shared.testing import load_challenge

prepare_features = load_challenge(
    "07_player_segmentation", "prepare_segmentation_features.py"
).prepare_features


def test_prepare_features_selects_and_fills():
    df = pd.DataFrame(
        {
            "player_id": [1, 2],
            "sessions_30d": [10.0, None],
            "ggr_30d": [100.0, -5.0],
            "country": ["UK", "DE"],
        }
    )
    out = prepare_features(df, ["sessions_30d", "ggr_30d"])
    assert list(out.columns) == ["sessions_30d", "ggr_30d"]
    assert out.loc[1, "sessions_30d"] == 0.0
    assert out.isna().sum().sum() == 0


def test_prepare_features_shape():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "label": ["x", "y"]})
    out = prepare_features(df, ["a", "b"])
    assert out.shape == (2, 2)
''',
    "tests/07_player_segmentation/test_kmeans_segment.py": '''\
import pandas as pd
from shared.testing import load_challenge

kmeans_segment = load_challenge("07_player_segmentation", "kmeans_segment.py").kmeans_segment


def test_kmeans_label_count():
    features = pd.DataFrame({"a": [0, 10, 0.1, 9.9], "b": [0, 10, 0.2, 9.8]})
    labels = kmeans_segment(features, n_clusters=2, random_state=42)
    assert len(labels) == 4
    assert labels.nunique() == 2


def test_kmeans_index_aligned():
    features = pd.DataFrame({"x": [1, 2, 3, 4]}, index=[10, 20, 30, 40])
    labels = kmeans_segment(features, n_clusters=2, random_state=42)
    assert list(labels.index) == [10, 20, 30, 40]


def test_kmeans_three_clusters():
    features = pd.DataFrame({"a": [0, 10, 20, 0.1, 9.9, 20.1], "b": [0, 10, 20, 0.2, 9.8, 19.9]})
    labels = kmeans_segment(features, n_clusters=3, random_state=42)
    assert labels.nunique() == 3
''',
    "tests/07_player_segmentation/test_profile_segments.py": '''\
import pandas as pd
from shared.testing import load_challenge

segment_profile = load_challenge("07_player_segmentation", "profile_segments.py").segment_profile


def test_profile_means_by_cluster():
    features = pd.DataFrame({"ggr_30d": [100.0, 102.0, 10.0, 12.0], "sessions_30d": [20, 22, 2, 3]})
    labels = pd.Series([0, 0, 1, 1])
    profile = segment_profile(features, labels)
    assert abs(profile.loc[0, "ggr_30d"] - 101.0) < 1e-6
    assert abs(profile.loc[1, "ggr_30d"] - 11.0) < 1e-6


def test_profile_column_count():
    features = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0]})
    labels = pd.Series([0, 1])
    profile = segment_profile(features, labels)
    assert list(profile.columns) == ["a", "b"]
    assert len(profile) == 2
''',
    "tests/08_churn_prediction/test_label_churn.py": '''\
import pandas as pd
from shared.testing import load_challenge

label_churn = load_challenge("08_churn_prediction", "label_churn.py").label_churn


def test_label_churn_inactive_player():
    activity = pd.DataFrame(
        {
            "player_id": [1, 1, 2, 2, 2],
            "activity_date": pd.to_datetime(
                ["2024-05-15", "2024-06-01", "2024-05-20", "2024-06-01", "2024-06-15"]
            ),
        }
    )
    out = label_churn(activity, pd.Timestamp("2024-06-01"), horizon_days=30)
    labels = dict(zip(out["player_id"], out["inactive_next_30_days"]))
    assert labels[1] == 1
    assert labels[2] == 0


def test_label_churn_active_in_horizon():
    activity = pd.DataFrame(
        {
            "player_id": [1, 1, 1],
            "activity_date": pd.to_datetime(["2024-05-15", "2024-06-01", "2024-06-15"]),
        }
    )
    out = label_churn(activity, pd.Timestamp("2024-06-01"), horizon_days=30)
    assert out.loc[out.player_id == 1, "inactive_next_30_days"].iloc[0] == 0


def test_label_churn_columns():
    activity = pd.DataFrame(
        {"player_id": [1], "activity_date": pd.to_datetime(["2024-06-01"])}
    )
    out = label_churn(activity, pd.Timestamp("2024-06-01"))
    assert list(out.columns) == ["player_id", "inactive_next_30_days"]
''',
    "tests/08_churn_prediction/test_churn_feature_matrix.py": '''\
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

build_churn_features = load_challenge(
    "08_churn_prediction", "churn_feature_matrix.py"
).build_churn_features


def test_churn_features_columns():
    out = build_churn_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert set(out.columns) == {
        "player_id",
        "days_since_last_session",
        "sessions_30d",
        "avg_bet_30d",
        "ggr_30d",
    }


def test_churn_features_player_101():
    out = build_churn_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    row = out[out.player_id == 101].iloc[0]
    assert row["sessions_30d"] == 1
    assert row["days_since_last_session"] == 2


def test_churn_features_includes_all_active_players():
    out = build_churn_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert set(out["player_id"]) == {101, 102, 103, 104}
''',
    "tests/08_churn_prediction/test_train_churn_model.py": '''\
import pandas as pd
from shared.testing import load_challenge

train_churn_classifier = load_challenge(
    "08_churn_prediction", "train_churn_model.py"
).train_churn_classifier


def test_train_churn_predict():
    features = pd.DataFrame(
        {
            "player_id": [1, 2, 3, 4],
            "sessions_30d": [10, 2, 8, 1],
            "avg_bet_30d": [5.0, 1.0, 4.0, 2.0],
            "ggr_30d": [100.0, -10.0, 50.0, -5.0],
            "days_since_last_session": [1, 20, 2, 25],
        }
    )
    labels = pd.Series([0, 1, 0, 1])
    model = train_churn_classifier(features, labels, random_state=42)
    preds = model.predict(features.drop(columns=["player_id"]))
    assert len(preds) == 4
    assert set(preds).issubset({0, 1})


def test_train_churn_predict_proba():
    features = pd.DataFrame(
        {
            "player_id": [1, 2, 3, 4],
            "sessions_30d": [10, 2, 8, 1],
            "avg_bet_30d": [5.0, 1.0, 4.0, 2.0],
            "ggr_30d": [100.0, -10.0, 50.0, -5.0],
            "days_since_last_session": [1, 20, 2, 25],
        }
    )
    labels = pd.Series([0, 1, 0, 1])
    model = train_churn_classifier(features, labels, random_state=42)
    proba = model.predict_proba(features.drop(columns=["player_id"]))
    assert proba.shape == (4, 2)
''',
    "tests/09_ltv_proxy/test_label_future_ggr.py": '''\
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

label_future_ggr = load_challenge("09_ltv_proxy", "label_future_ggr.py").label_future_ggr


def test_future_ggr_player_101():
    out = label_future_ggr(rgs_events_frame(), pd.Timestamp("2024-06-01"), horizon_days=30)
    row = out[out.player_id == 101].iloc[0]
    assert row["future_ggr_30d"] == 20.0


def test_future_ggr_columns():
    out = label_future_ggr(rgs_events_frame(), pd.Timestamp("2024-06-01"))
    assert list(out.columns) == ["player_id", "future_ggr_30d"]


def test_future_ggr_empty_horizon():
    out = label_future_ggr(rgs_events_frame(), pd.Timestamp("2024-12-01"), horizon_days=7)
    assert len(out) == 0
''',
    "tests/09_ltv_proxy/test_ltv_feature_matrix.py": '''\
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ltv_features = load_challenge("09_ltv_proxy", "ltv_feature_matrix.py").ltv_features


def test_ltv_features_columns():
    out = ltv_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert set(out.columns) == {"player_id", "ggr_30d", "sessions_30d", "avg_bet_30d"}


def test_ltv_features_player_103():
    out = ltv_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    row = out[out.player_id == 103].iloc[0]
    assert row["sessions_30d"] == 1
    assert row["ggr_30d"] == 26.0


def test_ltv_features_all_players_before_snapshot():
    out = ltv_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert set(out["player_id"]) == {101, 102, 103, 104}
''',
    "tests/09_ltv_proxy/test_train_ltv_model.py": '''\
import pandas as pd
from shared.testing import load_challenge

train_ltv_regressor = load_challenge("09_ltv_proxy", "train_ltv_model.py").train_ltv_regressor


def test_train_ltv_predict():
    features = pd.DataFrame(
        {
            "player_id": [1, 2, 3],
            "ggr_30d": [100.0, 50.0, 10.0],
            "sessions_30d": [20, 10, 2],
            "avg_bet_30d": [5.0, 4.0, 2.0],
        }
    )
    targets = pd.Series([120.0, 40.0, 15.0])
    model = train_ltv_regressor(features, targets, random_state=42)
    preds = model.predict(features.drop(columns=["player_id"]))
    assert len(preds) == 3
    assert preds.dtype.kind in {"f", "i"}


def test_train_ltv_regressor_fitted():
    features = pd.DataFrame({"ggr_30d": [1.0, 2.0], "sessions_30d": [1, 2]})
    targets = pd.Series([10.0, 20.0])
    model = train_ltv_regressor(features, targets, random_state=42)
    assert hasattr(model, "predict")
''',
    "tests/10_recommendations/test_player_game_matrix.py": '''\
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

player_game_matrix = load_challenge(
    "10_recommendations", "player_game_matrix.py"
).player_game_matrix


def test_matrix_shape():
    matrix = player_game_matrix(rgs_events_frame())
    assert matrix.shape == (4, 3)
    assert list(matrix.columns) == ["blackjack_c", "roulette_b", "slots_a"]


def test_matrix_player_101_slots():
    matrix = player_game_matrix(rgs_events_frame())
    assert matrix.loc[101, "slots_a"] == 2
    assert matrix.loc[101, "roulette_b"] == 1
    assert matrix.loc[101, "blackjack_c"] == 0


def test_matrix_no_nan():
    matrix = player_game_matrix(rgs_events_frame())
    assert matrix.isna().sum().sum() == 0
''',
    "tests/10_recommendations/test_top_games_per_player.py": '''\
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

top_n_games_per_player = load_challenge(
    "10_recommendations", "top_games_per_player.py"
).top_n_games_per_player


def test_top_n_player_101_rank1():
    out = top_n_games_per_player(rgs_events_frame(), n=2)
    row = out[(out.player_id == 101) & (out.rank == 1)].iloc[0]
    assert row["game_id"] == "slots_a"


def test_top_n_rank_sequence():
    out = top_n_games_per_player(rgs_events_frame(), n=3)
    for player_id, grp in out.groupby("player_id"):
        assert grp["rank"].tolist() == list(range(1, len(grp) + 1))


def test_top_n_respects_n():
    out = top_n_games_per_player(rgs_events_frame(), n=1)
    assert (out.groupby("player_id").size() <= 1).all()
''',
    "tests/10_recommendations/test_recommend_popular_games.py": '''\
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

recommend_popular_unplayed = load_challenge(
    "10_recommendations", "recommend_popular_games.py"
).recommend_popular_unplayed


def test_recommend_unplayed_player_101():
    recs = recommend_popular_unplayed(rgs_events_frame(), player_id=101, n=1)
    assert recs == ["blackjack_c"]


def test_recommend_excludes_played_games():
    recs = recommend_popular_unplayed(rgs_events_frame(), player_id=101, n=3)
    assert "slots_a" not in recs
    assert "roulette_b" not in recs


def test_recommend_respects_n():
    recs = recommend_popular_unplayed(rgs_events_frame(), player_id=102, n=2)
    assert len(recs) <= 2
    assert len(set(recs)) == len(recs)
''',
    "tests/11_analytics_architecture/test_estimate_storage.py": '''\
from shared.testing import load_challenge

estimate_daily_storage_gb = load_challenge(
    "11_analytics_architecture", "estimate_storage.py"
).estimate_daily_storage_gb


def test_storage_ten_million_events():
    assert estimate_daily_storage_gb(10_000_000) == 2.56


def test_storage_custom_bytes():
    assert estimate_daily_storage_gb(1_000_000, bytes_per_event=512) == 0.512


def test_storage_zero_events():
    assert estimate_daily_storage_gb(0) == 0.0
''',
    "tests/11_analytics_architecture/test_pipeline_phase_order.py": '''\
from shared.testing import load_challenge

next_phase = load_challenge(
    "11_analytics_architecture", "pipeline_phase_order.py"
).next_phase


def test_next_phase_first():
    assert next_phase([]) == "warehouse"


def test_next_phase_after_warehouse():
    assert next_phase(["warehouse"]) == "dbt_features"


def test_next_phase_complete():
    completed = [
        "warehouse",
        "dbt_features",
        "segmentation_churn_ltv",
        "recommendations",
        "feature_store_eval",
    ]
    assert next_phase(completed) is None


def test_next_phase_skips_unknown():
    assert next_phase(["warehouse", "unknown_phase"]) == "dbt_features"
''',
}


def main() -> None:
    for rel_path, content in QUIZZES.items():
        write(ROOT / rel_path, content)
        print(f"Wrote quiz {rel_path}")

    for rel_path, content in CHALLENGES.items():
        write(ROOT / rel_path, content)
        print(f"Wrote challenge {rel_path}")

    for rel_path, content in TESTS.items():
        write(ROOT / rel_path, content)
        print(f"Wrote test {rel_path}")

    print(
        f"\nUpdated {len(QUIZZES)} quizzes, {len(CHALLENGES)} challenges, "
        f"{len(TESTS)} test files."
    )


if __name__ == "__main__":
    main()
