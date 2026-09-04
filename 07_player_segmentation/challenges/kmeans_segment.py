"""
Challenge: K-Means Segment Players
Module 07: Player Segmentation

Theory: theory/02_clustering_algorithms.md

Inputs:
  features — numeric DataFrame (one row per player)
  n_clusters — k (default 3)
  random_state — reproducibility (default 42)

Outputs:
  Series of integer cluster labels indexed like features

Edge cases:
  - n_clusters must not exceed n_samples
  - Well-separated blobs → nunique() == n_clusters

Example:
  >>> kmeans_segment(features, n_clusters=2, random_state=42).nunique()
  2

Run: pytest tests/07_player_segmentation/test_kmeans_segment.py -v
"""

import pandas as pd
from sklearn.cluster import KMeans


def kmeans_segment(features: pd.DataFrame, n_clusters: int = 3, random_state: int = 42) -> pd.Series:
    """Return Series of cluster labels indexed like features."""
    pass
