-- Day 14: Second Highest Salary
-- Problem Link: https://leetcode.com/problems/second-highest-salary/
-- Category: SQL / Window Functions (ALT: Subquery with DISTINCT)

-- Option 1: Window Function
SELECT 
  MAX(salary) AS SecondHighestSalary
FROM (
  SELECT salary,
         DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM Employee
) ranked
WHERE rnk = 2;

-- Option 2: Subquery with DISTINCT (simpler)
-- SELECT (
--   SELECT DISTINCT salary
--   FROM Employee
--   ORDER BY salary DESC
--   LIMIT 1 OFFSET 1
-- ) AS SecondHighestSalary;