import pandas as pd
from shared.testing import load_challenge

kmeans_segment = load_challenge("07_player_segmentation", "kmeans_segment.py").kmeans_segment


def test_kmeans_label_count():
    features = pd.DataFrame({"a": [0, 10, 0.1, 9.9], "b": [0, 10, 0.2, 9.8]})
    labels = kmeans_segment(features, n_clusters=2, random_state=42)
    assert len(labels) == 4
    assert labels.nunique() == 2


def test_kmeans_index_aligned():
    features = pd.DataFrame({"x": [1, 2, 3, 4]}, index=[10, 20, 30, 40])
    labels = kmeans_segment(features, n_clusters=2, random_state=42)
    assert list(labels.index) == [10, 20, 30, 40]


def test_kmeans_three_clusters():
    features = pd.DataFrame({"a": [0, 10, 20, 0.1, 9.9, 20.1], "b": [0, 10, 20, 0.2, 9.8, 19.9]})
    labels = kmeans_segment(features, n_clusters=3, random_state=42)
    assert labels.nunique() == 3
