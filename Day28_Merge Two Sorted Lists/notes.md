# Day 28: Merge Two Sorted Lists

**Problem**  
Link: https://leetcode.com/problems/merge-two-sorted-lists/  
Category: Linked List / Two Pointers

---

## Approach
Use a **dummy head node** and a **two-pointer merge technique**.

1. Create a dummy node to simplify pointer management.
2. Compare `list1.val` and `list2.val`:
   - Attach the smaller node to `tail.next`.
   - Advance that list’s pointer.
   - Move `tail` forward.
3. When one list ends, link the remaining part of the other.
4. Return `dummy.next` (skip dummy node).

---

## Complexity
- **Time:** O(m + n) → traverse both lists once.  
- **Space:** O(1) → reuses existing nodes (in-place merge).

---

## Patterns
- Two-pointer technique  
- Linked List traversal  
- Dummy node pattern (simplifies edge handling)

---

## Notes
- Handles empty lists gracefully.  
- Avoid creating new nodes unnecessarily.  
- Similar to the **merge step** in Merge Sort.  
- Related problems:
  - Merge k Sorted Lists
  - Remove Duplicates from Sorted List