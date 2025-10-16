-- Day 27 (SQL): Duplicate Emails
-- Problem Link: https://leetcode.com/problems/duplicate-emails/
-- Category: SQL / Aggregation / Group By

SELECT
  email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;