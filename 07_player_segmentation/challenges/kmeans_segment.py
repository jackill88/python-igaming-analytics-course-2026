"""
Challenge: K-Means Segment Players
Module 07: Player Segmentation

Run: pytest tests/07_player_segmentation/test_kmeans_segment.py -v
"""

import pandas as pd
from sklearn.cluster import KMeans


def kmeans_segment(features: pd.DataFrame, n_clusters: int = 3, random_state: int = 42) -> pd.Series:
    """Return Series of cluster labels indexed like features."""
    pass
