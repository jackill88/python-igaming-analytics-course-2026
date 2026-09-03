"""DuckDB helpers for SQL challenges."""

from __future__ import annotations

from typing import Any

import duckdb
import pandas as pd


def relation_from_df(conn: duckdb.DuckDBPyConnection, name: str, df: pd.DataFrame) -> None:
    """Register a pandas DataFrame as a DuckDB relation/view."""
    conn.register(name, df)


def query_duckdb(sql: str, tables: dict[str, pd.DataFrame] | None = None) -> pd.DataFrame:
    """Run SQL against optional named DataFrames and return a pandas result."""
    conn = duckdb.connect(database=":memory:")
    try:
        if tables:
            for name, df in tables.items():
                relation_from_df(conn, name, df)
        return conn.execute(sql).fetchdf()
    finally:
        conn.close()


def scalar_query(sql: str, tables: dict[str, pd.DataFrame] | None = None) -> Any:
    """Return the first cell of a SQL query result."""
    df = query_duckdb(sql, tables)
    if df.empty:
        return None
    return df.iloc[0, 0]
