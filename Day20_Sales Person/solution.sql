-- Day 20: Sales Person
-- Problem Link: https://leetcode.com/problems/sales-person/
-- Category: SQL / Joins / Filtering

/* ============================================================
   Approach:
   - Find all salespersons who never sold to company 'RED'.
   - Join SalesPerson → Orders → Company.
   - Exclude salespersons whose orders involve company 'RED'.
   ============================================================ */

-- Option A: NOT IN (simple, clear)
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);

-- Option B: NOT EXISTS (safer for NULL cases)
-- SELECT s.name
-- FROM SalesPerson s
-- WHERE NOT EXISTS (
--     SELECT 1
--     FROM Orders o
--     JOIN Company c ON o.com_id = c.com_id
--     WHERE c.name = 'RED' AND o.sales_id = s.sales_id
-- );