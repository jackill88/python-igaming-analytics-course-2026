"""Reusable sample DataFrames for iGaming challenges and tests."""

from __future__ import annotations

import pandas as pd


def rgs_events_frame() -> pd.DataFrame:
    """Gameplay rounds from the Remote Gaming Server."""
    return pd.DataFrame(
        {
            "round_id": ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10"],
            "player_id": [101, 101, 101, 102, 102, 103, 103, 103, 104, 104],
            "session_id": ["s1", "s1", "s1", "s2", "s2", "s3", "s3", "s3", "s4", "s4"],
            "game_id": ["slots_a", "slots_a", "roulette_b", "slots_a", "blackjack_c",
                        "slots_a", "slots_a", "roulette_b", "slots_a", "roulette_b"],
            "timestamp": pd.to_datetime(
                [
                    "2024-06-01 10:00:00",
                    "2024-06-01 10:05:00",
                    "2024-06-01 10:35:00",
                    "2024-06-01 11:00:00",
                    "2024-06-01 11:45:00",
                    "2024-06-02 09:00:00",
                    "2024-06-02 09:15:00",
                    "2024-06-02 10:00:00",
                    "2024-06-03 14:00:00",
                    "2024-06-03 14:30:00",
                ]
            ),
            "bet_amount": [10.0, 5.0, 20.0, 15.0, 25.0, 8.0, 12.0, 30.0, 50.0, 10.0],
            "win_amount": [0.0, 15.0, 0.0, 0.0, 50.0, 0.0, 24.0, 0.0, 100.0, 0.0],
        }
    )


def players_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "player_id": [101, 102, 103, 104, 105],
            "registration_date": pd.to_datetime(
                ["2024-05-01", "2024-05-01", "2024-05-15", "2024-06-01", "2024-06-10"]
            ),
            "country": ["UK", "DE", "UK", "SE", "NO"],
        }
    )


def games_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "game_id": ["slots_a", "roulette_b", "blackjack_c"],
            "game_name": ["Lucky Slots", "Euro Roulette", "Classic Blackjack"],
            "category": ["slots", "table", "table"],
            "provider": ["provider_x", "provider_y", "provider_x"],
        }
    )


def daily_activity_frame() -> pd.DataFrame:
    """Player activity dates for engagement metrics."""
    return pd.DataFrame(
        {
            "player_id": [101, 101, 101, 102, 102, 103, 104],
            "activity_date": pd.to_datetime(
                [
                    "2024-06-01",
                    "2024-06-02",
                    "2024-06-05",
                    "2024-06-01",
                    "2024-06-03",
                    "2024-06-02",
                    "2024-06-03",
                ]
            ),
        }
    )


def player_rounds_extended_frame() -> pd.DataFrame:
    """Extended rounds for feature engineering and ML modules."""
    rows = []
    base_date = pd.Timestamp("2024-05-01")
    for player_id in range(1, 21):
        for day_offset in range(30):
            if (player_id + day_offset) % 3 == 0:
                continue
            ts = base_date + pd.Timedelta(days=day_offset, hours=player_id % 12)
            bet = 5.0 + (player_id % 5) * 2
            win = bet * 0.9 if day_offset % 7 == 0 else 0.0
            rows.append(
                {
                    "round_id": f"p{player_id}_d{day_offset}",
                    "player_id": player_id,
                    "session_id": f"p{player_id}_s{day_offset // 3}",
                    "game_id": ["slots_a", "roulette_b", "blackjack_c"][player_id % 3],
                    "timestamp": ts,
                    "bet_amount": bet,
                    "win_amount": win,
                }
            )
    return pd.DataFrame(rows)


def pam_fx_rates_frame() -> pd.DataFrame:
    """EUR per one unit of customer currency. EUR is the system currency."""
    return pd.DataFrame(
        {
            "currency": ["EUR", "GBP", "SEK"],
            "eur_per_unit": [1.0, 1.17, 0.09],
        }
    )


def pam_customers_frame() -> pd.DataFrame:
    """Teaching projection of service-customers."""
    return pd.DataFrame(
        {
            "cid": [101, 102, 103, 104, 105],
            "brand_id": ["brand_a", "brand_a", "brand_a", "brand_b", "brand_a"],
            "registered_at": pd.to_datetime(
                ["2024-05-01", "2024-05-01", "2024-05-15", "2024-06-01", "2024-06-10"]
            ),
            "currency": ["GBP", "EUR", "GBP", "SEK", "EUR"],
            "status": ["active", "active", "self_excluded", "active", "closed"],
            "marketing_email_allowed": [1, 1, 0, 1, 0],
        }
    )


