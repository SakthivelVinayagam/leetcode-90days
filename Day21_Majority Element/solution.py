# Day 21: Majority Element
# Problem Link: https://leetcode.com/problems/majority-element/
# Category: Array / Hashmap / Boyer–Moore Majority Vote

from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer–Moore Majority Vote:
        Keep a candidate and a counter. When counter hits 0, pick current number
        as new candidate. Increase for equal, decrease for different.
        Since majority (> n/2) is guaranteed to exist, the final candidate is the answer.
        Time: O(n), Space: O(1)
        """
        count = 0
        candidate = None
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate


# ------------------------
# 🔹 Alternative Approach (for interview comparison)
# ------------------------
# Using HashMap (Counter) – simpler but uses extra space O(n)
#
# def majorityElement(nums: List[int]) -> int:
#     counts = Counter(nums)
#     return max(counts.keys(), key=counts.get)
#
# Explanation:
# - Count frequency of each element.
# - Return the element with the highest count.
# - Still O(n) time but O(n) space.


# ------------------------
# ✅ Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()

    # Prompt examples
    print(sol.majorityElement([3, 2, 3]))              # Expected: 3
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Expected: 2

    # Additional tests
    print(sol.majorityElement([1]))                    # Expected: 1
    print(sol.majorityElement([6, 5, 5]))              # Expected: 5
    print(sol.majorityElement([9, 9, 9, 1, 2, 3, 9]))  # Expected: 9