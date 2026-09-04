# Feature Engineering Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** `player_features_daily` is typically keyed by:

- A) (game_id, feature_date)  
- B) (player_id, feature_date)  
- C) (session_id, round_id)  
- D) (country, month)  

**2.** `days_since_last_session` on snapshot date D should use events:

- A) After D for accuracy  
- B) Strictly before D (point-in-time)  
- C) From the next 30 days  
- D) From PAM wallet history only  

**3.** `sessions_7d` counts:

- A) Total rounds in 7 days  
- B) Distinct session_id in the 7-day window ending on feature_date  
- C) Deposits in 7 days  
- D) Unique game_ids ever played  

**4.** Feature leakage occurs when:

- A) Features use only past data  
- B) Future information influences training labels or features  
- C) NaN values are filled with zero  
- D) player_id is dropped before training  

**5.** A 7-day rolling window ending on 2024-06-03 inclusive spans:

- A) 2024-05-28 through 2024-06-03  
- B) 2024-06-03 through 2024-06-10  
- C) Only 2024-06-03  
- D) The full calendar month  

**6.** `favorite_game_7d` is typically the game with:

- A) Highest single win  
- B) Most rounds in the feature window  
- C) Lowest RTP  
- D) First alphabetically regardless of play  

**7.** `avg_bet_7d` should aggregate:

- A) win_amount only  
- B) mean of bet_amount in the window  
- C) max deposit  
- D) count of players  

**8.** Point-in-time correctness matters most for:

- A) Static game catalog exports  
- B) ML training and nightly batch scoring  
- C) Logo placement on dashboards  
- D) Provider contract PDFs  

**9.** Filling NaN with 0 in feature matrices is:

- A) Always wrong  
- B) A simple baseline when missing means "no activity"  
- C) Equivalent to leakage  
- D) Required for SQL only  

**10.** Before adding a feature store, the recommended pattern is:

- A) Feast on day one  
- B) dbt feature tables in the warehouse  
- C) Spreadsheets emailed nightly  
- D) Real-time Kafka only  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. A · 6. B · 7. B · 8. B · 9. B · 10. B
