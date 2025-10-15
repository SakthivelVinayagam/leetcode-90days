-- Test schema + data
DROP TABLE IF EXISTS Scores;
CREATE TABLE Scores (
  id    INT PRIMARY KEY,
  score DECIMAL(4,2) NOT NULL
);

INSERT INTO Scores (id, score) VALUES
(1, 3.50),
(2, 3.65),
(3, 4.00),
(4, 3.85),
(5, 4.00),
(6, 3.65);

-- Expected:
-- score | rank
-- 4.00  | 1
-- 4.00  | 1
-- 3.85  | 2
-- 3.65  | 3
-- 3.65  | 3
-- 3.50  | 4

-- Run Option A
SELECT
  score,
  DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;

-- Run Option B (no window functions)
SELECT
  s1.score,
  1 + (
    SELECT COUNT(DISTINCT s2.score)
    FROM Scores s2
    WHERE s2.score > s1.score
  ) AS `rank`
FROM Scores s1
ORDER BY s1.score DESC;

-- Extra tests
-- 1) Single row
TRUNCATE TABLE Scores;
INSERT INTO Scores VALUES (1, 9.99);
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS `rank` FROM Scores;

-- 2) Many ties
TRUNCATE TABLE Scores;
INSERT INTO Scores VALUES
(1, 10.00),(2,10.00),(3,9.50),(4,9.50),(5,9.50),(6,9.00);
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;