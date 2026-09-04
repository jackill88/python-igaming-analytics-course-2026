# Churn Prediction Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** A common iGaming churn definition is:

- A) One losing session  
- B) 30 consecutive days without activity  
- C) Negative lifetime GGR  
- D) Account closed in PAM only  

**2.** The ML target `inactive_next_30_days` means:

- A) Player was inactive in the past 30 days  
- B) No activity in the 30 days after the snapshot date  
- C) Player deleted the app yesterday  
- D) GGR was zero on snapshot day  

**3.** Churn features should be computed using data:

- A) Up to and including the snapshot date only  
- B) From the entire future horizon  
- C) From CRM emails sent after snapshot  
- D) From next month's deposits  

**4.** LightGBM/XGBoost are popular for churn because:

- A) They require no features  
- B) They handle tabular heterogeneous features well  
- C) They only work on text  
- D) They output SQL directly  

**5.** `days_since_last_session` is a:

- A) Recency feature  
- B) Provider fee  
- C) Game category label  
- D) Warehouse partition key  

**6.** Precision at top 10% is useful when:

- A) CRM budget limits who you can contact  
- B) You must contact every player  
- C) You have unlimited outreach capacity  
- D) Labels are all zeros  

**7.** Training labels need players who:

- A) Were active in the lookback window before snapshot  
- B) Registered after the snapshot  
- C) Never placed a bet  
- D) Only appear in PAM  

**8.** Class imbalance in churn often leads to:

- A) Always predicting "not churn" with high accuracy but low value  
- B) Perfect recall without effort  
- C) No need for evaluation metrics  
- D) Elimination of feature engineering  

**9.** A churn model deployed nightly typically scores:

- A) Real-time every bet  
- B) Batch predictions into a table for CRM  
- C) Only historical cohorts  
- D) Provider invoices  

**10.** RGS-only churn models cannot directly use:

- A) sessions_30d  
- B) avg_bet_30d  
- C) Deposit frequency and bonus usage  
- D) days_since_last_session  

---

## Answers

1. B · 2. B · 3. A · 4. B · 5. A · 6. A · 7. A · 8. A · 9. B · 10. C
