# Day 35: Binary Tree Inorder Traversal
# Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Category: Tree / DFS / Stack

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)          # Step 1: Visit left subtree
            result.append(node.val)     # Step 2: Visit node itself
            inorder(node.right)         # Step 3: Visit right subtree
        inorder(root)
        return result

    # Iterative Solution (Follow-up)
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        curr = root
        while curr or stack:
            # Traverse to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            # Process the top node
            curr = stack.pop()
            result.append(curr.val)
            # Move to the right subtree
            curr = curr.right
        return result


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    # Example 1: [1, None, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().inorderTraversal(root))  # Expected: [1, 3, 2]

    # Example 2: [1,2,3,4,5,None,8,None,None,6,7,9]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right.right.left = TreeNode(9)
    print(Solution().inorderTraversal(root))  # Expected: [4,2,6,5,7,1,3,9,8]

    # Example 3: []
    print(Solution().inorderTraversal(None))  # Expected: []

    # Example 4: [1]
    root = TreeNode(1)
    print(Solution().inorderTraversal(root))  # Expected: [1]