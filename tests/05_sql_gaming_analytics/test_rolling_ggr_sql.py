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
