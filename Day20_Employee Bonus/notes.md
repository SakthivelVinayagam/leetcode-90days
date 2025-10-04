# Day 20: Employee Bonus

**Problem**  
Link: https://leetcode.com/problems/employee-bonus/  
Category: SQL / Joins

---

## Approach
- Use a `LEFT JOIN` between `Employee` and `Bonus`.
- Keep all employees, even those without a bonus record (`NULL`).
- Filter rows:
  - `b.bonus < 1000` → small bonuses.
  - `b.bonus IS NULL` → no bonus record.

---

## Complexity
- **Time:** O(N log N) with join (depending on indexes).  
- **Space:** O(N) for intermediate join results.  

---

## Patterns
- Outer join to capture employees missing related data.  
- Conditional filter with `OR b.bonus IS NULL`.  

---

## Notes
- Boundary: `bonus = 1000` → excluded.  
- Indexes on `Employee.empId` and `Bonus.empId` speed up joins.  
- Always check for NULL explicitly in `LEFT JOIN` cases.