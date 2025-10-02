# Day 18: Squares of a Sorted Array

**Problem**  
Link: https://leetcode.com/problems/squares-of-a-sorted-array/  
Category: Array / Two Pointers  

---

## Approach
- Squaring can change the order because negative numbers become positive.  
- Largest square always comes from either leftmost (most negative) or rightmost (largest positive).  
- Use **two pointers** (`left`, `right`):  
  - Compare `abs(nums[left])` vs `abs(nums[right])`.  
  - Place the larger square at the current end of the result array, then move that pointer inward.  
- Continue until all positions are filled.

---

## Complexity
- **Time:** O(n) (one pass through array)  
- **Space:** O(n) (result array; could be optimized in-place but less clear)

---

## Patterns
- Two Pointers (meet in middle).  
- Similar to: Merge Sorted Array, Max Area Container, Sliding Window Maximum.

---

## Notes
- Squaring then sorting works but is O(n log n).  
- Two-pointer approach achieves O(n).  
- Handles both negative and positive ranges naturally.  
- Edge cases: all negatives, all positives, single element.