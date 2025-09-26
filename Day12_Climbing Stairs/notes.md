# Day 12: Climbing Stairs

**Problem**  
Link: https://leetcode.com/problems/climbing-stairs/  
Category: Dynamic Programming  

---

## Approach
- To reach step `n`, you can:
  - Take 1 step from `(n-1)`
  - Take 2 steps from `(n-2)`
- Therefore:  
  **dp[n] = dp[n-1] + dp[n-2]**
- Base cases:  
  - `dp[1] = 1`  
  - `dp[2] = 2`  
- Optimized to use only 2 variables (`prev1`, `prev2`) instead of a full DP array.

---

## Complexity
- **Time:** O(n) → loop through steps  
- **Space:** O(1) → only two variables  

---

## Patterns
- Dynamic Programming (1D)  
- Fibonacci-like recurrence  
- Related problems:  
  - House Robber  
  - Min Cost Climbing Stairs  

---

## Notes
- Key insight: choices (1 or 2 steps) → Fibonacci recurrence.  
- Handle small `n` explicitly (`n=1`, `n=2`).  
- Always check if DP can be optimized from O(n) space to O(1).  