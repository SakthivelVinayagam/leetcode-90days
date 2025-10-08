# Day 25: Linked List Cycle
# Problem Link: https://leetcode.com/problems/linked-list-cycle/
# Category: Linked List / Two Pointers

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Use Floyd’s Tortoise & Hare algorithm
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next          # move 1 step
            fast = fast.next.next     # move 2 steps
            if slow == fast:
                return True  # cycle detected

        return False  # no cycle found


# ------------------------
# ✅ Test Cases
# ------------------------
if __name__ == "__main__":
    # Helper to create a linked list with optional cycle
    def create_list(values, pos):
        nodes = [ListNode(v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos != -1:
            nodes[-1].next = nodes[pos]
        return nodes[0] if nodes else None

    sol = Solution()

    # Example 1
    head = create_list([3, 2, 0, -4], 1)
    print(sol.hasCycle(head))  # Expected: True

    # Example 2
    head = create_list([1, 2], 0)
    print(sol.hasCycle(head))  # Expected: True

    # Example 3
    head = create_list([1], -1)
    print(sol.hasCycle(head))  # Expected: False