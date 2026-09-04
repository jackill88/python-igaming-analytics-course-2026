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
