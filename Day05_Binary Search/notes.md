# Day 05: Binary Search  

**Problem**  
Link: https://leetcode.com/problems/binary-search/  
Category: Array / Binary Search  

---

## Approach  
- Since the array is sorted, use Binary Search (O(log n)) instead of linear scan (O(n)).  
- Initialize two pointers: `left = 0`, `right = len(nums) - 1`.  
- While `left <= right`:  
  - Compute `mid = (left + right) // 2`.  
  - If `nums[mid] == target` → return `mid`.  
  - If `nums[mid] < target` → move `left = mid + 1`.  
  - Else → move `right = mid - 1`.  
- If loop finishes with no match → return `-1`.  

---

## Complexity  
- **Time:** O(log n) (halves the search space each iteration).  
- **Space:** O(1) (constant extra space).  

---

## Patterns  
- Binary Search / Divide and Conquer  
- Related problems:  
  - Search Insert Position  
  - First Bad Version  
  - Search in Rotated Sorted Array  

---

## Notes  
- Edge cases:  
  - Single-element array → works correctly.  
  - Target not found → return `-1`.  
  - Ensure integer division (`//`) is used for `mid` in Python.  
- Common pitfalls:  
  - Forgetting to update `left` or `right`, causing infinite loop.  
  - Returning the value instead of the index.  