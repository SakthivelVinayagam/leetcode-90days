-- Day 27 (SQL): Rank Scores
-- Problem Link: https://leetcode.com/problems/rank-scores/
-- Category: SQL / Window Functions (dense ranking)

-- Option A (recommended, MySQL 8+/Postgres): DENSE_RANK
SELECT
  score,
  DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;

-- Option B (works without window functions): count distinct higher scores
-- SELECT
--   s1.score,
--   1 + (
--     SELECT COUNT(DISTINCT s2.score)
--     FROM Scores s2
--     WHERE s2.score > s1.score
--   ) AS `rank`
-- FROM Scores s1
-- ORDER BY s1.score DESC;