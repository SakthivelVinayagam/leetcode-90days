# Day 03: Valid Anagram

**Problem**  
Link: https://leetcode.com/problems/valid-anagram/  
Category: Hashmap / String  

---

## Approach
- First check: if lengths differ → immediately return False.  
- Use a frequency counter (hashmap) to count characters in both strings.  
- Compare the two counters: if equal → return True, else False.  
- Python shortcut: `collections.Counter(s) == Counter(t)`  

---

## Complexity
- **Time:** O(n) (single pass to count characters)  
- **Space:** O(1) for English lowercase letters (26 max)  

---

## Patterns
- Hashmap / Frequency Counting  
- Related to:  
  - Group Anagrams  
  - Find All Anagrams in a String  

---

## Notes
- Must compare **counts**, not just sets of characters.  
- Always check length first (fast fail).  
- Follow-up (Unicode): solution with `Counter` works since it handles arbitrary characters.  