# Day 21 (SQL): Rising Temperature

**Problem**  
Link: https://leetcode.com/problems/rising-temperature/  
Category: SQL / Joins / Window Functions

---

## Approach
We need all `id` where today’s temperature is **higher than yesterday’s** and the two rows are exactly one calendar day apart.

Two equivalent approaches:

### A) Window Function (MySQL 8+ / Postgres)
- Use `LAG(temperature)` and `LAG(recordDate)` over `ORDER BY recordDate`.
- Filter rows where `DATEDIFF(recordDate, prev_date) = 1` and `temperature > prev_temp`.

### B) Self-Join (Portable)
- Join `Weather w1` with `Weather w0` where `w1.recordDate` is exactly 1 day after `w0.recordDate`.
- Keep rows where `w1.temperature > w0.temperature`.

---

## Complexity
- Typically O(N log N) for sorting on `recordDate` (window or join with sort), improved with index.
- Space managed by the SQL engine.

---

## Patterns
- Time-series comparison with consecutive-day requirement.
- Window functions (`LAG`) vs self-join on date arithmetic.

---

## Notes
- Be strict about “yesterday”: enforce exact 1-day difference; do not just compare to the previous row in sort order if there are gaps.
- Index recommendation: `INDEX(recordDate)` to speed up ordering/join.
- Equality on temperature does **not** count as rising.