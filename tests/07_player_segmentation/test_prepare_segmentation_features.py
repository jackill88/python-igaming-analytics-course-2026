import pandas as pd
from shared.testing import load_challenge

prepare_features = load_challenge(
    "07_player_segmentation", "prepare_segmentation_features.py"
).prepare_features


def test_prepare_features_selects_and_fills():
    df = pd.DataFrame(
        {
            "player_id": [1, 2],
            "sessions_30d": [10.0, None],
            "ggr_30d": [100.0, -5.0],
            "country": ["UK", "DE"],
        }
    )
    out = prepare_features(df, ["sessions_30d", "ggr_30d"])
    assert list(out.columns) == ["sessions_30d", "ggr_30d"]
    assert out.loc[1, "sessions_30d"] == 0.0
    assert out.isna().sum().sum() == 0


def test_prepare_features_shape():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "label": ["x", "y"]})
    out = prepare_features(df, ["a", "b"])
    assert out.shape == (2, 2)
