import pandas as pd
from shared.testing import load_challenge

segment_profile = load_challenge("07_player_segmentation", "profile_segments.py").segment_profile


def test_profile_means_by_cluster():
    features = pd.DataFrame({"ggr_30d": [100.0, 102.0, 10.0, 12.0], "sessions_30d": [20, 22, 2, 3]})
    labels = pd.Series([0, 0, 1, 1])
    profile = segment_profile(features, labels)
    assert abs(profile.loc[0, "ggr_30d"] - 101.0) < 1e-6
    assert abs(profile.loc[1, "ggr_30d"] - 11.0) < 1e-6


def test_profile_column_count():
    features = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0]})
    labels = pd.Series([0, 1])
    profile = segment_profile(features, labels)
    assert list(profile.columns) == ["a", "b"]
    assert len(profile) == 2
