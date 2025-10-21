# Day 35: Binary Tree Inorder Traversal

**Problem**  
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/  
Category: Tree / DFS / Stack

---

## Approach
Perform **Inorder Traversal (Left → Node → Right)** using either recursion or an iterative stack-based method.

1. **Recursive Approach**
   - Visit the left child.
   - Record the current node value.
   - Visit the right child.

2. **Iterative Approach (Follow-up)**
   - Use a stack to simulate recursion.
   - Traverse down the left subtree, pushing nodes onto the stack.
   - Pop the stack when reaching a leaf, record value, then move right.

---

## Example
For the tree `[1, null, 2, 3]`: