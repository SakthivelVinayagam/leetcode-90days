# Day 14: Search Insert Position
# Problem Link: https://leetcode.com/problems/search-insert-position/
# Category: Binary Search / Array

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left  # correct insert position

# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))  # Expected: 2
    print(sol.searchInsert([1,3,5,6], 2))  # Expected: 1
    print(sol.searchInsert([1,3,5,6], 7))  # Expected: 4
    print(sol.searchInsert([1,3,5,6], 0))  # Expected: 0