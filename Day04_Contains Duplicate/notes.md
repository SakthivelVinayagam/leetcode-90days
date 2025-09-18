# Day 04: Contains Duplicate  

**Problem**  
Link: https://leetcode.com/problems/contains-duplicate/  
Category: Array / Hashset  

---

## Approach  
- Use a HashSet to keep track of numbers seen so far.  
- Iterate through the array:  
  - If the current number is already in the set → return `True`.  
  - Otherwise, add it to the set.  
- If no duplicates are found after processing all numbers → return `False`.  

---

## Complexity  
- **Time:** O(n) (each element checked once).  
- **Space:** O(n) (set may store all unique elements).  

---

## Patterns  
- Hashing / Duplicate detection  
- Related to:  
  - Contains Duplicate II (check distance between duplicates)  
  - Contains Duplicate III (check with value difference constraints)  

---

## Notes  
- Edge cases:  
  - Empty array → return `False`.  
  - Single element → return `False`.  
- Use early exit once a duplicate is found (saves time).  
- Sorting + adjacent check also works but is slower (O(n log n)).  