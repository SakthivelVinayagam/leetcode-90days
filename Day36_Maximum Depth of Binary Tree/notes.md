# Day 36: Maximum Depth of Binary Tree

**Problem**  
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/  
Category: Tree / DFS / BFS

---

## Approach 1: Recursive DFS
The depth of a binary tree =  
`1 + max(depth of left subtree, depth of right subtree)`

### Steps:
1. If the node is `None`, return 0.
2. Recursively call on left and right children.
3. Return `1 + max(left_depth, right_depth)`.

This naturally explores all paths and computes the maximum.

---

## Approach 2: Iterative BFS (Level Order)
1. Use a queue to perform level-by-level traversal.
2. For each level, count the nodes and increment `depth`.
3. When all levels are processed, `depth` = maximum depth.

---

## Example
Input: `[3,9,20,null,null,15,7]`