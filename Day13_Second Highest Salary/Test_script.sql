-- Schema
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    salary INT
);

-- Insert sample data
INSERT INTO Employee (id, salary) VALUES
(1, 100),
(2, 200),
(3, 300);

-- Test Case 1: Normal case
-- Expected output: 200
SELECT
  MAX(salary) AS SecondHighestSalary
FROM (
  SELECT
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM Employee
) t
WHERE rnk = 2;

-- Clear and reload for another case
DELETE FROM Employee;
INSERT INTO Employee (id, salary) VALUES (1, 100);

-- Test Case 2: Only one salary
-- Expected output: NULL
SELECT
  MAX(salary) AS SecondHighestSalary
FROM (
  SELECT
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM Employee
) t
WHERE rnk = 2;

-- Test Case 3: Duplicate top salaries
DELETE FROM Employee;
INSERT INTO Employee (id, salary) VALUES
(1, 500),
(2, 500),
(3, 400);

-- Expected output: 400 (since 500 is rank 1, 400 rank 2)
SELECT
  MAX(salary) AS SecondHighestSalary
FROM (
  SELECT
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM Employee
) t
WHERE rnk = 2;