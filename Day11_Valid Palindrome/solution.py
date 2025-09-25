# Day 11: Valid Palindrome
# Problem Link: https://leetcode.com/problems/valid-palindrome/
# Category: String / Two Pointers

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric, make lowercase
        filtered = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # Compare with its reverse
        return filtered == filtered[::-1]


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(sol.isPalindrome("race a car"))  # False
    print(sol.isPalindrome(" "))  # True (empty after cleaning)
    print(sol.isPalindrome("0P"))  # False
    print(sol.isPalindrome("Madam"))  # True