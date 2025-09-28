# Day 14: Search Insert Position

**Problem**  
Link: https://leetcode.com/problems/search-insert-position/  
Category: Binary Search / Array  

---

## Approach
- Use **binary search** to locate the target or its correct insert position.  
- Start with `left = 0`, `right = len(nums) - 1`.  
- While `left <= right`:
  - Calculate mid = (left + right) // 2.
  - If `nums[mid] == target` → return `mid`.
  - If `nums[mid] < target` → move right (`left = mid + 1`).
  - Else → move left (`right = mid - 1`).
- When the loop ends, return `left`, which is the correct index to insert.

---

## Complexity
- **Time:** O(log n) (binary search halves the search space).  
- **Space:** O(1) (constant variables).  

---

## Patterns
- Binary Search  
- Related problems:  
  - 704. Binary Search  
  - 278. First Bad Version  
  - 35. Search Insert Position (this one itself)  

---

## Notes
- If target is **smaller than all elements** → return 0.  
- If target is **larger than all elements** → return len(nums).  
- Returning `left` after the loop is the key insight.  