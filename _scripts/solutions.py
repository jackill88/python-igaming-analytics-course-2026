#!/usr/bin/env python3
"""Reference solutions — used to verify tests; not part of the student path."""

from __future__ import annotations

import pandas as pd
from sklearn.cluster import KMeans
import lightgbm as lgb


REQUIRED_FIELDS = {"round_id", "player_id", "session_id", "game_id", "timestamp", "bet_amount", "win_amount"}


def validate_rgs_event(event: dict) -> tuple[bool, list[str]]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in event:
            errors.append(f"missing field: {field}")
    if "bet_amount" in event and event["bet_amount"] < 0:
        errors.append("bet_amount must be non-negative")
    if "win_amount" in event and event["win_amount"] < 0:
        errors.append("win_amount must be non-negative")
    return len(errors) == 0, errors


def compute_ggr(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["ggr"] = out["bet_amount"] - out["win_amount"]
    return out


def total_ggr(df: pd.DataFrame) -> float:
    return float((df["bet_amount"] - df["win_amount"]).sum())


def ggr_by_game(df: pd.DataFrame) -> pd.DataFrame:
    agg = df.groupby("game_id").agg(
        total_bets=("bet_amount", "sum"),
        total_wins=("win_amount", "sum"),
    ).reset_index()
    agg["ggr"] = agg["total_bets"] - agg["total_wins"]
    return agg.sort_values("ggr", ascending=False).reset_index(drop=True)


def daily_active_users(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    day = as_of.normalize()
    mask = pd.to_datetime(activity["activity_date"]).dt.normalize() == day
    return int(activity.loc[mask, "player_id"].nunique())


def wau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    end = as_of.normalize()
    start = end - pd.Timedelta(days=6)
    dates = pd.to_datetime(activity["activity_date"]).dt.normalize()
    mask = (dates >= start) & (dates <= end)
    return int(activity.loc[mask, "player_id"].nunique())


def mau(activity: pd.DataFrame, as_of: pd.Timestamp) -> int:
    end = as_of.normalize()
    start = end - pd.Timedelta(days=29)
    dates = pd.to_datetime(activity["activity_date"]).dt.normalize()
    mask = (dates >= start) & (dates <= end)
    return int(activity.loc[mask, "player_id"].nunique())


def stickiness(activity: pd.DataFrame, as_of: pd.Timestamp) -> float:
    end = as_of.normalize()
    mau_start = end - pd.Timedelta(days=29)
    dau_start = end
    dates = pd.to_datetime(activity["activity_date"]).dt.normalize()
    mau_count = activity.loc[(dates >= mau_start) & (dates <= end), "player_id"].nunique()
    if mau_count == 0:
        return 0.0
    dau_count = activity.loc[dates == dau_start, "player_id"].nunique()
    return dau_count / mau_count


def assign_registration_cohort(players: pd.DataFrame) -> pd.DataFrame:
    out = players.copy()
    reg = pd.to_datetime(out["registration_date"])
    out["cohort_week"] = reg - pd.to_timedelta(reg.dt.dayofweek, unit="D")
    return out


def d7_retention(players: pd.DataFrame, activity: pd.DataFrame) -> float:
    if players.empty:
        return 0.0
    players = players.copy()
    activity = activity.copy()
    players["d7"] = pd.to_datetime(players["registration_date"]) + pd.Timedelta(days=7)
    activity_dates = pd.to_datetime(activity["activity_date"]).dt.normalize()
    retained = 0
    for _, row in players.iterrows():
        target = pd.Timestamp(row["d7"]).normalize()
        mask = (activity["player_id"] == row["player_id"]) & (activity_dates == target)
        if mask.any():
            retained += 1
    return retained / len(players)


def cohort_retention_table(players, activity, days):
    players = players.copy()
    reg = pd.to_datetime(players["registration_date"])
    players["cohort_week"] = reg - pd.to_timedelta(reg.dt.dayofweek, unit="D")
    activity = activity.copy()
    activity["activity_date"] = pd.to_datetime(activity["activity_date"])
    rows = {}
    for cohort, cohort_players in players.groupby("cohort_week"):
        cohort_ids = set(cohort_players["player_id"])
        n = len(cohort_ids)
        row = {}
        for d in days:
            target = cohort + pd.Timedelta(days=d)
            active = activity[
                (activity["player_id"].isin(cohort_ids))
                & (activity["activity_date"].dt.normalize() == target.normalize())
            ]["player_id"].nunique()
            row[f"d{d}"] = active / n if n else 0.0
        rows[cohort] = row
    return pd.DataFrame.from_dict(rows, orient="index")


def sessionize_by_gap(events: pd.DataFrame, gap_minutes: int = 30) -> pd.DataFrame:
    out = events.sort_values(["player_id", "timestamp"]).copy()
    session_ids = []
    for player_id, group in out.groupby("player_id"):
        sid = 1
        prev_ts = None
        for ts in group["timestamp"]:
            if prev_ts is not None and (ts - prev_ts).total_seconds() > gap_minutes * 60:
                sid += 1
            session_ids.append(sid)
            prev_ts = ts
    out["derived_session_id"] = session_ids
    return out


def session_durations(events: pd.DataFrame) -> pd.DataFrame:
    agg = events.groupby(["player_id", "session_id"]).agg(
        duration_minutes=("timestamp", lambda s: (s.max() - s.min()).total_seconds() / 60),
        round_count=("round_id", "count"),
    ).reset_index()
    return agg


def ggr_per_session(events: pd.DataFrame) -> pd.DataFrame:
    agg = events.groupby(["player_id", "session_id"]).agg(
        total_bets=("bet_amount", "sum"),
        total_wins=("win_amount", "sum"),
    ).reset_index()
    agg["ggr"] = agg["total_bets"] - agg["total_wins"]
    return agg


def top_games_by_ggr_sql() -> str:
    return """
    SELECT game_id, SUM(bet_amount - win_amount) AS ggr
    FROM rounds
    GROUP BY game_id
    ORDER BY ggr DESC
    LIMIT 3
    """


def player_favorite_game_sql() -> str:
    return """
    WITH counts AS (
        SELECT player_id, game_id, COUNT(*) AS cnt
        FROM rounds
        GROUP BY player_id, game_id
    ),
    ranked AS (
        SELECT player_id, game_id,
               ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY cnt DESC, game_id ASC) AS rn
        FROM counts
    )
    SELECT player_id, game_id AS favorite_game FROM ranked WHERE rn = 1
    """


def rolling_7d_ggr_sql() -> str:
    return """
    SELECT activity_date, ggr,
           SUM(ggr) OVER (ORDER BY activity_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7d_ggr
    FROM daily_ggr
    ORDER BY activity_date
    """


def days_since_last_session(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    events = events[events["timestamp"] < feature_date].copy()
    last = events.groupby("player_id")["timestamp"].max().reset_index()
    last["days_since_last_session"] = (feature_date - last["timestamp"]).dt.days
    return last[["player_id", "days_since_last_session"]]


def sessions_7d(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    start = feature_date - pd.Timedelta(days=6)
    window = events[(events["timestamp"] >= start) & (events["timestamp"] <= feature_date)]
    return window.groupby("player_id")["session_id"].nunique().reset_index(name="sessions_7d")


def build_player_features(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    start = feature_date - pd.Timedelta(days=6)
    window = events[(events["timestamp"] >= start) & (events["timestamp"] <= feature_date)].copy()
    fav = (
        window.groupby(["player_id", "game_id"]).size().reset_index(name="cnt")
        .sort_values(["player_id", "cnt", "game_id"], ascending=[True, False, True])
        .drop_duplicates("player_id")
        .rename(columns={"game_id": "favorite_game_7d"})
    )
    agg = window.groupby("player_id").agg(
        sessions_7d=("session_id", "nunique"),
        avg_bet_7d=("bet_amount", "mean"),
        ggr_7d=("bet_amount", lambda s: (s - window.loc[s.index, "win_amount"]).sum()),
    ).reset_index()
    return agg.merge(fav[["player_id", "favorite_game_7d"]], on="player_id", how="left")


def prepare_features(df: pd.DataFrame, feature_cols: list[str]) -> pd.DataFrame:
    return df[feature_cols].fillna(0)


def kmeans_segment(features: pd.DataFrame, n_clusters: int = 3, random_state: int = 42) -> pd.Series:
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    return pd.Series(model.fit_predict(features.values), index=features.index)


def segment_profile(features: pd.DataFrame, labels: pd.Series) -> pd.DataFrame:
    return features.groupby(labels).mean()


def label_churn(activity: pd.DataFrame, snapshot_date: pd.Timestamp, horizon_days: int = 30) -> pd.DataFrame:
    start = snapshot_date - pd.Timedelta(days=30)
    recent = activity[
        (pd.to_datetime(activity["activity_date"]) >= start)
        & (pd.to_datetime(activity["activity_date"]) <= snapshot_date)
    ]
    players = recent["player_id"].unique()
    end = snapshot_date + pd.Timedelta(days=horizon_days)
    future = activity[
        (pd.to_datetime(activity["activity_date"]) > snapshot_date)
        & (pd.to_datetime(activity["activity_date"]) <= end)
    ]
    active_future = set(future["player_id"])
    rows = [{"player_id": p, "inactive_next_30_days": int(p not in active_future)} for p in players]
    return pd.DataFrame(rows)


def build_churn_features(events: pd.DataFrame, snapshot_date: pd.Timestamp) -> pd.DataFrame:
    start = snapshot_date - pd.Timedelta(days=30)
    hist = events[(events["timestamp"] >= start) & (events["timestamp"] <= snapshot_date)].copy()
    last = events[events["timestamp"] <= snapshot_date].groupby("player_id")["timestamp"].max()
    agg = hist.groupby("player_id").agg(
        sessions_30d=("session_id", "nunique"),
        avg_bet_30d=("bet_amount", "mean"),
        ggr_30d=("bet_amount", lambda s: (s - hist.loc[s.index, "win_amount"]).sum()),
    )
    agg["days_since_last_session"] = (snapshot_date - last).dt.days
    return agg.reset_index()


def train_churn_classifier(features, labels, random_state=42):
    X = features.drop(columns=["player_id"], errors="ignore")
    model = lgb.LGBMClassifier(random_state=random_state, verbose=-1)
    model.fit(X, labels)
    return model


def label_future_ggr(events, snapshot_date, horizon_days=30):
    end = snapshot_date + pd.Timedelta(days=horizon_days)
    future = events[(events["timestamp"] > snapshot_date) & (events["timestamp"] <= end)].copy()
    future["ggr"] = future["bet_amount"] - future["win_amount"]
    return future.groupby("player_id")["ggr"].sum().reset_index(name="future_ggr_30d")


def ltv_features(events, snapshot_date):
    start = snapshot_date - pd.Timedelta(days=30)
    hist = events[events["timestamp"] <= snapshot_date].copy()
    window = hist[hist["timestamp"] >= start]
    return window.groupby("player_id").agg(
        ggr_30d=("bet_amount", lambda s: (s - window.loc[s.index, "win_amount"]).sum()),
        sessions_30d=("session_id", "nunique"),
        avg_bet_30d=("bet_amount", "mean"),
    ).reset_index()


def train_ltv_regressor(features, targets, random_state=42):
    X = features.drop(columns=["player_id"], errors="ignore")
    model = lgb.LGBMRegressor(random_state=random_state, verbose=-1)
    model.fit(X, targets)
    return model


def player_game_matrix(events):
    counts = events.groupby(["player_id", "game_id"]).size().reset_index(name="round_count")
    return counts.pivot(index="player_id", columns="game_id", values="round_count").fillna(0)


def top_n_games_per_player(events, n=3):
    counts = events.groupby(["player_id", "game_id"]).size().reset_index(name="cnt")
    counts = counts.sort_values(["player_id", "cnt", "game_id"], ascending=[True, False, True])
    counts["rank"] = counts.groupby("player_id").cumcount() + 1
    return counts[counts["rank"] <= n][["player_id", "rank", "game_id"]]


def recommend_popular_unplayed(events, player_id, n=3):
    global_pop = events.groupby("game_id").size().sort_values(ascending=False)
    played = set(events.loc[events["player_id"] == player_id, "game_id"])
    candidates = [g for g in global_pop.index if g not in played]
    return sorted(candidates, key=lambda g: (-global_pop[g], g))[:n]


def estimate_daily_storage_gb(events_per_day, bytes_per_event=256):
    return events_per_day * bytes_per_event / 1e9


RECOMMENDED_PHASES = [
    "warehouse", "dbt_features", "segmentation_churn_ltv", "recommendations", "feature_store_eval",
]


def next_phase(completed):
    for phase in RECOMMENDED_PHASES:
        if phase not in completed:
            return phase
    return None
