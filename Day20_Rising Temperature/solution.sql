-- Day 20: Rising Temperature
-- Problem Link: https://leetcode.com/problems/rising-temperature/
-- Category: SQL / Joins / Window Functions

/* ============================================================
   Option A (MySQL 8+ / Postgres): Window function + date check
   - Use LAG to get yesterday’s temp and date.
   - Ensure it is exactly the previous calendar day (no gaps).
   ============================================================ */
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


/* ============================================================
   Option B (Portable / MySQL / Postgres / SQLite-compatible):
   Self-join previous day by exact date difference of 1 day.
   ============================================================ */
-- MySQL / Postgres (MySQL: DATEDIFF(d1, d2) returns days between)
-- Postgres: use (recordDate - prev.recordDate) = 1 instead of DATEDIFF
SELECT w1.id
FROM Weather AS w1
JOIN Weather AS w0
  ON DATEDIFF(w1.recordDate, w0.recordDate) = 1
WHERE w1.temperature > w0.temperature;

/* Postgres variant for Option B:
SELECT w1.id
FROM Weather AS w1
JOIN Weather AS w0
  ON (w1.recordDate - w0.recordDate) = INTERVAL '1 day'
WHERE w1.temperature > w0.temperature;
*/