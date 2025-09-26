# Day 12: Climbing Stairs
# Problem Link: https://leetcode.com/problems/climbing-stairs/
# Category: Dynamic Programming

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n
        
        # Use two variables instead of DP array (O(1) space)
        prev1, prev2 = 1, 2  # dp[1] = 1, dp[2] = 2
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev1, prev2 = prev2, curr
        return prev2


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))  # Expected: 2 → (1+1, 2)
    print(sol.climbStairs(3))  # Expected: 3 → (1+1+1, 1+2, 2+1)
    print(sol.climbStairs(5))  # Expected: 8
    print(sol.climbStairs(1))  # Expected: 1
    print(sol.climbStairs(10)) # Expected: 89