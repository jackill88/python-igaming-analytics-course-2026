# Batch vs Real-Time ML

## Batch predictions (start here)

**Use for:** churn, segmentation, LTV proxy, daily game rec lists

```
Nightly: features → model → predictions table → CRM export
```

Latency: hours. Infrastructure: warehouse + Python job + cron/Airflow.

## Real-time predictions

**Use for:** in-session game recommendations, responsible gaming alerts, dynamic lobby

```
Event → feature lookup (Redis) → model API → response < 100ms
```

Requires: online feature serving, model API, monitoring.

## Decision matrix

| Question | Batch | Real-time |
|----------|-------|-----------|
| Action waits for user session? | No | Yes |
| Features change second-by-second? | Rarely | Often |
| CRM email next morning OK? | Yes | — |

## Recommended path

1. Batch churn + segmentation (prove ROI)
2. Batch recommendations in email/lobby tile
3. Evaluate real-time only if in-session lift justifies cost

## Key takeaway

**Do not** start with a feature store or real-time inference — validate use cases in batch first.
