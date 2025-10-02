# Day 18: Squares of a Sorted Array

**Problem**  
Link: https://leetcode.com/problems/squares-of-a-sorted-array/  
Category: Array / Two Pointers  

---

## Approach 1: Square then Sort
- Square each number, then sort the array.  
- **Time:** O(n log n)  
- **Space:** O(n)  
- Simple to implement but not optimal.  

---

## Approach 2: Two Pointers (Optimized)
- Array is sorted, but negatives can affect the order after squaring.  
- The largest square always comes from either the leftmost (large negative) or rightmost (large positive).  
- Use two pointers (`left`, `right`):  
  - Compare `abs(nums[left])` vs `abs(nums[right])`.  
  - Place the larger square at the end of the result array.  
  - Move that pointer inward.  
- Continue until all elements are placed.  

---

## Complexity
- **Time:** O(n)  
- **Space:** O(n) (result array)  

---

## Patterns
- Two Pointers (meet in middle).  
- Similar to: Merge Sorted Array, Container With Most Water.  

---

## Notes
- Approach 1 (sort) is acceptable but slower.  
- Approach 2 (two pointers) is interview-quality.  
- Edge cases:  
  - All negatives (e.g., [-5,-3,-1]) → result sorted after squaring.  
  - All positives (already sorted).  
  - Single element array.  