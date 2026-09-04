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
