# Day 20: Sales Person

**Problem**  
Link: https://leetcode.com/problems/sales-person/  
Category: SQL / Joins / Filtering

---

## Approach
We want all salespersons who did **not** sell to company `RED`.

- Join `Orders` with `Company` to identify which salespersons sold to `RED`.
- Exclude those salespersons using either:
  - **NOT IN** (clear and concise).
  - **NOT EXISTS** (preferred in NULL-safe contexts).

---

## Complexity
- Time: O(N) for scanning SalesPerson + Orders join.
- Space: O(1) beyond query processing.

---

## Patterns
- Anti-join (`NOT IN` / `NOT EXISTS`).
- Filtering by exclusion.

---

## Notes
- `NOT EXISTS` is more robust than `NOT IN` when NULL values can appear.
- Distinct is required inside the subquery to avoid duplicates.
- Indexes on `(Orders.com_id, Orders.sales_id)` and `Company.name` improve performance.