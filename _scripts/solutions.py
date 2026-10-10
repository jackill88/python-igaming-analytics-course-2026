#!/usr/bin/env python3
"""Reference solutions — used to verify tests; not part of the student path."""

from __future__ import annotations

import pandas as pd
from sklearn.cluster import KMeans
import lightgbm as lgb


REQUIRED_FIELDS = {"round_id", "player_id", "session_id", "game_id", "timestamp", "bet_amount", "win_amount"}


def _normalize_day(ts: pd.Timestamp) -> pd.Timestamp:
    return pd.Timestamp(ts).normalize()


def _event_days(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series).dt.normalize()


def _in_day_range(events: pd.DataFrame, feature_date: pd.Timestamp, window_days: int) -> pd.DataFrame:
    end_day = _normalize_day(feature_date)
    start_day = end_day - pd.Timedelta(days=window_days - 1)
    days = _event_days(events["timestamp"])
    return events.loc[(days >= start_day) & (days <= end_day)].copy()


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
    feature_day = _normalize_day(feature_date)
    hist = events.loc[_event_days(events["timestamp"]) < feature_day].copy()
    last = hist.groupby("player_id")["timestamp"].max().reset_index()
    last["days_since_last_session"] = (
        feature_day - _event_days(last["timestamp"])
    ).dt.days
    return last[["player_id", "days_since_last_session"]]


