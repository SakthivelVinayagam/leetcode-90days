# Day 16: Subarray Sum Equals K
# Problem Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Category: Array / Hashmap / Prefix Sum

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Prefix Sum + HashMap (counts)
        --------------------------------
        Let prefix[i] = sum(nums[0..i-1]).
        For each index r (1-based in prefix terms), we want # of l < r such that:
            prefix[r] - prefix[l] = k  ->  prefix[l] = prefix[r] - k
        Maintain a hashmap 'count' of prefix sums we've seen so far.
        Initialize count[0] = 1 to count subarrays that start at index 0.

        Time:  O(n)
        Space: O(n)
        """
        count = defaultdict(int)
        count[0] = 1  # empty prefix to allow subarrays starting at index 0

        total = 0
        prefix = 0
        for x in nums:
            prefix += x
            total += count[prefix - k]  # how many previous prefixes make sum k
            count[prefix] += 1
        return total


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()

    # Examples from the prompt
    print(sol.subarraySum([1,1,1], 2))     # Expected: 2
    print(sol.subarraySum([1,2,3], 3))     # Expected: 2

    # Additional tests
    print(sol.subarraySum([0,0,0], 0))     # Expected: 6  (all subarrays)
    print(sol.subarraySum([3,4,7,-2,2,1,4,2], 7))  # Expected: 4
    print(sol.subarraySum([-1,-1,1], 0))   # Expected: 1
    print(sol.subarraySum([1], 0))         # Expected: 0
    print(sol.subarraySum([1,-1,1,-1], 0)) # Expected: 4