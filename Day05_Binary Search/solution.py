# Day 05: Binary Search
# Problem Link: https://leetcode.com/problems/binary-search/
# Category: Array / Binary Search

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1,0,3,5,9,12], 9))   # Expected: 4
    print(sol.search([-1,0,3,5,9,12], 2))   # Expected: -1
    print(sol.search([5], 5))               # Expected: 0
    print(sol.search([5], -5))              # Expected: -1
    print(sol.search([1,2,3,4,5,6,7], 7))   # Expected: 6