-- Day 06: Combine Two Tables
-- Problem Link: https://leetcode.com/problems/combine-two-tables/
-- Category: SQL / JOINs

SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person AS p
LEFT JOIN Address AS a
    ON p.personId = a.personId;