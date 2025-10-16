# Day 28: Merge Two Sorted Lists
# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Category: Linked List / Two Pointers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify head management
        dummy = ListNode()
        tail = dummy

        # Traverse both lists until one runs out
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach remaining elements from the non-empty list
        tail.next = list1 or list2

        # Return the merged list (skip dummy)
        return dummy.next


# ------------------------
# Test Cases
# ------------------------
def list_to_linkedlist(arr):
    """Convert a Python list → Linked List"""
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    """Convert a Linked List → Python list"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    s = Solution()

    # Example 1
    l1 = list_to_linkedlist([1, 2, 4])
    l2 = list_to_linkedlist([1, 3, 4])
    print(linkedlist_to_list(s.mergeTwoLists(l1, l2)))  # Expected: [1,1,2,3,4,4]

    # Example 2
    l1 = list_to_linkedlist([])
    l2 = list_to_linkedlist([])
    print(linkedlist_to_list(s.mergeTwoLists(l1, l2)))  # Expected: []

    # Example 3
    l1 = list_to_linkedlist([])
    l2 = list_to_linkedlist([0])
    print(linkedlist_to_list(s.mergeTwoLists(l1, l2)))  # Expected: [0]