from shared.testing import load_challenge

estimate_daily_storage_gb = load_challenge("11_analytics_architecture", "estimate_storage.py").estimate_daily_storage_gb


def test_storage():
    gb = estimate_daily_storage_gb(1_000_000, bytes_per_event=256)
    assert abs(gb - 0.256) < 0.001
