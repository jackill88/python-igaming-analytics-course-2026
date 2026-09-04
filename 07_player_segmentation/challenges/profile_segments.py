"""
Challenge: Profile Segments
Module 07: Player Segmentation

Theory: theory/03_segment_profiling.md

Inputs:
  features — numeric feature DataFrame
  labels — cluster assignment Series (same index)

Outputs:
  Mean of each numeric column grouped by segment label

Edge cases:
  - Index of labels aligns with features rows
  - Single-column features still produce valid profile

Example:
  >>> profile = segment_profile(features, labels)
  >>> profile.loc[0, "ggr_30d"]  # mean GGR for cluster 0

Run: pytest tests/07_player_segmentation/test_profile_segments.py -v
"""

import pandas as pd


def segment_profile(features: pd.DataFrame, labels: pd.Series) -> pd.DataFrame:
    """Return mean of each numeric column grouped by segment label."""
    pass
