# Day 31: Design Linked List

**Problem**  
Link: https://leetcode.com/problems/design-linked-list/  
Category: Linked List / Design

---

## Approach
Implement a **doubly linked list** with **head/tail sentinels** to simplify edge cases:

- Structure: `head <-> ...nodes... <-> tail`
- Maintain `size` for O(1) length checks.
- Core helpers:
  - `_get_node(index)`: returns node at index using bidirectional traversal
    (choose from head or tail depending on proximity).
  - `_insert_before(ref, node)`: O(1) insert before a reference node.
  - `_remove(node)`: O(1) delete a node.

**API mapping**
- `get(index)`: locate with `_get_node`, return `val` or `-1`.
- `addAtHead(val)`: insert before `head.next`.
- `addAtTail(val)`: insert before `tail`.
- `addAtIndex(index, val)`: if `index == size` append at tail; if `0 <= index < size` insert before node at `index`; else ignore.
- `deleteAtIndex(index)`: `_get_node` then `_remove`.

---

## Complexity
- `get`, `addAtIndex`, `deleteAtIndex`: **O(min(index, n-index))** due to traversal.
- `addAtHead`, `addAtTail`: **O(1)** actual insertion.
- Space: **O(n)** for nodes.

---

## Patterns
- Sentinel nodes to avoid null checks on ends.
- Bidirectional traversal optimization.

---

## Notes
- Using **doubly** linked list makes deletion and insertion around arbitrary nodes O(1) once found.
- Be careful with off-by-one in `_get_node` and when `index == size` (append).