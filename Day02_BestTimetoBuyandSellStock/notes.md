# Day 02: Best Time to Buy and Sell Stock

**Problem**  
Link: [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
Category: Array, Dynamic Programming (one-pass optimization)

---

## Approach
- Use a one-pass scan with two trackers:
  - `min_price` → lowest price seen so far (best buy day).  
  - `max_profit` → best profit achievable so far.  
- For each price:
  - Update `min_price = min(min_price, price)`.  
  - Update `max_profit = max(max_profit, price - min_price)`.  
- Return `max_profit`.  

---

## Complexity
- **Time:** O(n) → single pass through the prices.  
- **Space:** O(1) → only two variables.  

---

## Patterns
- Running minimum / prefix optimization.  
- Similar to **Kadane’s Algorithm** (maximum subarray sum).  
- Related problems:  
  - Best Time to Buy and Sell Stock II (multiple transactions).  
  - Maximum Subarray (sliding profit differences).  

---

## Notes
- Must **buy before selling** (not allowed to sell first).  
- If prices always decrease → return 0.  
- Do not return negative profits; stick to 0.  
- Important interview trick: update `max_profit` **after** checking `min_price`.  