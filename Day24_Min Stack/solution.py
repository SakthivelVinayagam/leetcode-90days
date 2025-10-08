# Day 24: Min Stack
# Problem Link: https://leetcode.com/problems/min-stack/
# Category: Stack / Design

class MinStack:
    def __init__(self):
        # main_stack stores all values
        # min_stack keeps track of current minimum at each level
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if min_stack empty or new val <= current min, push it
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # if popped value is the current minimum, pop from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # return top element of main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # top of min_stack always holds the current minimum
        return self.min_stack[-1]


# ------------------------
# ✅ Test Cases
# ------------------------
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # Expected: -3
    minStack.pop()
    print(minStack.top())     # Expected: 0
    print(minStack.getMin())  # Expected: -2