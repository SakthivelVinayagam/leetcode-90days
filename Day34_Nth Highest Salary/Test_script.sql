-- Using DENSE_RANK() for distinct ranking
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

-- Example 1
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

CALL getNthHighestSalary(2);
-- Output:
-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+

-- Example 2
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+

CALL getNthHighestSalary(2);
-- Output:
-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | null                   |
-- +------------------------+