# Day 36: Maximum Depth of Binary Tree
# Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Category: Tree / DFS / BFS

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive DFS Approach
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 1 + maximum of left and right subtree depths
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Iterative BFS Approach (Level Order Traversal)
    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        from collections import deque
        queue = deque([root])
        depth = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    # Example 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxDepth(root))  # Expected: 3

    # Example 2
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(Solution().maxDepth(root))  # Expected: 2

    # Edge case: Empty tree
    print(Solution().maxDepth(None))  # Expected: 0