# Day 15: Group Anagrams

**Problem**  
Link: https://leetcode.com/problems/group-anagrams/  
Category: Hashmap / String

---

## Approach
- **Count Signature (recommended, O(N * L))**  
  - For each word, build a 26-length frequency vector of letters `a..z` and use the tuple as a key in a hashmap:  
    - Example: "eat" → [1,0,0,...,1,...,1] (for e, a, t)  
  - Group all words sharing the same signature.
- **Alternative (Sorted Key, O(N * L log L))**  
  - Sort each string and use the sorted string as the key:  
    - "eat" → "aet", "tea" → "aet", "ate" → "aet"

`N` = number of strings, `L` = average string length.

---

## Complexity
- **Count Signature:** Time O(N * L), Space O(N * L) for stored groups/keys.  
- **Sorted Key:** Time O(N * L log L), Space O(N * L).

---

## Patterns
- Hashmap bucketing  
- Canonical representation (signature) of anagrams  
- Frequency counting vs. normalized (sorted) keys

---

## Notes
- Works with empty strings and single-letter words.  
- For large strings, **count signature** avoids `log L` factor and is typically faster.  
- Output order and group order are not specified—any order is accepted.