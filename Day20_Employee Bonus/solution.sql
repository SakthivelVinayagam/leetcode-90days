-- Day 20: Employee Bonus
-- Problem Link: https://leetcode.com/problems/employee-bonus/
-- Category: SQL / Joins

SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b
  ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;