-- Day 13: Department Highest Salary
-- Problem Link: https://leetcode.com/problems/department-highest-salary/
-- Category: SQL / Window Functions (ALT: Aggregation + Join)

-- Preferred: window function (handles ties naturally)
SELECT
  d.name  AS Department,
  e.name  AS Employee,
  e.salary AS Salary
FROM (
  SELECT
    id,
    name,
    salary,
    departmentId,
    RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
  FROM Employee
) e
JOIN Department d
  ON d.id = e.departmentId
WHERE e.rnk = 1;

-- Alternative: aggregation + join
-- SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
-- FROM Employee e
-- JOIN (
--   SELECT departmentId, MAX(salary) AS max_salary
--   FROM Employee
--   GROUP BY departmentId
-- ) m
--   ON e.departmentId = m.departmentId AND e.salary = m.max_salary
-- JOIN Department d
--   ON d.id = e.departmentId;