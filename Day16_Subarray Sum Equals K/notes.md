# Day 16: Subarray Sum Equals K

**Problem**  
Link: https://leetcode.com/problems/subarray-sum-equals-k/  
Category: Array / Hashmap / Prefix Sum

---

## Approach
- Use **prefix sums** with a **hashmap** to count how many times each prefix sum has appeared.
- Let `prefix[i] = sum(nums[0..i])`. For each index `i`, we want the number of `j < i` such that:
  - `prefix[i] - prefix[j] = k`  ⇒  `prefix[j] = prefix[i] - k`.
- Maintain a hashmap `count` where `count[s]` = how many prefixes with sum `s` have been seen so far.
- Initialize `count[0] = 1` so subarrays starting at index 0 can be counted.

---

## Complexity
- **Time:** O(n) — single pass over the array with O(1) average hashmap lookups  
- **Space:** O(n) — hashmap of prefix sums

---

## Patterns
- Prefix Sum + Hashmap counting  
- Subarray sum with positive/negative numbers (works with negatives; two-pointers would not)

---

## Notes
- Critical init: `count[0] = 1` (subarrays starting at the beginning).
- Works with negatives and zeros (unlike sliding window).
- Each step:
  1. Update `prefix += nums[i]`
  2. Add `count[prefix - k]` to answer
  3. Increment `count[prefix]`
- Related:
  - 974. Subarray Sums Divisible by K (prefix mod counting)
  - 437. Path Sum III (tree version of prefix sums)
  - 523. Continuous Subarray Sum (prefix mod)