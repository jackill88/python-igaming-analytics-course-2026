import pandas as pd
from shared.testing import load_challenge

kmeans_segment = load_challenge("07_player_segmentation", "kmeans_segment.py").kmeans_segment


def test_kmeans():
    features = pd.DataFrame({"a": [0, 10, 0.1, 9.9], "b": [0, 10, 0.2, 9.8]})
    labels = kmeans_segment(features, n_clusters=2, random_state=42)
    assert len(labels) == 4
    assert labels.nunique() == 2
