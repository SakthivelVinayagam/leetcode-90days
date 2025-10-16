# Day 31: Design Linked List
# Problem Link: https://leetcode.com/problems/design-linked-list/
# Category: Linked List / Design
# Implementation: Doubly Linked List with head/tail sentinels for O(1) edge ops.

class Node:
    __slots__ = ("val", "prev", "next")
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        # Sentinels: head <-> ...nodes... <-> tail
        self.head = Node()   # dummy head
        self.tail = Node()   # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    # ----- helpers -----
    def _get_node(self, index: int) -> Node | None:
        """Return the real node at 0-based index, or None if invalid."""
        if index < 0 or index >= self.size:
            return None
        # Pick shortest direction
        if index < self.size // 2:
            cur = self.head.next
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail.prev
            for _ in range(self.size - 1 - index):
                cur = cur.prev
        return cur

    def _insert_before(self, ref: Node, node: Node):
        """Insert node before ref (ref is an existing node)."""
        prev = ref.prev
        prev.next = node
        node.prev = prev
        node.next = ref
        ref.prev = node
        self.size += 1

    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1

    # ----- API required by the problem -----
    def get(self, index: int) -> int:
        n = self._get_node(index)
        return n.val if n else -1

    def addAtHead(self, val: int) -> None:
        self._insert_before(self.head.next, Node(val))

    def addAtTail(self, val: int) -> None:
        self._insert_before(self.tail, Node(val))

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == self.size:
            self._insert_before(self.tail, Node(val))
        else:
            ref = self._get_node(index)
            self._insert_before(ref, Node(val))

    def deleteAtIndex(self, index: int) -> None:
        n = self._get_node(index)
        if n:
            self._remove(n)


# ------------------------
# ✅ Test harness (basic)
# ------------------------
if __name__ == "__main__":
    ll = MyLinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)      # 1 -> 2 -> 3
    print(ll.get(1))         # Expected: 2
    ll.deleteAtIndex(1)      # 1 -> 3
    print(ll.get(1))         # Expected: 3

    # Extra checks
    ll2 = MyLinkedList()
    ll2.addAtIndex(0, 10)    # 10
    ll2.addAtIndex(1, 20)    # 10 -> 20
    ll2.addAtIndex(1, 15)    # 10 -> 15 -> 20
    print([ll2.get(i) for i in range(ll2.size)])  # [10, 15, 20]
    ll2.deleteAtIndex(0)     # 15 -> 20
    ll2.deleteAtIndex(1)     # 15
    print([ll2.get(i) for i in range(ll2.size)])  # [15]