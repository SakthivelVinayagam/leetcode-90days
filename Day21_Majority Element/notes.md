# Day 21: Majority Element

**Problem**  
Link: https://leetcode.com/problems/majority-element/  
Category: Array / Hashmap / Boyer–Moore Majority Vote

---

## Approach
Use the **Boyer–Moore Majority Vote** algorithm:
- Maintain a `candidate` and a `count`.
- Iterate over `nums`:
  - If `count == 0`, set `candidate = num`.
  - If `num == candidate`, `count += 1` else `count -= 1`.
- Since a majority element (> ⌊n/2⌋) is guaranteed, the final `candidate` is the answer.

---

## Complexity
- **Time:** O(n) — single pass  
- **Space:** O(1) — constant

---

## Patterns
- Greedy cancellation / Majority Vote
- Stream processing with O(1) memory

---

## Notes
- Intuition: non-majority elements get “canceled out”; majority survives.
- Alternative (simpler but more space): frequency map with `collections.Counter`.
- Related:
  - Majority Element II (more than ⌊n/3⌋) — requires tracking two candidates.