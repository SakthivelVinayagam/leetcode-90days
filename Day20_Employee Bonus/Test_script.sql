-- Test schema + sample data

DROP TABLE IF EXISTS Bonus;
DROP TABLE IF EXISTS Employee;

CREATE TABLE Employee (
  empId INT PRIMARY KEY,
  name VARCHAR(50),
  supervisor INT,
  salary INT
);

CREATE TABLE Bonus (
  empId INT PRIMARY KEY,
  bonus INT
);

-- Sample data
INSERT INTO Employee VALUES
(3, 'Brad', NULL, 4000),
(1, 'John', 3, 1000),
(2, 'Dan', 3, 2000),
(4, 'Thomas', 3, 4000);

INSERT INTO Bonus VALUES
(2, 500),
(4, 2000);

-- Expected Output:
-- name  | bonus
-- ---------------
-- Brad  | NULL
-- John  | NULL
-- Dan   | 500

SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
  ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;