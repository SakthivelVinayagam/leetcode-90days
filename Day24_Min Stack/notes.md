# Day 24: Min Stack

**Problem**  
Link: https://leetcode.com/problems/min-stack/  
Category: Stack / Design  

---

## Approach
- Maintain **two stacks**:
  - `stack`: holds all pushed values.
  - `min_stack`: tracks the minimum value at each stack depth.
- On `push(val)`:
  - Push `val` to `stack`.
  - Push to `min_stack` if it's empty or `val <= min_stack[-1]`.
- On `pop()`:
  - Pop top from `stack`.
  - If popped element equals `min_stack[-1]`, pop from `min_stack` too.
- `getMin()` returns top of `min_stack`, which always holds the current minimum.

---

## Complexity
- **Time:** O(1) per operation  
- **Space:** O(n)

---

## Patterns
- Stack design with auxiliary data structure.  
- Similar pattern used in:
  - Max Stack
  - Min Queue
  - Browser History / Undo-Redo stack systems.

---

## Notes
- Core idea: Each level of the stack “remembers” the min so far.  
- `min_stack` ensures O(1) retrieval instead of rescanning elements.  
- Both stacks remain synchronized for every push/pop.