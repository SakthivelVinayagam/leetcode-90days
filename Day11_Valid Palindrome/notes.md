# Day 11: Valid Palindrome

**Problem**  
Link: https://leetcode.com/problems/valid-palindrome/  
Category: String / Two Pointers  

---

## Approach 
- Normalize string: convert to lowercase, strip non-alphanumeric characters.  
- Compare characters from both ends moving inward.  
- Or directly compare `filtered == filtered[::-1]` (Pythonic).  

---

## Complexity
- **Time:** O(n) (single pass + reverse)  
- **Space:** O(n) for cleaned string; O(1) if two-pointer in-place  

---

## Patterns
- Two Pointers  
- String normalization (cleaning)  
- Palindrome check  

---

## Notes
- Empty string → valid palindrome.  
- Must ignore cases and symbols.  
- Regex simplifies filtering.  
- Related problems:  
  - Palindrome Linked List  
  - Valid Palindrome II (remove one char allowed)  