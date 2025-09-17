# Day 02: Best Time to Buy and Sell Stock
# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Category: Array / One Pass

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)  # Best buy so far
            max_profit = max(max_profit, price - min_price)  # Profit if sold today
        return max_profit

# ------------------------
# Test Cases
# ------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))   # 5
    print(sol.maxProfit([7, 6, 4, 3, 1]))      # 0
    print(sol.maxProfit([5]))                  # 0
    print(sol.maxProfit([1, 2, 3, 4, 5]))      # 4
    print(sol.maxProfit([9, 7, 2, 3, 8, 1, 9])) # 8
