DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Department;

CREATE TABLE Department (id INT PRIMARY KEY, name VARCHAR(50) NOT NULL);
CREATE TABLE Employee (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  salary INT,
  departmentId INT
);

INSERT INTO Department (id, name) VALUES
(1, 'IT'), (2, 'Sales');

INSERT INTO Employee (id, name, salary, departmentId) VALUES
(1, 'Joe',   70000, 1),
(2, 'Jim',   90000, 1),
(3, 'Henry', 80000, 2),
(4, 'Sam',   60000, 2),
(5, 'Max',   90000, 1);

-- Run the main query here