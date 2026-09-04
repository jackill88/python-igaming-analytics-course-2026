# Session Analytics Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** RGS `session_id` differs from derived sessions because:

- A) RGS sessions are always 30 minutes  
- B) Derived sessions are recomputed from event gaps  
- C) RGS sessions ignore player_id  
- D) Derived sessions require PAM data  

**2.** Gap-based sessionization splits a session when:

- A) The player changes game_id  
- B) Time between consecutive events exceeds a threshold  
- C) GGR turns negative  
- D) round_id duplicates appear  

**3.** Session duration is typically computed as:

- A) Sum of bet amounts  
- B) max(timestamp) − min(timestamp) within the session  
- C) Count of unique game_ids  
- D) Registration date minus first bet  

**4.** A 30-minute gap threshold means a 31-minute pause:

- A) Continues the same session  
- B) Starts a new derived session  
- C) Deletes the events  
- D) Merges two players  

**5.** GGR per session aggregates:

- A) Only win amounts  
- B) Sum(bet_amount) − sum(win_amount) per session  
- C) Average bet across all players  
- D) Deposits minus withdrawals  

**6.** Before sessionization, events should be sorted by:

- A) game_id, then round_id  
- B) player_id, then timestamp  
- C) bet_amount descending  
- D) Random shuffle  

**7.** `derived_session_id` usually:

- A) Resets to 1 for each player  
- B) Is globally unique across all players  
- C) Matches round_id  
- D) Comes from PAM  

**8.** A single-round session has duration:

- A) Always 30 minutes  
- B) Zero minutes (max equals min)  
- C) Undefined  
- D) Equal to average bet  

**9.** Session metrics help answer:

- A) Which provider has the lowest fee  
- B) How long and how intensely players engage per visit  
- C) Tax jurisdiction per player  
- D) Email open rates  

**10.** Using RGS session_id vs derived sessions requires:

- A) Documenting which definition powers each dashboard  
- B) Always preferring PAM login sessions  
- C) Ignoring timestamp ordering  
- D) Dropping round_id  

---

## Answers

1. B · 2. B · 3. B · 4. B · 5. B · 6. B · 7. A · 8. B · 9. B · 10. A
