# Day 34: Consecutive Numbers

**Problem**  
Link: https://leetcode.com/problems/consecutive-numbers/  
Category: SQL / Window / Self-Join

---

## Approach

### Option 1 — Self-Join on consecutive ids (portable)
- Because `id` is an auto-increment and represents row order, three consecutive appearances of the same `num` must satisfy:
  - row i: `l1`
  - row i+1: `l2` with `l2.num = l1.num`
  - row i+2: `l3` with `l3.num = l1.num`
- Join `Logs` to itself twice on `id+1` and `id+2`, filter where `num` matches in all three, then `SELECT DISTINCT`.

### Option 2 — Window function (MySQL 8+)
- Use `LAG(num,1)` and `LAG(num,2)` over `ORDER BY id`.
- A row belongs to a 3-run if `num = LAG(num,1) = LAG(num,2)`.
- `SELECT DISTINCT num` from those rows.

---

## Complexity
- Time: O(n) over ordered scan + join/window operations (db-dependent).  
- Space: O(1) extra (logical), engine may use temp structures.

---

## Notes
- Self-join version is simplest and compatible with older MySQL versions.
- Window version is expressive and scales to “k consecutive” by checking more `LAG`s or by streak grouping.