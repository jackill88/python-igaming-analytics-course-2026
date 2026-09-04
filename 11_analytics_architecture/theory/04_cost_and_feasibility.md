# Cost and Feasibility

Stakeholders need **numbers**, not architecture diagrams alone.

## Storage estimate

```
daily_GB = events_per_day × bytes_per_event / 1e9
```

Example: 10M rounds/day × 256 bytes ≈ **2.56 GB/day** ≈ 77 GB/month raw.

Add 3× for warehouse indexes, aggregates, and backups.

## Compute estimate

| Workload | Order of magnitude |
|----------|-------------------|
| Daily dbt run | Minutes on warehouse |
| Nightly ML score (1M players) | Single VM / small K8s job |
| Real-time API | Always-on pods + Redis |

## Headcount

For RGS-only analytics MVP:

- 1 analytics engineer (dbt + pipelines)
- 0.5 ML engineer (churn + segmentation)
- No dedicated DE if scope stays batch

## Feasibility gates

| Gate | Criterion |
|------|-----------|
| Phase 1 | GGR + DAU dashboards trusted by ops |
| Phase 2 | Churn model beats random at P@10% |
| Phase 3 | Recommendation A/B shows GGR lift |
| Phase 4 | Real-time ROI > infra cost |

## Key takeaway

Your role is to **validate the roadmap and estimate cost** — not to over-build infrastructure on day one.
