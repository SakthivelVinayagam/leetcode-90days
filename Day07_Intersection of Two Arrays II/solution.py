# Day 07: Intersection of Two Arrays II
# Problem Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Category: Array / Hashmap; (Alt) Two Pointers when sorted

from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Always build the counter on the smaller array to reduce memory usage
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        counts = Counter(nums1)
        result = []
        for x in nums2:
            if counts.get(x, 0) > 0:
                result.append(x)
                counts[x] -= 1
        return result

# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersect([1,2,2,1], [2,2]))             # [2,2]
    print(sol.intersect([4,9,5], [9,4,9,8,4]))         # [4,9] or [9,4]
    print(sol.intersect([], []))                       # []
    print(sol.intersect([1,1,1], [1,1]))               # [1,1]
    print(sol.intersect([1,2,3], [4,5,6]))             # []