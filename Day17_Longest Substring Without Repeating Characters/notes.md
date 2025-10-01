# Day 17: Longest Substring Without Repeating Characters

**Problem**  
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/  
Category: String / Sliding Window / HashMap

---

## Approach
- Use a **sliding window** with two pointers (`left` and `right`) and a hashmap `last_seen` that stores the last index where each character appeared.
- For each character `s[right]`:
  - If it has been seen inside the current window (`last_seen[ch] >= left`), move `left` to `last_seen[ch] + 1` to remove the duplicate from the window.
  - Update `last_seen[ch] = right`.
  - Update the best length as `right - left + 1`.
- This ensures each character index is processed at most twice (enter/adjust), giving linear time.

---

## Complexity
- **Time:** O(n) — each index moves `left` and `right` at most forward once  
- **Space:** O(min(n, charset)) — hashmap of last-seen positions

---

## Patterns
- Sliding Window  
- HashMap to track constraints inside the window  
- “Expand right, shrink left when constraint violated” idiom

---

## Notes
- Works with any ASCII/Unicode characters present in the string (digits, spaces, symbols).  
- Key correctness point: when a duplicate is found, advance `left` only **forward** (`max(left, last_seen[ch] + 1)` pattern) to keep the window valid.  
- Related problems:  
  - Longest Repeating Character Replacement  
  - Minimum Window Substring  
  - Longest Substring with At Most K Distinct Characters