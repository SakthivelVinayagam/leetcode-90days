# Day 36: Product Sales Analysis I

**Problem**  
Link: https://leetcode.com/problems/product-sales-analysis-i/  
Category: SQL / JOIN

---

## Approach
- Perform an **INNER JOIN** between the `Sales` and `Product` tables using `product_id`.
- Select relevant columns: `product_name`, `year`, and `price` from the joined result.
- Every `sale_id` in `Sales` maps to exactly one `product_id` in `Product`.

---

## Complexity
- **Time:** O(n) — one scan of `Sales`, indexed join on `product_id`.  
- **Space:** O(1) — constant extra space.

---

## Notes
- If a product has no sales, it won’t appear in the output (INNER JOIN behavior).
- To include unsold products, use a **LEFT JOIN** instead.
- Straightforward query, often the first exercise in SQL JOIN practice.