# Day 26: Reverse Linked List

**Problem**  
Link: https://leetcode.com/problems/reverse-linked-list/  
Category: Linked List / Iteration / Recursion  

---

## Approach
### Iterative Solution
- Use two pointers: `prev` (initially `None`) and `curr` (starting at head).
- For each node:
  - Temporarily store `curr.next`.
  - Reverse the pointer: `curr.next = prev`.
  - Move both pointers forward.
- Continue until `curr` becomes `None`.
- Return `prev` as the new head (the last node of the original list).

### Recursive Solution (Optional)
- Base case: if `head` is `None` or `head.next` is `None`, return `head`.
- Recursively reverse the rest of the list.
- Fix the links while unwinding recursion.

---

## Complexity
- **Time:** O(n) — each node visited once.  
- **Space:** O(1) for iterative; O(n) for recursive (stack frames).

---

## Patterns
- Two-pointer pattern (prev–current).  
- Often used before:
  - Palindrome Linked List
  - Add Two Numbers (reversed)
  - Reverse Nodes in k-Group

---

## Notes
- Common mistake: forgetting to store `next` before reversing `curr.next`.  
- Iterative approach is more space-efficient.  
- Recursive version is elegant but uses stack memory.