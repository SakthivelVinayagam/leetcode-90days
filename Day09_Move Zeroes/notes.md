# Day 09: Move Zeroes  
**Problem**  
Link: [https://leetcode.com/problems/move-zeroes/](https://leetcode.com/problems/move-zeroes/)  
Category: Array / Two Pointers  

---

## Approach  
- Use a pointer `pos` to track the next position for a non-zero element.  
- Iterate through the array:  
  - If the current element is non-zero, place it at `nums[pos]` and increment `pos`.  
- After processing all elements, fill the rest of the array from `pos` to end with zeros.  
- This ensures all non-zeros are shifted to the front and zeros moved to the end, while keeping relative order intact.  

---

## Complexity  
- **Time:** O(n) (single pass through the array + another pass to fill zeros).  
- **Space:** O(1) (in-place, no extra storage).  

---

## Patterns  
- Two Pointers (read + write pointer).  
- In-place array modification.  
- Related to: Remove Element, Remove Duplicates from Sorted Array.  

---

## Notes  
- Must **not** create a copy — modify in-place.  
- Be careful to maintain **relative order** of non-zero elements.  
- Edge cases:  
  - All zeros → array remains unchanged.  
  - No zeros → array remains unchanged.  
  - Mixed zeros and non-zeros → relative order must be preserved.  