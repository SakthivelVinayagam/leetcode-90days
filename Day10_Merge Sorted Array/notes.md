# Day 10: Merge Sorted Array

**Problem**  
Link: https://leetcode.com/problems/merge-sorted-array/  
Category: Array / Two Pointers (from the end)

---

## Approach
- Merge **in-place from the end** of `nums1` to avoid overwriting valid data.
- Pointers:
  - `i = m - 1` → last valid element in `nums1`
  - `j = n - 1` → last element in `nums2`
  - `k = m + n - 1` → write position in `nums1`
- While `i >= 0` and `j >= 0`:
  - Place the larger of `nums1[i]` and `nums2[j]` at `nums1[k]` and move the corresponding pointer.
- After loop, if `nums2` still has remaining elements, copy them to the front of `nums1`.

---

## Complexity
- **Time:** O(m + n)  
- **Space:** O(1) (in-place)

---

## Patterns
- Two Pointers from the end
- In-place merge

---

## Notes
- We only need to copy leftovers from `nums2`; leftovers in `nums1` are already in correct position.
- Works when `m = 0` (all from `nums2`) and when `n = 0` (already sorted).
- Avoid merging from the front—it risks overwriting unprocessed values.