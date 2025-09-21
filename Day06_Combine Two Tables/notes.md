# Day 06: Combine Two Tables

**Problem**  
Link: https://leetcode.com/problems/combine-two-tables/  
Category: SQL / JOINs

---

## Approach
- Use a `LEFT JOIN` from `Person` to `Address` on `personId` to return all persons.
- Select `firstName`, `lastName` from `Person` and `city`, `state` from `Address`.
- If a person has no matching row in `Address`, `city` and `state` will be `NULL` (as required).

---

## Complexity
- Time: Depends on indexing and the database engine’s join strategy; typically O(n) with appropriate indexes.
- Space: O(1) extra (beyond the result set).

---

## Patterns
- Outer join to retain “master” table rows and optionally fill from a “detail” table.
- Similar: “LEFT JOIN with defaults/NULLs” for optional relationships.

---

## Notes
- `LEFT JOIN` is essential; `INNER JOIN` would drop persons without addresses.
- Ensure join predicate: `Person.personId = Address.personId`.
- Column selection and aliasing keep the output columns clear and aligned with the prompt.