def pam_login_sessions_frame() -> pd.DataFrame:
    """Successful login rows. Grain: one row per login session."""
    return pd.DataFrame(
        {
            "session_id": ["l1", "l2", "l3", "l4", "l5"],
            "cid": [101, 101, 102, 103, 104],
            "login_at": pd.to_datetime(
                [
                    "2024-06-01 10:00:00",
                    "2024-06-02 10:00:00",
                    "2024-06-01 11:00:00",
                    "2024-06-02 09:00:00",
                    "2024-06-03 12:00:00",
                ]
            ),
        }
    )


def pam_transactions_frame() -> pd.DataFrame:
    """Wallet transactions. Only status 'approved' and tx_type 'deposit' count as a successful deposit."""
    return pd.DataFrame(
        {
            "transaction_id": ["t1", "t2", "t3", "t4", "t5", "t6", "t7"],
            "cid": [101, 101, 101, 102, 103, 105, 101],
            "brand_id": ["brand_a", "brand_a", "brand_a", "brand_a", "brand_a", "brand_a", "brand_a"],
            "tx_type": ["deposit", "deposit", "deposit", "deposit", "deposit", "deposit", "withdrawal"],
            "status": ["approved", "approved", "open", "approved", "approved", "rejected", "approved"],
            "amount": [100.0, 50.0, 20.0, 80.0, 40.0, 25.0, 10.0],
            "currency": ["GBP", "GBP", "GBP", "EUR", "GBP", "EUR", "GBP"],
            "amount_eur": [117.0, 58.5, 23.4, 80.0, 46.8, 25.0, 11.7],
            "created_at": pd.to_datetime(
                [
                    "2024-05-02 09:00:00",
                    "2024-06-01 12:00:00",
                    "2024-06-10 12:00:00",
                    "2024-05-20 15:00:00",
                    "2024-05-16 08:00:00",
                    "2024-06-11 08:00:00",
                    "2024-06-05 08:00:00",
                ]
            ),
        }
    )


def pam_game_rounds_frame() -> pd.DataFrame:
    """Casino rounds with cash and bonus stake already converted to EUR.

    GGR on a round is (cash_bet_eur + bonus_bet_eur) - win_amount_eur.
    """
    return pd.DataFrame(
        {
            "round_id": ["r1", "r2", "r3", "r4", "r5", "r6"],
            "cid": [101, 101, 101, 101, 102, 103],
            "brand_id": ["brand_a", "brand_a", "brand_a", "brand_a", "brand_a", "brand_a"],
            "session_id": ["s1", "s1", "s2", "s3", "s4", "s5"],
            "game_id": ["slots_a", "slots_a", "slots_a", "roulette_b", "slots_a", "slots_a"],
            "provider": ["diger_rgs", "diger_rgs", "pragmatic", "diger_rgs", "pragmatic", "ezugi"],
            "cash_bet_eur": [10.0, 0.0, 10.0, 5.0, 20.0, 0.0],
            "bonus_bet_eur": [0.0, 0.0, 0.0, 5.0, 10.0, 40.0],
            "win_amount_eur": [0.0, 0.0, 0.0, 4.0, 15.0, 10.0],
            "event_ts": pd.to_datetime(
                [
                    "2024-05-02 18:00:00",
                    "2024-05-03 18:00:00",
                    "2024-06-01 18:00:00",
                    "2024-06-08 18:00:00",
                    "2024-05-08 18:00:00",
                    "2024-05-16 18:00:00",
                ]
            ),
        }
    )


def pam_bonus_claims_frame() -> pd.DataFrame:
    """Wallet bonus claims. bonus_cost_eur is the cost to include in NGR, in system currency."""
    return pd.DataFrame(
        {
            "claim_id": ["c1", "c2", "c3"],
            "cid": [101, 102, 103],
            "bonus_plan": ["retention_bonus", "first_deposit", "no_deposit"],
            "bonus_cost_eur": [10.0, 20.0, 30.0],
            "claimed_at": pd.to_datetime(["2024-05-02", "2024-05-20", "2024-05-16"]),
        }
    )
