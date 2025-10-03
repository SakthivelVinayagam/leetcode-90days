# Day 19: Find Minimum in Rotated Sorted Array
# Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Category: Binary Search / Array

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Binary search on a rotated sorted array (distinct elements).
        Key idea:
          - Compare middle with right end:
             * If nums[mid] > nums[right], the min is in the right half (mid+1 .. right)
             * Else, the min is in the left half including mid (left .. mid)
        Loop invariant: the minimum is always within [left, right].
        Time: O(log n), Space: O(1)
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # Min must be to the right of mid
                left = mid + 1
            else:
                # Mid could be the min, keep it in range
                right = mid
        return nums[left]


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()

    # Given examples
    print(sol.findMin([3,4,5,1,2]))         # Expected: 1
    print(sol.findMin([4,5,6,7,0,1,2]))     # Expected: 0
    print(sol.findMin([11,13,15,17]))       # Expected: 11  (no rotation)

    # Additional tests
    print(sol.findMin([2,3,4,5,6,7,1]))     # Expected: 1
    print(sol.findMin([1]))                 # Expected: 1
    print(sol.findMin([5,1,2,3,4]))         # Expected: 1
    print(sol.findMin([2,1]))               # Expected: 1