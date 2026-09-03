import pandas as pd
from shared.testing import load_challenge

prepare_features = load_challenge("07_player_segmentation", "prepare_segmentation_features.py").prepare_features


def test_prepare():
    df = pd.DataFrame({"player_id": [1, 2], "ggr": [10.0, None], "sessions": [5, 3]})
    out = prepare_features(df, ["ggr", "sessions"])
    assert out.shape == (2, 2)
    assert out.isna().sum().sum() == 0
