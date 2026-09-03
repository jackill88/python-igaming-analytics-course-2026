# Session Definitions

RGS session_id vs derived sessions.

## Key concepts

- iGaming analytics starts from **RGS gameplay events** when PAM data is unavailable
- State **grain** (player, session, round) before aggregating
- **GGR = bets − wins** is the primary revenue metric from RGS
- Engagement (DAU/WAU/MAU), retention, and churn build on activity definitions
- ML features belong in warehouse tables like `player_features_daily`
- Validate business value before investing in real-time ML infrastructure

## Example

```python
import pandas as pd

events = pd.DataFrame({
    "bet_amount": [10.0, 5.0, 20.0],
    "win_amount": [0.0, 15.0, 0.0],
})
events["ggr"] = events["bet_amount"] - events["win_amount"]
print(events["ggr"].sum())  # GGR = 20.0
```

## Practice

Complete the module challenges and run pytest to verify your implementation.
