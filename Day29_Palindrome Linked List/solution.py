# Day 29: Palindrome Linked List
# Problem Link: https://leetcode.com/problems/palindrome-linked-list/
# Category: Linked List / Two Pointers

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        O(n) time, O(1) extra space:
        1) Find middle with slow/fast pointers.
        2) Reverse second half in-place.
        3) Compare first half and reversed second half.
        4) (Optional) Restore the list by reversing second half back.
        """
        if not head or not head.next:
            return True

        # 1) Find middle (slow ends at mid for odd length, first of right half for even)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half
        second = self._reverse(slow)

        # 3) Compare halves
        p1, p2 = head, second
        result = True
        while p2:  # second half is <= first in length
            if p1.val != p2.val:
                result = False
                break
            p1 = p1.next
            p2 = p2.next

        # 4) Optional: restore list (not required by LeetCode, but good hygiene)
        self._reverse(second)

        return result

    def _reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, node
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


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
    print(sol.isPalindrome(list_to_linkedlist([1,2,2,1])))  # True
    print(sol.isPalindrome(list_to_linkedlist([1,2])))      # False
    print(sol.isPalindrome(list_to_linkedlist([1])))        # True
    print(sol.isPalindrome(list_to_linkedlist([1,2,3,2,1])))# True
    print(sol.isPalindrome(list_to_linkedlist([1,0,1,0])))  # False