# Day 23: Implement Queue using Stacks
# Problem Link: https://leetcode.com/problems/implement-queue-using-stacks/
# Category: Stack / Queue Simulation

class MyQueue:
    def __init__(self):
        # Two stacks: one for input, one for output
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # Always push new elements to the input stack
        self.in_stack.append(x)

    def pop(self) -> int:
        # Ensure out_stack has elements to pop
        self._move_in_to_out()
        return self.out_stack.pop()

    def peek(self) -> int:
        # Ensure out_stack has elements to peek
        self._move_in_to_out()
        return self.out_stack[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.in_stack and not self.out_stack

    def _move_in_to_out(self):
        # Move elements from in_stack → out_stack only when needed
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


# ------------------------
# ✅ Test Cases
# ------------------------
if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # Expected: 1
    print(q.pop())    # Expected: 1
    print(q.empty())  # Expected: False

    q.push(3)
    q.push(4)
    print(q.pop())    # Expected: 2
    print(q.peek())   # Expected: 3
    print(q.pop())    # Expected: 3
    print(q.pop())    # Expected: 4
    print(q.empty())  # Expected: True