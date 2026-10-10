#!/usr/bin/env python3
"""Run pytest with reference solutions patched in (maintainer tool)."""

from __future__ import annotations

import inspect
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "_scripts"))

import solutions as sol

CHALLENGE_MAP = {
    ("01_igaming_domain", "validate_rgs_event.py"): ["validate_rgs_event"],
    ("01_igaming_domain", "compute_ggr.py"): ["compute_ggr", "total_ggr"],
    ("01_igaming_domain", "compute_ggr_by_game.py"): ["ggr_by_game"],
    ("02_engagement_metrics", "compute_dau.py"): ["daily_active_users"],
    ("02_engagement_metrics", "compute_wau_mau.py"): ["wau", "mau"],
    ("02_engagement_metrics", "compute_stickiness.py"): ["stickiness"],
    ("03_cohorts_retention", "assign_cohort.py"): ["assign_registration_cohort"],
    ("03_cohorts_retention", "compute_retention.py"): ["d7_retention"],
    ("03_cohorts_retention", "build_cohort_table.py"): ["cohort_retention_table"],
    ("04_session_analytics", "sessionize_events.py"): ["sessionize_by_gap"],
    ("04_session_analytics", "session_duration.py"): ["session_durations"],
    ("04_session_analytics", "ggr_per_session.py"): ["ggr_per_session"],
    ("05_sql_gaming_analytics", "top_games_sql.py"): ["top_games_by_ggr_sql"],
    ("05_sql_gaming_analytics", "player_favorite_game_sql.py"): ["player_favorite_game_sql"],
    ("05_sql_gaming_analytics", "rolling_ggr_sql.py"): ["rolling_7d_ggr_sql"],
    ("06_feature_engineering", "days_since_last_session.py"): ["days_since_last_session"],
    ("06_feature_engineering", "sessions_in_window.py"): ["sessions_7d"],
    ("06_feature_engineering", "build_player_features.py"): ["build_player_features"],
    ("07_player_segmentation", "prepare_segmentation_features.py"): ["prepare_features"],
    ("07_player_segmentation", "kmeans_segment.py"): ["kmeans_segment"],
    ("07_player_segmentation", "profile_segments.py"): ["segment_profile"],
    ("08_churn_prediction", "label_churn.py"): ["label_churn"],
    ("08_churn_prediction", "churn_feature_matrix.py"): ["build_churn_features"],
    ("08_churn_prediction", "train_churn_model.py"): ["train_churn_classifier"],
    ("09_ltv_proxy", "label_future_ggr.py"): ["label_future_ggr"],
    ("09_ltv_proxy", "ltv_feature_matrix.py"): ["ltv_features"],
    ("09_ltv_proxy", "train_ltv_model.py"): ["train_ltv_regressor"],
    ("10_recommendations", "player_game_matrix.py"): ["player_game_matrix"],
    ("10_recommendations", "top_games_per_player.py"): ["top_n_games_per_player"],
    ("10_recommendations", "recommend_popular_games.py"): ["recommend_popular_unplayed"],
    ("11_analytics_architecture", "estimate_storage.py"): ["estimate_daily_storage_gb"],
    ("11_analytics_architecture", "pipeline_phase_order.py"): ["next_phase"],
    ("part_02_pam/01_what_changes", "classify_metric_source.py"): ["classify_metric_source"],
    ("part_02_pam/01_what_changes", "historical_ggr_source.py"): ["is_historical_ggr_source"],
    ("part_02_pam/01_what_changes", "convert_to_eur.py"): ["to_eur"],
    ("part_02_pam/02_activity_and_cohorts", "activity_counts.py"): ["activity_counts"],
    ("part_02_pam/02_activity_and_cohorts", "anchor_retention.py"): ["anchor_retention"],
    ("part_02_pam/02_activity_and_cohorts", "crm_eligible_players.py"): ["crm_eligible_players"],
    ("part_02_pam/03_wallet_revenue", "first_deposit.py"): ["first_deposit"],
    ("part_02_pam/03_wallet_revenue", "paying_users.py"): ["paying_user_count"],
    ("part_02_pam/03_wallet_revenue", "arpu_arppu.py"): ["arpu_arppu"],
    ("part_02_pam/04_bonus_and_ngr", "bonus_cost.py"): ["bonus_cost_per_player"],
    ("part_02_pam/04_bonus_and_ngr", "compute_ngr.py"): ["compute_ngr"],
    ("part_02_pam/04_bonus_and_ngr", "bonus_ggr_share.py"): ["bonus_ggr_share"],
    ("part_02_pam/05_models_and_pipeline", "pam_player_features.py"): [
        "bonus_ggr_share",
        "pam_player_features",
    ],
    ("part_02_pam/05_models_and_pipeline", "label_deposit_churn.py"): ["label_deposit_churn"],
    ("part_02_pam/05_models_and_pipeline", "warehouse_source.py"): ["warehouse_source"],
}


def main() -> int:
    helper_block = "\n\n".join(
        inspect.getsource(getattr(sol, name))
        for name in ("_normalize_day", "_event_days", "_in_day_range")
    )
    needs_helpers = {
        "days_since_last_session.py",
        "sessions_in_window.py",
        "build_player_features.py",
        "churn_feature_matrix.py",
        "ltv_feature_matrix.py",
    }

    backups: dict[Path, str] = {}
    for (mod, fname), funcs in CHALLENGE_MAP.items():
        path = ROOT / mod / "challenges" / fname
        backups[path] = path.read_text()
        header = path.read_text().split("def ")[0].rstrip()
        parts = [header]
        if fname in needs_helpers:
            parts.append(helper_block)
        parts.extend(inspect.getsource(getattr(sol, fn)) for fn in funcs)
        path.write_text("\n\n".join(parts) + "\n")

    result = subprocess.run([sys.executable, "-m", "pytest", "-q"], cwd=ROOT)

    for path, content in backups.items():
        path.write_text(content)

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
