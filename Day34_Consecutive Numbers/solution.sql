-- Day 35: Consecutive Numbers
-- Problem: https://leetcode.com/problems/consecutive-numbers/
-- Category: SQL / Window / Self-Join

/* ✅ Option 1: Simple self-join on consecutive ids (works on MySQL 5.x/8.x) */
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l2.id = l1.id + 1 AND l2.num = l1.num
JOIN Logs l3 ON l3.id = l2.id + 1 AND l3.num = l1.num;

/* ✅ Option 2: Window function (MySQL 8+), more general
SELECT DISTINCT num AS ConsecutiveNums
FROM (
  SELECT
    id,
    num,
    LAG(num, 1) OVER (ORDER BY id) AS prev1,
    LAG(num, 2) OVER (ORDER BY id) AS prev2
  FROM Logs
) t
WHERE num = prev1 AND num = prev2;
*/