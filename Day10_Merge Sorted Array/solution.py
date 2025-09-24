# Day 10: Merge Sorted Array
# Problem Link: https://leetcode.com/problems/merge-sorted-array/
# Category: Array / Two Pointers (from the end)

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        In-place merge from the back.
        - i: last valid index in nums1 (m - 1)
        - j: last index in nums2 (n - 1)
        - k: write index in nums1 (m + n - 1)
        Compare nums1[i] and nums2[j], place the larger at nums1[k], and move pointers.
        If nums2 has leftovers, copy them to the front of nums1.
        """
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements, copy them (nums1 leftovers are already in place)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()

    a1 = [1,2,3,0,0,0]; sol.merge(a1, 3, [2,5,6], 3); print(a1)  # [1,2,2,3,5,6]
    a2 = [1]; sol.merge(a2, 1, [], 0); print(a2)                 # [1]
    a3 = [0]; sol.merge(a3, 0, [1], 1); print(a3)                # [1]
    a4 = [2,0]; sol.merge(a4, 1, [1], 1); print(a4)              # [1,2]
    a5 = [4,5,6,0,0,0]; sol.merge(a5, 3, [1,2,3], 3); print(a5)  # [1,2,3,4,5,6]