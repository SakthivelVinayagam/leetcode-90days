-- Setup
CREATE TABLE Logs (id INT PRIMARY KEY, num VARCHAR(20));
INSERT INTO Logs (id, num) VALUES
(1,'1'), (2,'1'), (3,'1'),
(4,'2'),
(5,'1'),
(6,'2'), (7,'2');

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

-- Run solution (choose one of the options above)
-- Expected:
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+