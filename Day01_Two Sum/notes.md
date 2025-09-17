# Day 01: Two Sum

**Problem**  
Link: [Two Sum](https://leetcode.com/problems/two-sum/)  
Category: Array, Hashmap

---

## Approach
- Scan once and store previously seen numbers in a dictionary mapping `value -> index`.  
- For each `num`, compute `complement = target - num`.  
- If `complement` is already in the dictionary, return `[seen[complement], i]`.  
- Else insert `seen[num] = i`.  
- Check before insert to avoid pairing with itself when `target == 2 * num`.  

---

## Complexity
- **Time:** O(n)  
- **Space:** O(n)  

---

## Patterns
- Hashing / Complement lookup  
- Similar problems: Two Sum II (sorted, two pointers), 3Sum, Subarray Sum Equals K (uses hashmap over prefix sums)  

---

## Notes
- Be careful to return indices, not values.  
- One valid answer exists; return immediately.  
- Insert after checking complement.  