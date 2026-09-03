# Stakeholder Framing

Stakeholders in iGaming analytics often ask for ML platforms, feature stores, and real-time personalization. Your job as an **Analytics Lead / Applied ML consultant** is to validate whether those investments solve real problems.

## The key question

> "Are we solving the right problems, and what does it cost?"

This matters more than building technology for its own sake.

## Recommended positioning

For initial RGS-based use cases, a large ML platform is probably **unnecessary**. You can:

1. Derive player features directly in the warehouse (dbt)
2. Validate business value through **segmentation** and **churn** models
3. Introduce real-time infrastructure or a feature store only when recommendation and next-best-action use cases show **measurable ROI**

## ROI conversation template

| Use case | Data needed | Batch OK? | Typical first metric |
|----------|-------------|-----------|----------------------|
| Churn prevention | RGS + activity | Yes | % churners contacted |
| Segmentation | RGS features | Yes | campaign lift by segment |
| Game recommendations | RGS play history | Often yes (daily) | click-through / play rate |
| Next-best-action | RGS + PAM | Usually no | conversion rate |
| True LTV | PAM payments | Yes | forecast vs actual NGR |

## When to escalate infrastructure

| Signal | Consider adding |
|--------|-----------------|
| Multiple models share 20+ features | dbt mart consolidation first |
| Online inference < 100ms required | Redis scoring layer |
| Training-serving skew is painful | Feature store evaluation |
| Team > 5 ML engineers | MLOps platform |

## What to say in interviews

- Start with **business metric** (retention, GGR, churn cost)
- Show **feasibility** with available data (RGS vs PAM)
- Estimate **cost** (storage, compute, headcount)
- Propose **phased roadmap** with validation gates
