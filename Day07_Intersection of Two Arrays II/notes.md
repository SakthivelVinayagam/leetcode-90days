# Day 07: Intersection of Two Arrays II

**Problem**  
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/  
Category: Array / Hashmap (Alt: Two Pointers for sorted arrays)

---

## Approach
- Build a frequency map (Counter) for the smaller array to save space.
- Iterate the other array: if an element’s count > 0 in the map, append to result and decrement the count.
- This yields the multiset intersection (elements appear min(count1, count2) times).

---

## Complexity
- **Time:** O(n + m) using hashmap (average).  
- **Space:** O(min(n, m)) for counts.

---

## Patterns
- Hashmap frequency counting  
- Two pointers when arrays are sorted (sort both, then advance pointers)

---

## Notes
- If arrays are already sorted: two pointers avoids extra space (after sorting if needed).
- If `nums1` ≪ `nums2`: count `nums1`, stream through `nums2` to minimize memory.
- If `nums2` is on disk / memory-limited: count the in-memory smaller array; process `nums2` in chunks and output on the fly.