# 122. Best Time to Buy and Sell Stock II
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold than one share of the stock.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 
# Problem: Best Time to Buy and Sell Stock II

# You are given:

# An array prices, where prices[i] = price of a stock on day i.

# You can buy and sell as many times as you want.

# You cannot hold more than one stock at a time (you must sell before you can buy again).

# Goal:
# Maximize your total profit.

# Key Points

# You can buy and sell multiple times.

# You must sell before buying again.

# Profit is sell price - buy price.

# If prices are decreasing, you cannot make profit → profit = 0.

# Example 1
# prices = [7, 1, 5, 3, 6, 4]


# Step by step:

# Day 0 → 1: prices drop 7 → 1 → don’t buy yet

# Day 1 → 2: prices rise 1 → 5 → buy at 1, sell at 5 → profit = 4

# Day 2 → 3: prices drop 5 → 3 → don’t buy

# Day 3 → 4: prices rise 3 → 6 → buy at 3, sell at 6 → profit = 3

# Total profit = 4 + 3 = 7

# Example 2
# prices = [1, 2, 3, 4, 5]


# Prices rise every day → you can treat it as one long transaction: buy at 1, sell at 5 → profit = 4

# Or sum all consecutive rises: (2-1)+(3-2)+(4-3)+(5-4) = 4 → same answer

# Example 3
# prices = [7, 6, 4, 3, 1]


# Prices always decrease → no transaction possible → profit = 0

# Intuition

# Every time the price goes up from one day to the next, you can capture that profit.

# You can think of it as buying at every local minimum and selling at the next local maximum.

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 4, 3, 1]))