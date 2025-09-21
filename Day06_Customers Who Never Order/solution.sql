-- Day 06: Customers Who Never Order
-- Problem Link: https://leetcode.com/problems/customers-who-never-order/
-- Category: SQL / Anti-join

SELECT c.name AS Customers
FROM Customers AS c
LEFT JOIN Orders AS o
  ON c.id = o.customerId
WHERE o.customerId IS NULL;


-- Alternative approaches for anti-join
-- NOT EXISTS
SELECT c.name AS Customers
FROM Customers c
WHERE NOT EXISTS (
  SELECT 1
  FROM Orders o
  WHERE o.customerId = c.id
);

-- OR: NOT IN (be careful with NULLs in some SQL engines)
SELECT c.name AS Customers
FROM Customers c
WHERE c.id NOT IN (SELECT customerId FROM Orders);