# Day 25: Linked List Cycle

**Problem**  
Link: https://leetcode.com/problems/linked-list-cycle/  
Category: Linked List / Two Pointers  

---

## Approach
- Use **Floyd’s Tortoise and Hare Algorithm**:
  - Initialize two pointers: `slow` and `fast` at head.
  - Move `slow` by 1 step and `fast` by 2 steps each iteration.
  - If at any point `slow == fast`, a cycle exists.
  - If `fast` or `fast.next` becomes `None`, the list terminates — no cycle.

---

## Complexity
- **Time:** O(n) — each pointer traverses the list at most once.  
- **Space:** O(1) — no extra data structures.

---

## Patterns
- Two-pointer technique.
- Same principle used in:
  - Find start of cycle (Linked List Cycle II)
  - Detect palindrome in linked list
  - Fast-slow pointer intersection problems.

---

## Notes
- Avoid using sets or hashmaps to store visited nodes — violates O(1) space.
- Works even if the cycle starts anywhere, not necessarily at the head.
- Intuition:  
  - If a fast pointer “laps” the slow pointer → a loop exists.