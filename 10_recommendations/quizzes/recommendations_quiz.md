# Recommendation Engine Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** A player-game matrix has:

- A) Rows = games, columns = providers  
- B) Rows = players, columns = games, values = interaction strength  
- C) Rows = deposits, columns = withdrawals  
- D) Rows = cohorts, columns = retention days  

**2.** Collaborative filtering recommends items based on:

- A) Only item metadata tags  
- B) Similarity of player interaction patterns  
- C) Random number generation  
- D) Tax jurisdiction  

**3.** A popularity baseline recommends games:

- A) Never played by anyone  
- B) With highest global round counts among unplayed candidates  
- C) Alphabetically first always  
- D) From PAM bonus history only  

**4.** Tie-breaking by `game_id` ascending ensures:

- A) Non-deterministic results  
- B) Reproducible rankings when counts tie  
- C) Higher GGR always  
- D) More clusters in K-Means  

**5.** Offline evaluation metrics include:

- A) Hit rate, coverage, and diversity  
- B) Warehouse disk RPM only  
- C) Provider contract length  
- D) KYC completion rate  

**6.** Recommendations for games the player already played heavily should be:

- A) Always top-ranked  
- B) Deprioritized for discovery use cases  
- C) Excluded from the matrix entirely  
- D) Required by GDPR  

**7.** Matrix factorization (e.g. LightFM) is useful when:

- A) You need implicit feedback from round counts  
- B) You have no player-item interactions  
- C) Only one game exists  
- D) SQL window functions fail  

**8.** Real-time game recommendations require:

- A) Batch-only nightly CSV exports  
- B) Low-latency scoring infrastructure  
- C) No event stream  
- D) PAM-only data  

**9.** `top_n_games_per_player` ranks by:

- A) Round count per (player, game) descending  
- B) Registration date  
- C) Withdrawal amount  
- D) Session_id lexicographic order  

**10.** Cold-start for a new player with no history often falls back to:

- A) Personalized CF from similar players only  
- B) Global popularity or content-based defaults  
- C) Empty recommendations forever  
- D) Churn model scores  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. A · 6. B · 7. A · 8. B · 9. A · 10. B