def sessions_7d(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    window = _in_day_range(events, feature_date, window_days=7)
    return window.groupby("player_id")["session_id"].nunique().reset_index(name="sessions_7d")


def build_player_features(events: pd.DataFrame, feature_date: pd.Timestamp) -> pd.DataFrame:
    window = _in_day_range(events, feature_date, window_days=7)
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
    hist = _in_day_range(events, snapshot_date, window_days=30)
    snapshot_day = _normalize_day(snapshot_date)
    last = (
        events.loc[_event_days(events["timestamp"]) <= snapshot_day]
        .groupby("player_id")["timestamp"]
        .max()
    )
    agg = hist.groupby("player_id").agg(
        sessions_30d=("session_id", "nunique"),
        avg_bet_30d=("bet_amount", "mean"),
        ggr_30d=("bet_amount", lambda s: (s - hist.loc[s.index, "win_amount"]).sum()),
    )
    agg["days_since_last_session"] = (
        snapshot_day - _event_days(last)
    ).dt.days
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
    window = _in_day_range(events, snapshot_date, window_days=30)
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


def classify_metric_source(metric: str) -> str:
    sources = {
        "login_dau": "service-customers",
        "kyc_status": "service-customers",
        "deposits": "service-wallet",
        "bonus_claims": "service-wallet",
        "game_rounds": "service-casino",
        "free_spins": "service-casino",
        "bonus_definitions": "service-offerings",
        "messages_sent": "service-communications",
        "daily_gaming_activity": "service-bo-reports",
    }
    return sources.get(metric, "unknown")


def is_historical_ggr_source(table_name: str) -> bool:
    return table_name in {"game_rounds", "transactions"}


def to_eur(amount: float, currency: str, rates: pd.DataFrame) -> float:
    match = rates.loc[rates["currency"] == currency, "eur_per_unit"]
    if match.empty:
        raise KeyError(currency)
    return float(amount) * float(match.iloc[0])


def activity_counts(logins, rounds, transactions, as_of):
    day = pd.Timestamp(as_of).normalize()
    login_days = pd.to_datetime(logins["login_at"]).dt.normalize()
    play_days = pd.to_datetime(rounds["event_ts"]).dt.normalize()
    created = pd.to_datetime(transactions["created_at"]).dt.normalize()
    deposits = transactions[
        (transactions["tx_type"] == "deposit")
        & (transactions["status"] == "approved")
        & (created == day)
    ]
    return {
        "login": int(logins.loc[login_days == day, "cid"].nunique()),
        "play": int(rounds.loc[play_days == day, "cid"].nunique()),
        "deposit": int(deposits["cid"].nunique()),
    }


def anchor_retention(customers, rounds, transactions, anchor, offset_days):
    if anchor == "registration":
        anchors = customers[["cid"]].copy()
        anchors["anchor_date"] = pd.to_datetime(customers["registered_at"]).dt.normalize().to_numpy()
    elif anchor == "ftd":
        approved = transactions[
            (transactions["tx_type"] == "deposit") & (transactions["status"] == "approved")
        ].copy()
        if approved.empty:
            return 0.0
        approved["created_day"] = pd.to_datetime(approved["created_at"]).dt.normalize()
        anchors = approved.groupby("cid", as_index=False)["created_day"].min()
        anchors = anchors.rename(columns={"created_day": "anchor_date"})
    else:
        raise ValueError(anchor)
    if anchors.empty:
        return 0.0
    play = rounds[["cid", "event_ts"]].copy()
    play["play_day"] = pd.to_datetime(play["event_ts"]).dt.normalize()
    anchors = anchors.copy()
    anchors["target"] = anchors["anchor_date"] + pd.to_timedelta(offset_days, unit="D")
    merged = anchors.merge(play, on="cid", how="left")
    retained = merged.loc[merged["play_day"] == merged["target"], "cid"].nunique()
    return float(retained) / float(anchors["cid"].nunique())


def crm_eligible_players(customers):
    mask = (customers["status"] == "active") & (customers["marketing_email_allowed"] == 1)
    return customers.loc[mask, ["cid"]].sort_values("cid").reset_index(drop=True)


def first_deposit(transactions):
    columns = ["cid", "first_deposit_at", "amount_eur"]
    approved = transactions[
        (transactions["tx_type"] == "deposit") & (transactions["status"] == "approved")
    ].copy()
    if approved.empty:
        return pd.DataFrame(columns=columns)
    approved = approved.sort_values(["cid", "created_at", "transaction_id"])
    first = approved.drop_duplicates("cid", keep="first")
    out = first[["cid", "created_at", "amount_eur"]].rename(columns={"created_at": "first_deposit_at"})
    return out.sort_values("cid").reset_index(drop=True)


def paying_user_count(transactions) -> int:
    approved = transactions[
        (transactions["tx_type"] == "deposit") & (transactions["status"] == "approved")
    ]
    return int(approved["cid"].nunique())


def arpu_arppu(revenue, active_cids, transactions):
    total = float(revenue["revenue_eur"].sum()) if len(revenue) else 0.0
    active = len(set(active_cids))
    paying = int(
        transactions.loc[
            (transactions["tx_type"] == "deposit") & (transactions["status"] == "approved"),
            "cid",
        ].nunique()
    ) if len(transactions) else 0
    arpu = total / active if active else 0.0
    arppu = total / paying if paying else 0.0
    return arpu, arppu


def bonus_cost_per_player(claims):
    columns = ["cid", "bonus_cost_eur"]
    if claims.empty:
        return pd.DataFrame(columns=columns)
    out = claims.groupby("cid", as_index=False)["bonus_cost_eur"].sum()
    return out.sort_values("cid").reset_index(drop=True)


def compute_ngr(rounds, claims, provider_fee_rate, tax_rate):
    columns = ["cid", "ggr_eur", "bonus_cost_eur", "provider_fee_eur", "tax_eur", "ngr_eur"]
    if rounds.empty:
        ggr = pd.DataFrame(columns=["cid", "ggr_eur", "stake_eur"])
    else:
        tmp = rounds.copy()
        tmp["stake_eur"] = tmp["cash_bet_eur"] + tmp["bonus_bet_eur"]
        tmp["ggr_eur"] = tmp["stake_eur"] - tmp["win_amount_eur"]
        ggr = tmp.groupby("cid", as_index=False).agg(
            ggr_eur=("ggr_eur", "sum"),
            stake_eur=("stake_eur", "sum"),
        )
    if claims.empty:
        costs = pd.DataFrame(columns=["cid", "bonus_cost_eur"])
    else:
        costs = claims.groupby("cid", as_index=False)["bonus_cost_eur"].sum()
    merged = ggr.merge(costs, on="cid", how="outer")
    if merged.empty:
        return pd.DataFrame(columns=columns)
    for col in ("ggr_eur", "stake_eur", "bonus_cost_eur"):
        merged[col] = pd.to_numeric(merged[col], errors="coerce").fillna(0.0)
    merged["provider_fee_eur"] = merged["stake_eur"] * provider_fee_rate
    merged["tax_eur"] = merged["ggr_eur"] * tax_rate
    merged["ngr_eur"] = (
        merged["ggr_eur"]
        - merged["bonus_cost_eur"]
        - merged["provider_fee_eur"]
        - merged["tax_eur"]
    )
    return merged[columns].sort_values("cid").reset_index(drop=True)


def bonus_ggr_share(rounds):
    columns = ["cid", "ggr_eur", "bonus_ggr_eur", "bonus_ggr_share"]
    if rounds.empty:
        return pd.DataFrame(columns=columns)
    tmp = rounds.copy()
    tmp["stake_eur"] = tmp["cash_bet_eur"] + tmp["bonus_bet_eur"]
    tmp["ggr_eur"] = tmp["stake_eur"] - tmp["win_amount_eur"]
    agg = tmp.groupby("cid", as_index=False).agg(
        ggr_eur=("ggr_eur", "sum"),
        stake_eur=("stake_eur", "sum"),
        bonus_stake_eur=("bonus_bet_eur", "sum"),
    )
    agg["bonus_ggr_share"] = 0.0
    positive = agg["stake_eur"] > 0
    agg.loc[positive, "bonus_ggr_share"] = (
        agg.loc[positive, "bonus_stake_eur"] / agg.loc[positive, "stake_eur"]
    )
    agg["bonus_ggr_eur"] = agg["ggr_eur"] * agg["bonus_ggr_share"]
    return agg[columns].sort_values("cid").reset_index(drop=True)


def pam_player_features(customers, transactions, rounds, feature_date):
    feature_day = pd.Timestamp(feature_date).normalize()
    start = feature_day - pd.Timedelta(days=29)
    approved = transactions[
        (transactions["tx_type"] == "deposit") & (transactions["status"] == "approved")
    ].copy()
    approved["day"] = pd.to_datetime(approved["created_at"]).dt.normalize()
    played = rounds.copy()
    played["day"] = pd.to_datetime(played["event_ts"]).dt.normalize()
    hist = played.loc[played["day"] <= feature_day]
    shares = (
        bonus_ggr_share(hist).set_index("cid")["bonus_ggr_share"]
        if len(hist)
        else pd.Series(dtype=float)
    )
    rows = []
    for cid in customers["cid"]:
        cust = customers.loc[customers["cid"] == cid].iloc[0]
        deps = approved.loc[approved["cid"] == cid]
        deps_asof = deps.loc[deps["day"] <= feature_day]
        if deps_asof.empty:
            days_since = pd.NA
        else:
            days_since = int((feature_day - deps_asof["day"].min()).days)
        deposits_30d = int(((deps["day"] >= start) & (deps["day"] <= feature_day)).sum())
        share = float(shares.loc[cid]) if cid in shares.index else 0.0
        eligible = int(cust["status"] == "active" and int(cust["marketing_email_allowed"]) == 1)
        rows.append(
            {
                "cid": cid,
                "days_since_ftd": days_since,
                "deposits_30d": deposits_30d,
                "bonus_ggr_share": share,
                "crm_eligible": eligible,
            }
        )
    return pd.DataFrame(rows)


def label_deposit_churn(transactions, snapshot_date, horizon_days=30):
    columns = ["cid", "no_deposit_next_30_days"]
    snapshot = pd.Timestamp(snapshot_date).normalize()
    start = snapshot - pd.Timedelta(days=29)
    end = snapshot + pd.Timedelta(days=horizon_days)
    approved = transactions[
        (transactions["tx_type"] == "deposit") & (transactions["status"] == "approved")
    ].copy()
    if approved.empty:
        return pd.DataFrame(columns=columns)
    approved["day"] = pd.to_datetime(approved["created_at"]).dt.normalize()
    recent = approved[(approved["day"] >= start) & (approved["day"] <= snapshot)]
    future_ids = set(
        approved.loc[(approved["day"] > snapshot) & (approved["day"] <= end), "cid"]
    )
    rows = [
        {"cid": cid, "no_deposit_next_30_days": int(cid not in future_ids)}
        for cid in sorted(recent["cid"].unique())
    ]
    return pd.DataFrame(rows, columns=columns)


def warehouse_source(metric: str):
    if metric == "realtime_balance_push":
        return None
    sources = {
        "player_identity": "customers",
        "login_activity": "login_sessions",
        "historical_ggr": "game_rounds",
        "deposits": "transactions",
        "bonus_cost": "bonuses_claimed",
        "bonus_catalogue": "bonuses",
        "reconciliation_check": "bo_reports",
    }
    if metric not in sources:
        raise KeyError(metric)
    return sources[metric]
