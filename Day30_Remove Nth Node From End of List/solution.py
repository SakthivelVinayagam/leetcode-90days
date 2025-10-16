# Day 30: Remove Nth Node From End of List
# Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Category: Linked List / Two Pointers

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        One-pass approach using two pointers:
        1. Move 'fast' n steps ahead.
        2. Move both 'fast' and 'slow' until 'fast' hits the end.
        3. 'slow.next' is the node to remove.
        """
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Step 1: Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Step 2: Move both until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Step 3: Remove the nth node
        slow.next = slow.next.next

        return dummy.next


# ------------------------
# ✅ Test Helpers & Cases
# ------------------------
def list_to_linkedlist(arr):
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def linkedlist_to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()
    print(linkedlist_to_list(sol.removeNthFromEnd(list_to_linkedlist([1,2,3,4,5]), 2)))  # [1,2,3,5]
    print(linkedlist_to_list(sol.removeNthFromEnd(list_to_linkedlist([1]), 1)))          # []
    print(linkedlist_to_list(sol.removeNthFromEnd(list_to_linkedlist([1,2]), 1)))        # [1]
    print(linkedlist_to_list(sol.removeNthFromEnd(list_to_linkedlist([1,2]), 2)))        # [2]