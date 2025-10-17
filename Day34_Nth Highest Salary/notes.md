# Day 34: Nth Highest Salary

**Problem**  
Link: https://leetcode.com/problems/nth-highest-salary/  
Category: SQL / Window Functions  

---

## Approach
Use the **DENSE_RANK()** window function to assign ranks to salaries in descending order.  
Each distinct salary gets a unique rank (no gaps in ranking when duplicates exist).

Then, simply **filter** where `rnk = N`.  

If there are fewer than N distinct salaries, the result returns `NULL`.

---

## Steps
1. Rank salaries in descending order using:
   ```sql
   DENSE_RANK() OVER (ORDER BY salary DESC)