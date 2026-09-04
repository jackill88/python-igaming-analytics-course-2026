# Player Segmentation Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** Segmentation on RGS data commonly identifies:

- A) Payment processor latency tiers  
- B) Whales, casuals, and churn-risk players  
- C) Tax jurisdictions  
- D) Email domain clusters  

**2.** K-Means requires you to specify:

- A) Only the random seed  
- B) The number of clusters k  
- C) The churn horizon  
- D) Provider fee schedule  

**3.** HDBSCAN is useful when:

- A) You want exactly 3 clusters always  
- B) Cluster count is unknown and noise points exist  
- C) Data has no numeric columns  
- D) You need SQL window functions  

**4.** Before clustering, numeric features should typically be:

- A) Left on different scales without transformation  
- B) Scaled or standardized when magnitudes differ widely  
- C) Converted to player emails  
- D) Dropped entirely  

**5.** Segment profiling computes:

- A) Mean/median of features per cluster label  
- B) Global DAU only  
- C) Provider RTP tables  
- D) Deposit limits  

**6.** A "whale" segment in iGaming usually shows:

- A) Zero sessions and zero GGR  
- B) High GGR and high average bet  
- C) Only bonus-driven play with no rounds  
- D) Negative player_id values  

**7.** `random_state=42` in K-Means ensures:

- A) Different results every run  
- B) Reproducible cluster assignments for the same data  
- C) Automatic optimal k  
- D) Removal of outliers  

**8.** Segmentation outputs feed CRM when:

- A) Segments are interpretable and stable enough to act on  
- B) k equals the number of games  
- C) All players are in one cluster  
- D) Features include future GGR  

**9.** GMM (Gaussian Mixture) differs from K-Means by:

- A) Producing soft cluster probabilities  
- B) Requiring no numeric input  
- C) Only working on categorical data  
- D) Ignoring variance  

**10.** With RGS-only data, segmentation features often include:

- A) Wallet balance and bonus abuse score from PAM  
- B) sessions_30d, avg_bet, ggr_30d, days_since_last_session  
- C) Email click-through rate  
- D) Withdrawal processor ID  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. A · 6. B · 7. B · 8. A · 9. A · 10. B
