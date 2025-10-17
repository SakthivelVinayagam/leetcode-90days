-- Day 34: Nth Highest Salary
-- Problem Link: https://leetcode.com/problems/nth-highest-salary/
-- Category: SQL / Window Functions

-- ✅ Using DENSE_RANK() for distinct ranking
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    SELECT DISTINCT salary
    FROM (
      SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
      FROM Employee
    ) ranked
    WHERE rnk = N
  );
END;