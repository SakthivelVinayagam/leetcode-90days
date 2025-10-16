# Day 30: Remove Nth Node From End of List

**Problem**  
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/  
Category: Linked List / Two Pointers  

---

## Approach (One Pass)
Use **two pointers** (`fast` and `slow`) with a **dummy node**:
1. Initialize both at the dummy node before `head`.
2. Move `fast` pointer `n` steps ahead.
3. Move both `fast` and `slow` one step at a time until `fast` reaches the end.
4. Now `slow` points to the node *before* the target → remove `slow.next`.

This avoids counting total length (one-pass O(n) approach).

---

## Complexity
- **Time:** O(n) — single traversal through list.  
- **Space:** O(1) — only two pointers used.  

---

## Patterns
- Two Pointers (fast/slow gap method)  
- Dummy Node (simplifies edge cases like removing the head)

---

## Notes
- Use dummy node to handle deletion of head easily.  
- Always move `fast` first by `n` steps, then sync move until `fast` hits null.  
- For `n == length`, the first node (head) is removed.  
- Related problems:  
  - Rotate List  
  - Remove Linked List Elements  
  - Middle of the Linked List