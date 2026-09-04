# Clustering Algorithms

## K-Means

- **Pros:** Fast, simple, scales well
- **Cons:** Assumes spherical clusters; pick K manually
- **Use when:** Rough behavioral groupings, large player base

```python
from sklearn.cluster import KMeans
KMeans(n_clusters=4, random_state=42, n_init=10)
```

## Gaussian Mixture Models (GMM)

- Soft cluster assignments (probability per segment)
- Better for overlapping groups

## HDBSCAN

- Finds arbitrary shapes; auto-estimates cluster count
- Labels noise points as −1
- Slower; great for exploration

## Preprocessing

1. Select numeric features
2. Handle nulls (fill 0 or median)
3. **Standardize** (`StandardScaler`) — critical for K-Means

## Choosing K

- Elbow method (inertia vs K)
- Silhouette score
- Business interpretability of profiles

## Key takeaway

Clustering finds **structure** — you still must **name segments** and validate with domain experts.
