# Day 27 (SQL): Duplicate Emails

**Problem**  
Link: https://leetcode.com/problems/duplicate-emails/  
Category: SQL / Aggregation / Group By  

---

## Approach
- Group all rows by the `email` column.  
- Use `COUNT(email)` to find how many times each email appears.  
- Filter with `HAVING COUNT(email) > 1` to return only duplicates.

---

## Complexity
- **Time:** O(N) for scanning and grouping.  
- **Space:** O(D) where D = number of distinct emails.  

---

## Patterns
- Aggregation + Filtering via `GROUP BY` and `HAVING`.  
- Often reused in:
  - Finding duplicate users/customers.
  - Identifying repeated transactions or entries.

---

## Notes
- `HAVING` filters groups *after* aggregation (unlike `WHERE` which filters rows before grouping).  
- Always alias the result column as `Email` to match expected output.
- For large tables, consider indexing the `email` column.