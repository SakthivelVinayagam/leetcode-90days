# Day 23: Implement Queue using Stacks

**Problem**  
Link: https://leetcode.com/problems/implement-queue-using-stacks/  
Category: Stack / Queue Simulation  

---

## Approach
- Use **two stacks**:
  - `in_stack`: holds elements pushed recently.
  - `out_stack`: used for popping/peeking in FIFO order.
- When popping or peeking:
  - If `out_stack` is empty, move all elements from `in_stack` to `out_stack`.
  - This reverses order → front of queue is now top of `out_stack`.
- Push operations always go to `in_stack`.

---

## Complexity
- **Amortized Time:** O(1) per operation  
  (Each element moves from `in_stack` → `out_stack` only once)
- **Space:** O(n)

---

## Patterns
- Stack-based Queue simulation  
- Related problems:
  - Implement Stack using Queues
  - Min Stack
  - Browser History (similar logic with 2 stacks)

---

## Notes
- `_move_in_to_out()` ensures amortized efficiency.  
- Only transfer when `out_stack` is empty → minimizes overhead.  
- Classic interview problem testing understanding of **data structure symmetry**.