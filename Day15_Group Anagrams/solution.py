# Day 15: Group Anagrams
# Problem Link: https://leetcode.com/problems/group-anagrams/
# Category: Hashmap / String

from typing import List, Dict, Tuple
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach 1 (Count Signature, O(N * L)):
        Build a frequency signature (26-length tuple) for each string.
        Use it as a dictionary key to collect anagram groups.
        Faster than sorting for long strings.
        """
        groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())

    def groupAnagrams_sorted(self, strs: List[str]) -> List[List[str]]:
        """
        Approach 2 (Sorted Key, O(N * L log L)):
        Sort each string and use the sorted string as key.
        Simpler to write; often fast enough in practice.
        """
        groups: Dict[str, List[str]] = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())


# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()

    # Basic examples
    print(sorted([sorted(g) for g in sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])]))
    # Expected (order may vary): [["ate","eat","tea"], ["nat","tan"], ["bat"]]

    print(sol.groupAnagrams([""]))   # [[""]]
    print(sol.groupAnagrams(["a"]))  # [["a"]]

    # Mixed sizes / duplicates
    data = ["abc","bca","cab","aaaa","aa","a","", "", "ab","ba","xyz"]
    print(sorted([sorted(g) for g in sol.groupAnagrams(data)]))

    # Verify alternative approach returns same grouping size
    res1 = sol.groupAnagrams(data)
    res2 = sol.groupAnagrams_sorted(data)
    assert sorted(sorted(g) for g in res1) == sorted(sorted(g) for g in res2)
    print("All tests passed.")