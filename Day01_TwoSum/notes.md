# Day 1: Two Sum

**Problem:** [Two Sum](https://leetcode.com/problems/two-sum/)  
**Category:** Array / Hashmap  

## 🧠 Approach
- Use a hashmap to store values and their indices.  
- For each number, check if `target - num` is already in the hashmap.  
- Complexity: **O(n)** time, **O(n)** space.  

## 📝 Patterns
- **Hashmap lookup** → efficient for complement pairs.  
- Reappears in subarray sums, anagrams, frequency problems.  

## 🚩 Notes
- Brute force = O(n²). Avoid.  
- Handle duplicates carefully (store indices properly).  
