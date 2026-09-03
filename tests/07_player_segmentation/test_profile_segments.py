import pandas as pd
from shared.testing import load_challenge

segment_profile = load_challenge("07_player_segmentation", "profile_segments.py").segment_profile


def test_profile():
    features = pd.DataFrame({"ggr": [10.0, 20.0, 1.0, 2.0]})
    labels = pd.Series([0, 0, 1, 1])
    out = segment_profile(features, labels)
    assert len(out) == 2
