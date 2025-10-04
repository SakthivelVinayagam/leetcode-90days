-- Test schema + data + queries for LeetCode Day 20: Rising Temperature

DROP TABLE IF EXISTS Weather;

CREATE TABLE Weather (
  id          INT PRIMARY KEY,
  recordDate  DATE NOT NULL,
  temperature INT NOT NULL
);

-- Base sample from prompt
INSERT INTO Weather (id, recordDate, temperature) VALUES
(1, '2015-01-01', 10),
(2, '2015-01-02', 25),
(3, '2015-01-03', 20),
(4, '2015-01-04', 30);

-- Expected output (from prompt):
-- id
-- ----
-- 2
-- 4

-- Run: Option A (Window version; MySQL 8+/Postgres)
SELECT id
FROM (
  SELECT
    id,
    recordDate,
    temperature,
    LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
    LAG(recordDate)  OVER (ORDER BY recordDate) AS prev_date
  FROM Weather
) t
WHERE DATEDIFF(recordDate, prev_date) = 1
  AND temperature > prev_temp;

-- Run: Option B (Self-join; MySQL/Postgres/SQLite-adaptable)
SELECT w1.id
FROM Weather AS w1
JOIN Weather AS w0
  ON DATEDIFF(w1.recordDate, w0.recordDate) = 1
WHERE w1.temperature > w0.temperature;

-- -----------------------------------------------------------
-- Additional tests
-- -----------------------------------------------------------

-- 1) Gap days should not count (only compare with exact yesterday)
DELETE FROM Weather;
INSERT INTO Weather VALUES
(1, '2022-06-01', 10),
(2, '2022-06-03', 50),  -- two days later (gap)
(3, '2022-06-04', 55);  -- consecutive to 06-03

-- Expected: only id = 3 (06-04 vs 06-03 and 55 > 50)
SELECT w1.id
FROM Weather AS w1
JOIN Weather AS w0
  ON DATEDIFF(w1.recordDate, w0.recordDate) = 1
WHERE w1.temperature > w0.temperature;

-- 2) Equal temperatures on consecutive days (should NOT count)
DELETE FROM Weather;
INSERT INTO Weather VALUES
(1, '2022-01-01', 20),
(2, '2022-01-02', 20),  -- equal → not rising
(3, '2022-01-03', 25),  -- rising from yesterday (2 → 3)
(4, '2022-01-05', 26);  -- gap day → ignored
-- Expected: id = 3 only
SELECT w1.id
FROM Weather AS w1
JOIN Weather AS w0
  ON DATEDIFF(w1.recordDate, w0.recordDate) = 1
WHERE w1.temperature > w0.temperature;

-- 3) All rising consecutive days
DELETE FROM Weather;
INSERT INTO Weather VALUES
(1, '2023-07-10', 10),
(2, '2023-07-11', 11),
(3, '2023-07-12', 12),
(4, '2023-07-13', 13);
-- Expected: ids 2,3,4
SELECT w1.id
FROM Weather AS w1
JOIN Weather AS w0
  ON DATEDIFF(w1.recordDate, w0.recordDate) = 1
WHERE w1.temperature > w0.temperature;