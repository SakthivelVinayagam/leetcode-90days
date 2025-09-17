# Day 02: Best Time to Buy and Sell Stock

def maxProfit(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


#  Test cases
if __name__ == "__main__":
    # Example 1
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
    # Explanation: Buy at 1, Sell at 6 → Profit = 5

    # Example 2
    print(maxProfit([7, 6, 4, 3, 1]))  # Expected: 0
    # Explanation: No profitable transaction

    # Edge case: Only one price (can't sell)
    print(maxProfit([5]))  # Expected: 0

    # Increasing prices (best profit = last - first)
    print(maxProfit([1, 2, 3, 4, 5]))  # Expected: 4

    # Decreasing then increasing
    print(maxProfit([9, 7, 2, 3, 8, 1, 9]))  # Expected: 8
    # Buy at 1, sell at 9 → Profit = 8