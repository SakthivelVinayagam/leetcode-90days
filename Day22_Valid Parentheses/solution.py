# Day 22: Valid Parentheses
# Problem Link: https://leetcode.com/problems/valid-parentheses/
# Category: Stack / String

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Use a stack to track opening brackets.
        For every closing bracket, check if it matches the top of the stack.
        If mismatch or premature closing → invalid.
        At the end, stack must be empty.
        """
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pairs.values():           # opening bracket
                stack.append(ch)
            elif ch in pairs:                  # closing bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False               # mismatch or no opening
                stack.pop()                    # valid pair found → pop
            else:
                return False                   # invalid char (should not occur)

        return not stack                       # true if all brackets matched


# ------------------------
# ✅ Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()

    # From examples
    print(sol.isValid("()"))          # True
    print(sol.isValid("()[]{}"))      # True
    print(sol.isValid("(]"))          # False
    print(sol.isValid("([])"))        # True
    print(sol.isValid("([)]"))        # False

    # Additional tests
    print(sol.isValid("{[]}"))        # True
    print(sol.isValid("["))           # False
    print(sol.isValid("]"))           # False