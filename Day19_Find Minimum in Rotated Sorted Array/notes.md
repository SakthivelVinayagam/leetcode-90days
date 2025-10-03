# Day 19: Find Minimum in Rotated Sorted Array

**Problem**  
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/  
Category: Binary Search / Array

---

## Approach
- Use **binary search** to locate the minimum in a rotated sorted array (all elements are distinct).
- Maintain two pointers `left` and `right` with the invariant: the minimum is within `[left, right]`.
- At each step:
  - Compute `mid = (left + right) // 2`.
  - Compare `nums[mid]` with `nums[right]`:
    - If `nums[mid] > nums[right]` → the minimum lies **to the right** of `mid` → set `left = mid + 1`.
    - Else (`nums[mid] <= nums[right]`) → the minimum is in **[left..mid]** → set `right = mid`.
- Loop ends when `left == right`, which points to the minimum.

---

## Complexity
- **Time:** O(log n)  
- **Space:** O(1)

---

## Patterns
- Binary Search on Answer / Rotated Arrays  
- Comparison against the **rightmost** element to decide the half.

---

## Notes
- Works because the array is strictly increasing then rotated; no duplicates.
- If the array is not rotated (e.g., `[11,13,15,17]`), the algorithm naturally returns the first element.
- Common pitfall: using `nums[left]` for comparisons leads to trickier invariants; comparing with `nums[right]` is simpler here.
- Related:  
  - 33. Search in Rotated Sorted Array  
  - 154. Find Minimum in Rotated Sorted Array II (with duplicates → requires a tweak)