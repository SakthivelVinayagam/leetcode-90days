# Day 27 (SQL): Rank Scores

**Problem**  
Link: https://leetcode.com/problems/rank-scores/  
Category: SQL / Window Functions / Ranking

---

## Approach
We need to assign ranks from highest to lowest score, **without holes** after ties.  
This is exactly what **DENSE_RANK()** does:

```sql
SELECT
  score,
  DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
ORDER BY score DESC;