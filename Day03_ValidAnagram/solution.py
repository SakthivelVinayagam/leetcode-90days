# Day 03: Valid Anagram
# Problem Link: https://leetcode.com/problems/valid-anagram/
# Category: Hashmap / String

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick check: if lengths differ, can't be an anagram
        if len(s) != len(t):
            return False
        
        # Count characters in both strings
        return Counter(s) == Counter(t)


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
    print(sol.isAnagram("a", "a"))              # True
    print(sol.isAnagram("ab", "ba"))            # True
    print(sol.isAnagram("hello", "bello"))      # False