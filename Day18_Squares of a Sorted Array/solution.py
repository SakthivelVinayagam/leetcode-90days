# Day 18: Squares of a Sorted Array
# Problem Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# Category: Array / Two Pointers

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Two-pointer approach:
        - Numbers may be negative, but their squares become positive.
        - The largest square comes from either leftmost (negative large abs) 
          or rightmost (positive large).
        - Use two pointers (left, right), place larger square at the end of result.
        
        Time: O(n)
        Space: O(n)
        """
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] ** 2
                left += 1
            else:
                res[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return res


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.sortedSquares([-4, -1, 0, 3, 10]))   # Expected: [0,1,9,16,100]
    print(sol.sortedSquares([-7, -3, 2, 3, 11]))   # Expected: [4,9,9,49,121]
    print(sol.sortedSquares([0]))                  # Expected: [0]
    print(sol.sortedSquares([-5, -3, -2, -1]))     # Expected: [1,4,9,25]
    print(sol.sortedSquares([1, 2, 3, 4]))         # Expected: [1,4,9,16]