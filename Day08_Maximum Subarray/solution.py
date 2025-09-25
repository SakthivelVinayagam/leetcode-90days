# Day 08: Maximum Subarray
# Problem Link: https://leetcode.com/problems/maximum-subarray/
# Category: Array / Dynamic Programming (Kadane), (Alt) Divide & Conquer

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm Explanation:
        -------------------------------
        - The maximum subarray ending at index i is either:
            (a) the element itself (nums[i]) OR
            (b) the element plus the maximum subarray ending at i-1.
        - So we update:
            curr_sum = max(nums[i], curr_sum + nums[i])
        - And keep track of the global max:
            max_sum = max(max_sum, curr_sum)

        Why it works:
        - If curr_sum + nums[i] is worse than just nums[i],
          we "reset" the subarray at nums[i].
        - Guarantees O(n) time and O(1) space.

        Common pitfalls:
        - Initializing curr_sum = 0 can fail for all-negative arrays.
        - The correct initialization is curr_sum = max_sum = nums[0].

        Edge Cases:
        - All negative numbers → largest single element.
        - Single element arrays.
        """

        curr_sum = max_sum = nums[0]
        for x in nums[1:]:
            curr_sum = max(x, curr_sum + x)
            max_sum = max(max_sum, curr_sum)
        return max_sum


# Optional: Divide & Conquer version (O(n log n))
def max_subarray_divide_conquer(nums: List[int]) -> int:
    def helper(lo: int, hi: int) -> int:
        if lo == hi:
            return nums[lo]

        mid = (lo + hi) // 2
        left_best = helper(lo, mid)
        right_best = helper(mid + 1, hi)

        # max suffix sum on left
        s, best_left_suffix = 0, float("-inf")
        for i in range(mid, lo - 1, -1):
            s += nums[i]
            best_left_suffix = max(best_left_suffix, s)

        # max prefix sum on right
        s, best_right_prefix = 0, float("-inf")
        for i in range(mid + 1, hi + 1):
            s += nums[i]
            best_right_prefix = max(best_right_prefix, s)

        cross = best_left_suffix + best_right_prefix
        return max(left_best, right_best, cross)

    return helper(0, len(nums) - 1)


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected 6
    print(sol.maxSubArray([1]))                      # Expected 1
    print(sol.maxSubArray([5,4,-1,7,8]))            # Expected 23
    print(sol.maxSubArray([-1,-2,-3]))               # Expected -1

    # Sanity-check D&C variant
    print(max_subarray_divide_conquer([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(max_subarray_divide_conquer([1]))                      # 1
    print(max_subarray_divide_conquer([5,4,-1,7,8]))            # 23
    print(max_subarray_divide_conquer([-1,-2,-3]))              # -1