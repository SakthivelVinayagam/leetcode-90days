# Day 04: Contains Duplicate
# Problem Link: https://leetcode.com/problems/contains-duplicate/
# Category: Array / Hashset

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))          # True
    print(sol.containsDuplicate([1,2,3,4]))          # False
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # True
    print(sol.containsDuplicate([]))                 # False
    print(sol.containsDuplicate([99]))               # False