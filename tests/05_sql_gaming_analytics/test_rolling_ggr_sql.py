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
