# Day 13: Second Highest Salary

**Problem**  
Link: https://leetcode.com/problems/second-highest-salary/  
Category: SQL / Window Functions (ALT: Subquery with DISTINCT)

---

## Approach
- **Window Function method:**
  - Rank salaries in descending order using `DENSE_RANK()`.
  - Pick the salary where rank = 2 (second distinct highest).
  - Use `MAX(salary)` to safely handle multiple employees with the same salary.
- **Alternative (simpler in MySQL):**
  - `SELECT DISTINCT salary ... ORDER BY salary DESC LIMIT 1 OFFSET 1`.

---

## Complexity
- **Time:** O(n log n) (due to sorting salaries).  
- **Space:** O(1) beyond query engine’s sort.  

---

## Patterns
- Top-K queries (`LIMIT 1 OFFSET k`).  
- Ranking with window functions (`DENSE_RANK()`, `ROW_NUMBER()`).  

---

## Notes
- Use `DENSE_RANK()` instead of `ROW_NUMBER()` because multiple employees can share the same salary.  
- If fewer than 2 distinct salaries exist, return `NULL`.  
- Works in MySQL, PostgreSQL, SQL Server.  
- In Pandas: `df['salary'].drop_duplicates().nlargest(2).iloc[-1]` (with null handling).