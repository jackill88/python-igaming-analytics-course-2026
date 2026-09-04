# LTV & Value Proxy Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** True financial LTV typically requires:

- A) RGS rounds only  
- B) PAM revenue, bonuses, and costs  
- C) Session duration only  
- D) Game thumbnails  

**2.** With RGS-only data, the practical LTV proxy target is:

- A) future_ggr or future turnover  
- B) Exact NGR after tax  
- C) Payment processor fee  
- D) CRM email LTV  

**3.** `future_ggr_30d` labels sum GGR:

- A) Before the snapshot date  
- B) In the period after snapshot through the horizon  
- C) Across all historical time  
- D) From bonus ledger entries  

**4.** LTV regression differs from churn classification because:

- A) It predicts a continuous value  
- B) It never uses gameplay features  
- C) It requires deep learning only  
- D) It ignores player_id grain  

**5.** A player with high past GGR but zero future activity illustrates:

- A) Why past-only features may not predict future value  
- B) Perfect LTV accuracy  
- C) That labels are unnecessary  
- D) PAM integration is automatic  

**6.** LightGBM regressor is appropriate when:

- A) Target is binary churn  
- B) Target is numeric future GGR  
- C) No numeric features exist  
- D) You need SQL parsing  

**7.** Communicating LTV proxy limitations means stating:

- A) It equals audited financial LTV  
- B) It excludes bonuses, tax, and payment costs  
- C) It replaces finance entirely  
- D) It requires no caveats  

**8.** Point-in-time LTV features use history:

- A) Up to snapshot date  
- B) Including the entire future horizon  
- C) From next week's campaigns  
- D) From other operators  

**9.** Negative future GGR in the label window means:

- A) Player won more than they bet in that future window  
- B) Data is always invalid  
- C) The model must classify instead  
- D) round_id is duplicated  

**10.** Stakeholders often accept GGR-based LTV proxies when:

- A) PAM integration is not yet available  
- B) They need exact NGR on day one  
- C) No gameplay data exists  
- D) Only emails are tracked  

---

## Answers

1. B · 2. A · 3. B · 4. A · 5. A · 6. B · 7. B · 8. A · 9. A · 10. A
