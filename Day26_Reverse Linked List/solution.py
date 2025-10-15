# Day 26: Reverse Linked List
# Problem Link: https://leetcode.com/problems/reverse-linked-list/
# Category: Linked List / Iteration / Recursion

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None        # previous node starts as None
        curr = head        # start from the head

        while curr:
            nxt = curr.next   # store next node
            curr.next = prev  # reverse the link
            prev = curr       # move prev forward
            curr = nxt        # move current forward

        return prev           # new head after reversal


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    # Helper to create and print linked list
    def create_list(values):
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    def to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    sol = Solution()
    print(to_list(sol.reverseList(create_list([1, 2, 3, 4, 5]))))  # [5,4,3,2,1]
    print(to_list(sol.reverseList(create_list([1, 2]))))           # [2,1]
    print(to_list(sol.reverseList(create_list([]))))               # []