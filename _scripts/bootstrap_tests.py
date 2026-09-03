#!/usr/bin/env python3
"""Generate all pytest files for course challenges."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


TESTS = {
    "01_igaming_domain/test_validate_rgs_event.py": '''
from shared.testing import load_challenge

validate_rgs_event = load_challenge("01_igaming_domain", "validate_rgs_event.py").validate_rgs_event


def test_valid_event():
    event = {
        "round_id": "r1", "player_id": 1, "session_id": "s1", "game_id": "slots_a",
        "timestamp": "2024-06-01", "bet_amount": 10.0, "win_amount": 0.0,
    }
    ok, errs = validate_rgs_event(event)
    assert ok is True
    assert errs == []


def test_missing_field():
    event = {"round_id": "r1", "player_id": 1}
    ok, errs = validate_rgs_event(event)
    assert ok is False
    assert len(errs) > 0


def test_negative_bet():
    event = {
        "round_id": "r1", "player_id": 1, "session_id": "s1", "game_id": "g",
        "timestamp": "2024-06-01", "bet_amount": -1.0, "win_amount": 0.0,
    }
    ok, errs = validate_rgs_event(event)
    assert ok is False
''',
    "01_igaming_domain/test_compute_ggr.py": '''
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

compute_ggr = load_challenge("01_igaming_domain", "compute_ggr.py").compute_ggr
total_ggr = load_challenge("01_igaming_domain", "compute_ggr.py").total_ggr


def test_compute_ggr_column():
    df = rgs_events_frame()
    out = compute_ggr(df)
    assert "ggr" in out.columns
    assert out.loc[0, "ggr"] == 10.0
    assert out.loc[1, "ggr"] == -10.0


def test_total_ggr():
    df = rgs_events_frame()
    assert total_ggr(df) == 59.0
''',
    "01_igaming_domain/test_compute_ggr_by_game.py": '''
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ggr_by_game = load_challenge("01_igaming_domain", "compute_ggr_by_game.py").ggr_by_game


def test_ggr_by_game():
    out = ggr_by_game(rgs_events_frame())
    assert list(out.columns) == ["game_id", "total_bets", "total_wins", "ggr"]
    assert out.iloc[0]["game_id"] == "slots_a"
    assert out.iloc[0]["ggr"] == 33.0
''',
    "02_engagement_metrics/test_compute_dau.py": '''
import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

daily_active_users = load_challenge("02_engagement_metrics", "compute_dau.py").daily_active_users


def test_dau():
    activity = daily_activity_frame()
    assert daily_active_users(activity, pd.Timestamp("2024-06-01")) == 2
    assert daily_active_users(activity, pd.Timestamp("2024-06-03")) == 2
''',
    "02_engagement_metrics/test_compute_wau_mau.py": '''
import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

mod = load_challenge("02_engagement_metrics", "compute_wau_mau.py")
wau = mod.wau
mau = mod.mau


def test_wau():
    activity = daily_activity_frame()
    assert wau(activity, pd.Timestamp("2024-06-05")) == 3


def test_mau():
    activity = daily_activity_frame()
    assert mau(activity, pd.Timestamp("2024-06-05")) == 4
''',
    "02_engagement_metrics/test_compute_stickiness.py": '''
import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

stickiness = load_challenge("02_engagement_metrics", "compute_stickiness.py").stickiness


def test_stickiness():
    activity = daily_activity_frame()
    ratio = stickiness(activity, pd.Timestamp("2024-06-05"))
    assert 0 < ratio <= 1.0
''',
    "03_cohorts_retention/test_assign_cohort.py": '''
from shared.datasets import players_frame
from shared.testing import load_challenge

assign_registration_cohort = load_challenge("03_cohorts_retention", "assign_cohort.py").assign_registration_cohort


def test_cohort_week():
    out = assign_registration_cohort(players_frame())
    assert "cohort_week" in out.columns
    assert out.loc[out.player_id == 101, "cohort_week"].iloc[0].dayofweek == 0
''',
    "03_cohorts_retention/test_compute_retention.py": '''
import pandas as pd
from shared.datasets import daily_activity_frame, players_frame
from shared.testing import load_challenge

d7_retention = load_challenge("03_cohorts_retention", "compute_retention.py").d7_retention


def test_d7_retention():
    players = players_frame()
    activity = daily_activity_frame()
    rate = d7_retention(players, activity)
    assert 0.0 <= rate <= 1.0
''',
    "03_cohorts_retention/test_build_cohort_table.py": '''
from shared.datasets import daily_activity_frame, players_frame
from shared.testing import load_challenge

build = load_challenge("03_cohorts_retention", "build_cohort_table.py").cohort_retention_table


def test_cohort_table_shape():
    out = build(players_frame(), daily_activity_frame(), [1, 7])
    assert "d1" in out.columns or "d7" in out.columns or len(out.columns) >= 1
''',
    "04_session_analytics/test_sessionize_events.py": '''
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

sessionize_by_gap = load_challenge("04_session_analytics", "sessionize_events.py").sessionize_by_gap


def test_sessionize():
    out = sessionize_by_gap(rgs_events_frame(), gap_minutes=30)
    assert "derived_session_id" in out.columns
    assert out[out.player_id == 101]["derived_session_id"].nunique() >= 1
''',
    "04_session_analytics/test_session_duration.py": '''
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

session_durations = load_challenge("04_session_analytics", "session_duration.py").session_durations


def test_duration():
    out = session_durations(rgs_events_frame())
    assert set(out.columns) >= {"player_id", "session_id", "duration_minutes", "round_count"}
    assert out["duration_minutes"].min() >= 0
''',
    "04_session_analytics/test_ggr_per_session.py": '''
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ggr_per_session = load_challenge("04_session_analytics", "ggr_per_session.py").ggr_per_session


def test_ggr_session():
    out = ggr_per_session(rgs_events_frame())
    assert "ggr" in out.columns
    assert out["ggr"].sum() == 59.0
''',
    "05_sql_gaming_analytics/test_top_games_sql.py": '''
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.sql_helpers import query_duckdb
from shared.testing import load_challenge

top_games_by_ggr_sql = load_challenge("05_sql_gaming_analytics", "top_games_sql.py").top_games_by_ggr_sql


def test_top_games():
    df = rgs_events_frame().rename(columns={"round_id": "round_id"})
    rounds = df[["round_id", "player_id", "game_id", "bet_amount", "win_amount", "timestamp"]]
    sql = top_games_by_ggr_sql()
    result = query_duckdb(sql, {"rounds": rounds})
    assert len(result) <= 3
    assert "game_id" in result.columns
''',
    "05_sql_gaming_analytics/test_player_favorite_game_sql.py": '''
from shared.datasets import rgs_events_frame
from shared.sql_helpers import query_duckdb
from shared.testing import load_challenge

player_favorite_game_sql = load_challenge("05_sql_gaming_analytics", "player_favorite_game_sql.py").player_favorite_game_sql


def test_favorite_game():
    rounds = rgs_events_frame()[["round_id", "player_id", "game_id", "bet_amount", "win_amount", "timestamp"]]
    result = query_duckdb(player_favorite_game_sql(), {"rounds": rounds})
    assert "player_id" in result.columns
    assert "favorite_game" in result.columns
''',
    "05_sql_gaming_analytics/test_rolling_ggr_sql.py": '''
import pandas as pd
from shared.sql_helpers import query_duckdb
from shared.testing import load_challenge

rolling_7d_ggr_sql = load_challenge("05_sql_gaming_analytics", "rolling_ggr_sql.py").rolling_7d_ggr_sql


def test_rolling_ggr():
    daily = pd.DataFrame({
        "activity_date": pd.date_range("2024-06-01", periods=10),
        "ggr": [10.0] * 10,
    })
    result = query_duckdb(rolling_7d_ggr_sql(), {"daily_ggr": daily})
    assert "rolling_7d_ggr" in result.columns
''',
    "06_feature_engineering/test_days_since_last_session.py": '''
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

days_since_last_session = load_challenge("06_feature_engineering", "days_since_last_session.py").days_since_last_session


def test_days_since():
    out = days_since_last_session(rgs_events_frame(), pd.Timestamp("2024-06-04"))
    assert "days_since_last_session" in out.columns
    assert (out["days_since_last_session"] >= 0).all()
''',
    "06_feature_engineering/test_sessions_in_window.py": '''
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

sessions_7d = load_challenge("06_feature_engineering", "sessions_in_window.py").sessions_7d


def test_sessions_7d():
    out = sessions_7d(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    assert "sessions_7d" in out.columns
''',
    "06_feature_engineering/test_build_player_features.py": '''
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

build_player_features = load_challenge("06_feature_engineering", "build_player_features.py").build_player_features


def test_player_features():
    out = build_player_features(rgs_events_frame(), pd.Timestamp("2024-06-03"))
    cols = {"player_id", "sessions_7d", "avg_bet_7d", "ggr_7d", "favorite_game_7d"}
    assert cols <= set(out.columns)
''',
    "07_player_segmentation/test_prepare_segmentation_features.py": '''
import pandas as pd
from shared.testing import load_challenge

prepare_features = load_challenge("07_player_segmentation", "prepare_segmentation_features.py").prepare_features


def test_prepare():
    df = pd.DataFrame({"player_id": [1, 2], "ggr": [10.0, None], "sessions": [5, 3]})
    out = prepare_features(df, ["ggr", "sessions"])
    assert out.shape == (2, 2)
    assert out.isna().sum().sum() == 0
''',
    "07_player_segmentation/test_kmeans_segment.py": '''
import pandas as pd
from shared.testing import load_challenge

kmeans_segment = load_challenge("07_player_segmentation", "kmeans_segment.py").kmeans_segment


def test_kmeans():
    features = pd.DataFrame({"a": [0, 10, 0.1, 9.9], "b": [0, 10, 0.2, 9.8]})
    labels = kmeans_segment(features, n_clusters=2, random_state=42)
    assert len(labels) == 4
    assert labels.nunique() == 2
''',
    "07_player_segmentation/test_profile_segments.py": '''
import pandas as pd
from shared.testing import load_challenge

segment_profile = load_challenge("07_player_segmentation", "profile_segments.py").segment_profile


def test_profile():
    features = pd.DataFrame({"ggr": [10.0, 20.0, 1.0, 2.0]})
    labels = pd.Series([0, 0, 1, 1])
    out = segment_profile(features, labels)
    assert len(out) == 2
''',
    "08_churn_prediction/test_label_churn.py": '''
import pandas as pd
from shared.datasets import daily_activity_frame
from shared.testing import load_challenge

label_churn = load_challenge("08_churn_prediction", "label_churn.py").label_churn


def test_label():
    activity = daily_activity_frame()
    out = label_churn(activity, pd.Timestamp("2024-06-01"), horizon_days=30)
    assert "inactive_next_30_days" in out.columns
''',
    "08_churn_prediction/test_churn_feature_matrix.py": '''
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

build_churn_features = load_challenge("08_churn_prediction", "churn_feature_matrix.py").build_churn_features


def test_churn_features():
    out = build_churn_features(rgs_events_frame(), pd.Timestamp("2024-06-05"))
    assert "sessions_30d" in out.columns
''',
    "08_churn_prediction/test_train_churn_model.py": '''
import pandas as pd
from shared.testing import load_challenge

train_churn_classifier = load_challenge("08_churn_prediction", "train_churn_model.py").train_churn_classifier


def test_train():
    features = pd.DataFrame({
        "player_id": [1, 2, 3, 4],
        "sessions_30d": [10, 2, 8, 1],
        "avg_bet_30d": [5.0, 1.0, 4.0, 2.0],
        "ggr_30d": [100.0, -10.0, 50.0, -5.0],
        "days_since_last_session": [1, 20, 2, 25],
    })
    labels = pd.Series([0, 1, 0, 1])
    model = train_churn_classifier(features, labels, random_state=42)
    assert hasattr(model, "predict")
''',
    "09_ltv_proxy/test_label_future_ggr.py": '''
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

label_future_ggr = load_challenge("09_ltv_proxy", "label_future_ggr.py").label_future_ggr


def test_future_ggr():
    out = label_future_ggr(rgs_events_frame(), pd.Timestamp("2024-06-01"), horizon_days=30)
    assert "future_ggr_30d" in out.columns
''',
    "09_ltv_proxy/test_ltv_feature_matrix.py": '''
import pandas as pd
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

ltv_features = load_challenge("09_ltv_proxy", "ltv_feature_matrix.py").ltv_features


def test_ltv_features():
    out = ltv_features(rgs_events_frame(), pd.Timestamp("2024-06-05"))
    assert "ggr_30d" in out.columns
''',
    "09_ltv_proxy/test_train_ltv_model.py": '''
import pandas as pd
from shared.testing import load_challenge

train_ltv_regressor = load_challenge("09_ltv_proxy", "train_ltv_model.py").train_ltv_regressor


def test_train_ltv():
    features = pd.DataFrame({
        "player_id": [1, 2, 3],
        "ggr_30d": [10.0, 20.0, 5.0],
        "sessions_30d": [5, 10, 2],
        "avg_bet_30d": [2.0, 4.0, 1.0],
    })
    targets = pd.Series([15.0, 30.0, 8.0])
    model = train_ltv_regressor(features, targets, random_state=42)
    assert hasattr(model, "predict")
''',
    "10_recommendations/test_player_game_matrix.py": '''
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

player_game_matrix = load_challenge("10_recommendations", "player_game_matrix.py").player_game_matrix


def test_matrix():
    out = player_game_matrix(rgs_events_frame())
    assert out.loc[101, "slots_a"] >= 1
    assert out.fillna(0).min().min() >= 0
''',
    "10_recommendations/test_top_games_per_player.py": '''
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

top_n_games_per_player = load_challenge("10_recommendations", "top_games_per_player.py").top_n_games_per_player


def test_top_n():
    out = top_n_games_per_player(rgs_events_frame(), n=2)
    assert set(out.columns) >= {"player_id", "rank", "game_id"}
''',
    "10_recommendations/test_recommend_popular_games.py": '''
from shared.datasets import rgs_events_frame
from shared.testing import load_challenge

recommend_popular_unplayed = load_challenge("10_recommendations", "recommend_popular_games.py").recommend_popular_unplayed


def test_recommend():
    recs = recommend_popular_unplayed(rgs_events_frame(), player_id=101, n=2)
    assert len(recs) <= 2
    assert "slots_a" not in recs or len(recs) > 0
''',
    "11_analytics_architecture/test_estimate_storage.py": '''
from shared.testing import load_challenge

estimate_daily_storage_gb = load_challenge("11_analytics_architecture", "estimate_storage.py").estimate_daily_storage_gb


def test_storage():
    gb = estimate_daily_storage_gb(1_000_000, bytes_per_event=256)
    assert abs(gb - 0.256) < 0.001
''',
    "11_analytics_architecture/test_pipeline_phase_order.py": '''
from shared.testing import load_challenge

next_phase = load_challenge("11_analytics_architecture", "pipeline_phase_order.py").next_phase


def test_next_phase():
    assert next_phase([]) == "warehouse"
    assert next_phase(["warehouse"]) == "dbt_features"
    assert next_phase(["warehouse", "dbt_features", "segmentation_churn_ltv", "recommendations", "feature_store_eval"]) is None
''',
}


if __name__ == "__main__":
    for rel, content in TESTS.items():
        write(ROOT / "tests" / rel, content)
    print(f"Generated {len(TESTS)} test files")
