-- Day 34: Product Sales Analysis I
-- Problem: https://leetcode.com/problems/product-sales-analysis-i/
-- Category: SQL / JOIN

SELECT 
  p.product_name,
  s.year,
  s.price
FROM Sales AS s
JOIN Product AS p
  ON s.product_id = p.product_id;