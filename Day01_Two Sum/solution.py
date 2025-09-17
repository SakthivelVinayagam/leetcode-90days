# Day 01: Two Sum
# Problem Link: https://leetcode.com/problems/two-sum/
# Category: Array / Hashmap

from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                # Found the solution: indices of complement and current number
                return [seen[complement], i]
            # Store current number after checking, to avoid using the same element twice
            seen[num] = i
        return []  # Problem guarantees one solution

# ------------------------
# Test Cases
# ------------------------ 
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))        # [1, 2]
    print(sol.twoSum([3, 3], 6))           # [0, 1]
    print(sol.twoSum([-2, 0, 1, 4], -2))   # [0, 1]