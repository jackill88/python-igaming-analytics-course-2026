import pandas as pd

from shared.testing import load_challenge

label_deposit_churn = load_challenge(
    "part_02_pam/05_models_and_pipeline", "label_deposit_churn.py"
).label_deposit_churn


def _transactions() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "cid": [1, 1, 2, 3, 4],
            "tx_type": ["deposit", "deposit", "deposit", "deposit", "deposit"],
            "status": ["approved", "approved", "approved", "approved", "open"],
            "created_at": pd.to_datetime(
                [
                    "2024-06-01",
                    "2024-06-15",
                    "2024-05-20",
                    "2024-04-01",
                    "2024-06-01",
                ]
            ),
        }
    )


def test_labels_recent_depositors_only():
    out = label_deposit_churn(_transactions(), pd.Timestamp("2024-06-01"), horizon_days=30)
    labels = dict(zip(out["cid"], out["no_deposit_next_30_days"]))
    assert labels[1] == 0
    assert labels[2] == 1
    assert 3 not in labels
    assert 4 not in labels


def test_sorted_and_columns():
    out = label_deposit_churn(_transactions(), pd.Timestamp("2024-06-01"))
    assert list(out.columns) == ["cid", "no_deposit_next_30_days"]
    assert out["cid"].tolist() == sorted(out["cid"].tolist())


def test_empty_population():
    transactions = _transactions().iloc[0:0]
    out = label_deposit_churn(transactions, pd.Timestamp("2024-06-01"))
    assert list(out.columns) == ["cid", "no_deposit_next_30_days"]
    assert out.empty
