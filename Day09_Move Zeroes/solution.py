# Day 09: Move Zeroes
# Problem Link: https://leetcode.com/problems/move-zeroes/
# Category: Array / Two Pointers

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0  # pointer for the next non-zero position
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        # Fill the rest with zeros
        for i in range(pos, len(nums)):
            nums[i] = 0


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()

    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print(nums1)  # Expected: [1, 3, 12, 0, 0]

    nums2 = [0]
    sol.moveZeroes(nums2)
    print(nums2)  # Expected: [0]

    nums3 = [1, 2, 3]
    sol.moveZeroes(nums3)
    print(nums3)  # Expected: [1, 2, 3]

    nums4 = [0, 0, 0, 1]
    sol.moveZeroes(nums4)
    print(nums4)  # Expected: [1, 0, 0, 0]

    nums5 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    sol.moveZeroes(nums5)
    print(nums5)  # Expected: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]