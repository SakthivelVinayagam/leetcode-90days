# Day 32: LRU Cache

**Problem**  
Link: https://leetcode.com/problems/lru-cache/  
Category: Hashmap + Doubly Linked List (Design)  
Requirement: `get` and `put` in O(1) average time.

---

## Approach
Use **two data structures** together:

1) **HashMap (key → node)** for O(1) lookup/update.  
2) **Doubly Linked List** to track recency:
   - **Most Recently Used (MRU)** node sits **right after the dummy head**.
   - **Least Recently Used (LRU)** node sits **right before the dummy tail**.
   - On access (`get`) or update (`put`), move the node to the head (MRU).
   - When capacity is exceeded, remove the node right before tail (LRU).

**Why doubly list?**  
Insert/remove a node in O(1) when you already have the pointer (unlike singly list which needs predecessor).

---

## Operations
- `get(key)`:
  - If key not found → `-1`.
  - Else move node to head (mark as MRU) and return value.

- `put(key, value)`:
  - If key exists: update value and move node to head.
  - Else:
    - Create node, insert after head, add to map.
    - If over capacity: pop node before tail (LRU) and remove from map.

---

## Complexity
- **Time:** O(1) average per `get`/`put`.  
- **Space:** O(capacity) for map + list.

---

## Patterns
- HashMap + Doubly Linked List (classic LRU/LFU patterns)
- Sentinels (dummy head/tail) to simplify edge cases

---

## Notes
- Moving a node to head = remove from current position + insert after head.
- Eviction only when size exceeds capacity **after** insertion.
- Update existing key in-place; do not create duplicates.

**Related:** LFU Cache (needs frequency buckets), Design Linked List.