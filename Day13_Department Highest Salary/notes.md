# Day 13: Department Highest Salary

**Problem**  
Link: https://leetcode.com/problems/department-highest-salary/  
Category: SQL / Window Functions (ALT: Aggregation + Join)

---

## Approach
- Use a window function to rank employees by salary within each department:
  - `RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC)`  
- Select rows where rank = 1 to get all employees tied for the highest salary per department.
- Join with `Department` to output department names.

**Alternative:**  
- Compute `MAX(salary)` per `departmentId` in a subquery, then join back to `Employee` on `(departmentId, salary)` and to `Department` for names.

---

## Complexity
- Time: Driven by indexing and engine; window function or grouped aggregate with proper indexes performs well.  
- Space: O(1) extra (beyond result set).

---

## Patterns
- Top-N per group using window functions (`RANK()` / `DENSE_RANK()`).
- Group aggregate + join when window functions are unavailable.

---

## Notes
- `RANK()` returns all ties (required by the problem). `ROW_NUMBER()` would return only one row.
- Ensure join to `Department` by `departmentId` to display department names.
- Indexes that help: `Employee(departmentId, salary)` and `Department(id)`.