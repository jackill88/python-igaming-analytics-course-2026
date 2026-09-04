# Analytics Architecture Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** Phase 1 of the recommended analytics roadmap is:

- A) Feature store evaluation  
- B) Warehouse ingestion from RGS  
- C) Real-time recommendation API  
- D) Blockchain audit trail  

**2.** dbt feature tables sit between:

- A) CRM and email SMTP  
- B) Raw warehouse tables and ML models  
- C) Game servers and players  
- D) Tax authority and regulator  

**3.** Batch nightly ML scoring is sufficient for:

- A) In-session game recommendations at bet time  
- B) Churn and segmentation CRM lists  
- C) Sub-millisecond fraud on every click  
- D) Live dealer video streaming  

**4.** A feature store (e.g. Feast) is justified when:

- A) Day one of analytics with one report  
- B) Multiple models share features and online inference matters  
- C) No warehouse exists  
- D) Only static PDFs are needed  

**5.** Daily storage estimate uses:

- A) events_per_day × bytes_per_event / 1e9 GB  
- B) MAU × DAU  
- C) GGR × tax rate  
- D) Cluster count × k  

**6.** Redis is often paired with batch ML when:

- A) Low-latency serving of precomputed scores is needed  
- B) Replacing the warehouse entirely  
- C) Storing raw video  
- D) Eliminating dbt  

**7.** Training-serving skew happens when:

- A) Training and production features are computed differently  
- B) Models use the same SQL in both paths  
- C) player_id is consistent  
- D) Random seed is fixed  

**8.** For RGS-only MVP, headcount often includes:

- A) 10 dedicated data engineers day one  
- B) 1 analytics engineer + fractional ML support  
- C) No analytics roles  
- D) Only frontend designers  

**9.** Feasibility gate for Phase 2 ML might require:

- A) Churn model beats random at precision@k  
- B) Unlimited CRM budget proof  
- C) PAM integration complete  
- D) Feature store in production  

**10.** The stakeholder ask to "validate roadmap and cost" means:

- A) Build every tool immediately  
- B) Prove business value before scaling infrastructure  
- C) Skip metrics entirely  
- D) Outsource all modeling  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. A · 6. A · 7. A · 8. B · 9. A · 10. B
