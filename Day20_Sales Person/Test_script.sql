-- Test setup for Day 20: Sales Person

DROP TABLE IF EXISTS SalesPerson, Company, Orders;

CREATE TABLE SalesPerson (
  sales_id INT PRIMARY KEY,
  name VARCHAR(50),
  salary INT,
  commission_rate INT,
  hire_date DATE
);

CREATE TABLE Company (
  com_id INT PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50)
);

CREATE TABLE Orders (
  order_id INT PRIMARY KEY,
  order_date DATE,
  com_id INT,
  sales_id INT,
  amount INT
);

-- Insert sample data (from LeetCode example)
INSERT INTO SalesPerson VALUES
(1, 'John', 100000, 6, '2006-04-01'),
(2, 'Amy', 12000, 5, '2010-05-01'),
(3, 'Mark', 65000, 12, '2008-12-25'),
(4, 'Pam', 25000, 25, '2005-01-01'),
(5, 'Alex', 5000, 10, '2007-02-03');

INSERT INTO Company VALUES
(1, 'RED', 'Boston'),
(2, 'ORANGE', 'New York'),
(3, 'YELLOW', 'Boston'),
(4, 'GREEN', 'Austin');

INSERT INTO Orders VALUES
(1, '2014-01-01', 3, 4, 10000),
(2, '2014-02-01', 4, 5, 5000),
(3, '2014-03-01', 1, 1, 50000),
(4, '2014-04-01', 1, 4, 25000);

-- Run main query
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);

-- Expected:
-- +------+
-- | name |
-- +------+
-- | Amy  |
-- | Mark |
-- | Alex |
-- +------+