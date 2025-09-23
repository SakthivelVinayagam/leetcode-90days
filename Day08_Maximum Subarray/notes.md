# Day 08: Maximum Subarray

**Problem**  
Link: https://leetcode.com/problems/maximum-subarray/  
Category: Array / Dynamic Programming (Kadane), (Alt) Divide & Conquer

---

## Approach
- **Kadane’s Algorithm (O(n))**:
  - Maintain a running sum `curr_sum` and a global maximum `max_sum`.
  - For each element `x`, decide to extend the current subarray or start a new one:
    - `curr_sum = max(x, curr_sum + x)`
    - `max_sum = max(max_sum, curr_sum)`
  - Initialize both with `nums[0]` to correctly handle all-negative arrays.

- **Follow-up (Divide & Conquer, O(n log n))**:
  - The maximum subarray is the max of:
    - best in left half, best in right half, or a subarray crossing the middle
      (max suffix of left + max prefix of right).

---

## Complexity
- **Kadane**: Time O(n), Space O(1)  
- **Divide & Conquer**: Time O(n log n), Space O(log n) recursion

---

## Patterns
- Dynamic Programming (running optimum)
- Prefix/suffix reasoning (for divide & conquer)

---

## Notes
- Works with negative numbers by initializing to `nums[0]`, not 0.
- Common pitfall: resetting `curr_sum` to 0 can be wrong for all-negative arrays.
- The divide & conquer version is useful to understand theoretical alternatives.