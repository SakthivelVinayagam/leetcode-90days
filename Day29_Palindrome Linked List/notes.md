# Day 29: Palindrome Linked List

**Problem**  
Link: https://leetcode.com/problems/palindrome-linked-list/  
Category: Linked List / Two Pointers

---

## Approach (O(n) time, O(1) space)
1. **Find the middle** using fast/slow pointers.  
   - `fast` moves 2 steps, `slow` moves 1 step.  
   - When `fast` ends, `slow` is at mid (for odd length) or at start of right half (for even).
2. **Reverse the second half** of the list in-place.
3. **Compare** the first half with the reversed second half node-by-node.  
   - If any mismatch → not a palindrome.
4. **(Optional) Restore** the list by reversing the second half back.

This avoids extra memory (like copying into an array or using a stack).

---

## Complexity
- **Time:** O(n) — one pass to find mid, one to reverse, one to compare.  
- **Space:** O(1) — in-place reversal.

---

## Patterns
- Two Pointers (fast/slow)  
- In-place list reversal  
- Compare halves

---

## Notes
- For **odd** lengths, the middle element can be skipped naturally because the second-half reversal starts from `slow`.  
- Be careful to only iterate up to the length of the (reversed) second half during comparison.  
- Alternative (simpler but O(n) space): push values to array and check palindrome with two pointers.