# Day 33: Kth Largest Element in an Array
# Problem Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Category: Heap / Quickselect
# Goal: Find kth largest element without full sorting.

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Use a min-heap of size k.
        # Keep only the k largest elements seen so far.
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)   # push current number
            if len(min_heap) > k:
                heapq.heappop(min_heap)     # remove smallest in heap if size > k

        # The heap root (smallest among k largest) is the kth largest element.
        return min_heap[0]


# ------------------------
# ✅ Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))   # Expected: 5

    # Example 2
    print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Expected: 4

    # Edge case: Single element
    print(sol.findKthLargest([10], 1))   # Expected: 10

    # Duplicates
    print(sol.findKthLargest([1, 2, 2, 3, 3], 3))   # Expected: 2

    # Large k
    print(sol.findKthLargest([5, 9, 1, 3, 7, 8], 6))  # Expected: 1