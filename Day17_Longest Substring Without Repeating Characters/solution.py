# Day 17: Longest Substring Without Repeating Characters
# Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Category: String / Sliding Window / HashMap

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window with last-seen index.
        Maintain window [left..right]. For each char c at index r:
          - If c was seen and last_seen[c] >= left, move left = last_seen[c] + 1
          - Update last_seen[c] = r
          - Track best length = max(best, r-left+1)
        Time: O(n), Space: O(min(n, charset))
        """
        last_seen = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)

        return best


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()

    # Given examples
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # Expected: 3 ("abc")
    print(sol.lengthOfLongestSubstring("bbbbb"))     # Expected: 1 ("b")
    print(sol.lengthOfLongestSubstring("pwwkew"))    # Expected: 3 ("wke")

    # Edge cases
    print(sol.lengthOfLongestSubstring(""))          # Expected: 0
    print(sol.lengthOfLongestSubstring(" "))         # Expected: 1
    print(sol.lengthOfLongestSubstring("au"))        # Expected: 2
    print(sol.lengthOfLongestSubstring("dvdf"))      # Expected: 3 ("vdf")
    print(sol.lengthOfLongestSubstring("abba"))      # Expected: 2 ("ab" or "ba")