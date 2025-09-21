# Day 06: Customers Who Never Order

**Problem**  
Link: https://leetcode.com/problems/customers-who-never-order/  
Category: SQL / Anti-join

---

## Approach
- Use a LEFT JOIN from `Customers` to `Orders` on `c.id = o.customerId`.
- Keep only rows where the right side is missing: `WHERE o.customerId IS NULL`.
- This returns all customers with no orders.

---

## Complexity
- Time: Depends on indexes; efficient with indexes on `Customers(id)` and `Orders(customerId)`.
- Space: O(1) extra beyond the result set.

---

## Patterns
- Anti-join:
  - `LEFT JOIN ... WHERE right.key IS NULL`
  - Equivalent: `NOT EXISTS (SELECT 1 FROM Orders o WHERE o.customerId = c.id)`

---

## Notes
- `LEFT JOIN ... IS NULL` is robust across SQL engines.
- `NOT EXISTS` is equally valid and often performant.
- Avoid `NOT IN` if the subquery can contain NULLs (engine-dependent behavior).