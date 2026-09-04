# SQL Analytics on Gaming Data Quiz

10 multiple-choice questions. Answers at the bottom.

---

**1.** The grain of `rounds(round_id, player_id, game_id, …)` is:

- A) One row per player per day  
- B) One row per round  
- C) One row per session summary  
- D) One row per game catalog entry  

**2.** Top games by GGR in SQL typically use:

- A) `SUM(bet_amount - win_amount) GROUP BY game_id`  
- B) `COUNT(DISTINCT player_id)` only  
- C) `MAX(win_amount)`  
- D) `AVG(deposit_amount)`  

**3.** Player favorite game by round count should break ties by:

- A) Highest GGR first, then random  
- B) game_id ascending (deterministic tie-break)  
- C) Latest timestamp only  
- D) Alphabetical player_id  

**4.** `ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY cnt DESC, game_id ASC)` assigns:

- A) The same rank to all games  
- B) Rank 1 to the most-played game per player  
- C) Global game popularity  
- D) Session duration  

**5.** A rolling 7-day GGR window with `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` includes:

- A) 6 days total  
- B) 7 days including the current row  
- C) 8 days excluding the current row  
- D) Only future days  

**6.** DuckDB is useful in this course because:

- A) It replaces the RGS entirely  
- B) It runs analytical SQL in-memory against pandas DataFrames  
- C) It requires a dedicated cluster  
- D) It only supports NoSQL  

**7.** When joining rounds to a game catalog, use:

- A) player_id  
- B) game_id  
- C) round_id  
- D) session_id  

**8.** Filtering `WHERE activity_date BETWEEN …` before aggregating helps:

- A) Increase storage costs  
- B) Reduce scanned data and improve performance  
- C) Eliminate the need for indexes  
- D) Convert GGR to NGR  

**9.** Window functions differ from `GROUP BY` because:

- A) They remove all row detail  
- B) They can compute running/rolling metrics while keeping row grain  
- C) They only work on strings  
- D) They require PAM data  

**10.** SQL for player-game affinity often starts with:

- A) `SELECT * FROM bonuses`  
- B) Counting rounds or bets per (player_id, game_id)  
- C) Deleting duplicate sessions  
- D) Importing CRM emails  

---

## Answers

1. B · 2. A · 3. B · 4. B · 5. B · 6. B · 7. B · 8. B · 9. B · 10. B
