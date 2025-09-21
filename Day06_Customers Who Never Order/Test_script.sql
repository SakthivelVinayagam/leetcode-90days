-- Clean start
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;

-- Tables
CREATE TABLE Customers (
  id INT PRIMARY KEY,
  name VARCHAR(50)
);

CREATE TABLE Orders (
  id INT PRIMARY KEY,
  customerId INT
);

-- Data
INSERT INTO Customers (id, name) VALUES
(1, 'Joe'),
(2, 'Henry'),
(3, 'Sam'),
(4, 'Max');

INSERT INTO Orders (id, customerId) VALUES
(1, 3),
(2, 1);

-- Query under test
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
  ON c.id = o.customerId
WHERE o.customerId IS NULL;