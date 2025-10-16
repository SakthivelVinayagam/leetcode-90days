# Day 32: LRU Cache
# Problem Link: https://leetcode.com/problems/lru-cache/
# Category: Hashmap + Doubly Linked List (Design)
# Goal: O(1) average time for both get and put.

class Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}  # key -> Node
        # Doubly linked list with head/tail sentinels:
        # Most-recently-used is right next to head;
        # Least-recently-used is right before tail.
        self.head = Node()  # dummy head
        self.tail = Node()  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # ----- internal helpers -----
    def _add_after_head(self, node: Node):
        """Insert node right after head (mark as most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        """Detach node from its current position."""
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _move_to_head(self, node: Node):
        """Make an existing node the most recently used."""
        self._remove_node(node)
        self._add_after_head(node)

    def _pop_lru(self) -> Node:
        """Remove and return the least-recently-used real node (before tail)."""
        lru = self.tail.prev
        self._remove_node(lru)
        return lru

    # ----- API -----
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_head(node)  # use updates recency
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # Update and move to head
            node = self.map[key]
            node.val = value
            self._move_to_head(node)
            return

        # Create new node, add to map and list
        node = Node(key, value)
        self.map[key] = node
        self._add_after_head(node)

        # Evict if over capacity
        if len(self.map) > self.cap:
            lru = self._pop_lru()
            del self.map[lru.key]


# ------------------------
# ✅ Quick Tests
# ------------------------
if __name__ == "__main__":
    # Example from prompt
    cache = LRUCache(2)
    cache.put(1, 1)                    # {1=1}
    cache.put(2, 2)                    # {1=1, 2=2}
    print(cache.get(1))    # 1        # use key=1: {2=2, 1=1}
    cache.put(3, 3)                    # evict 2 -> {1=1, 3=3}
    print(cache.get(2))    # -1
    cache.put(4, 4)                    # evict 1 -> {3=3, 4=4}
    print(cache.get(1))    # -1
    print(cache.get(3))    # 3
    print(cache.get(4))    # 4

    # Additional sanity checks
    c = LRUCache(1)
    c.put(10, 100)
    print(c.get(10))  # 100
    c.put(20, 200)    # evicts 10
    print(c.get(10))  # -1
    print(c.get(20))  # 200