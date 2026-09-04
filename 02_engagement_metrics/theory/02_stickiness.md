# Stickiness

Stickiness measures **how often users return** within a longer window.

```
Stickiness = DAU / MAU
```

| Stickiness | Interpretation |
|------------|----------------|
| ~0.03 | Players visit ~1 day per month (typical casual app) |
| ~0.10 | Strong daily habit |
| ~0.20+ | Very high-frequency product |

## Why it matters in iGaming

- High stickiness → reliable daily revenue base
- Low stickiness + high MAU → many occasional players (weekend spikes)
- Track stickiness by **cohort** and **game category** for product insight

## Example

```python
stickiness = dau(activity, as_of) / mau(activity, as_of)  # guard MAU=0
```

## Related metrics

- **WAU / MAU** — weekly return rate
- **DAU / WAU** — within-week frequency

## Key takeaway

Stickiness is a **ratio of two active-user metrics** — if you change the active definition, both numerator and denominator must use the same rule.
