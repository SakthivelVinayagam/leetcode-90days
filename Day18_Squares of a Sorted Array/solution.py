# Day 18: Squares of a Sorted Array
# Problem Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# Category: Array / Two Pointers

from typing import List

class Solution:
    # Approach 1: Trivial (Square then Sort)
    def sortedSquares_sort(self, nums: List[int]) -> List[int]:
        """
        Square each element then sort.
        Time: O(n log n)
        Space: O(n)
        """
        return sorted([x * x for x in nums])

    # Approach 2: Optimized (Two Pointers)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Two-pointer approach:
        - Biggest square comes from leftmost (large negative) or rightmost (large positive).
        - Compare abs(left) vs abs(right), place larger square at end of result.
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
    
    print("Sort approach:")
    print(sol.sortedSquares_sort([-4, -1, 0, 3, 10]))   # [0,1,9,16,100]

    print("Two-pointer approach:")
    print(sol.sortedSquares([-4, -1, 0, 3, 10]))        # [0,1,9,16,100]
    print(sol.sortedSquares([-7, -3, 2, 3, 11]))        # [4,9,9,49,121]
    print(sol.sortedSquares([0]))                       # [0]
    print(sol.sortedSquares([-5, -3, -2, -1]))          # [1,4,9,25]
    print(sol.sortedSquares([1, 2, 3, 4]))              # [1,4,9,16]