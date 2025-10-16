-- Test schema + data
DROP TABLE IF EXISTS Person;
CREATE TABLE Person (
  id INT PRIMARY KEY,
  email VARCHAR(255) NOT NULL
);

INSERT INTO Person (id, email) VALUES
(1, 'a@b.com'),
(2, 'c@d.com'),
(3, 'a@b.com'),
(4, 'x@y.com'),
(5, 'x@y.com'),
(6, 'z@z.com');

-- Expected Output:
-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- | x@y.com |
-- +---------+

SELECT
  email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;