# Day 1: Two Sum

from typing import List
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                # complement seen at seen[complement], current index is i
                return [seen[complement], i]
            # store current number's index after checking, so we don't pair a number with itself
            seen[num] = i
        # problem guarantees one solution; this return is for completeness
        return []
    
if __name__ == "__main__":
    s = Solution()
    tests = [
        (([2,7,11,15], 9), {0,1}),
        (([3,2,4], 6), {1,2}),
        (([3,3], 6), {0,1}),
        (([-2,0,1,4], -2), {0,1}),
    ]
    for (nums, target), expected_set in tests:
        ans = s.twoSum(nums, target)
        assert set(ans) == expected_set, f"Failed for {nums}, target={target}, got {ans}"
    print("All tests passed.")