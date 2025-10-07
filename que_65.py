
# Code
# Testcase
# Testcase
# Test Result
# Leet
# 123. Best Time to Buy and Sell Stock III
# Hard
# Topics
# premium lock icon
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 105

# We track four states:

# first_buy: Max profit after first buy (negative because you spent money)

# first_sell: Max profit after first sell

# second_buy: Max profit after second buy

# second_sell: Max profit after second sell

# How it works

# For each price in prices:

# first_buy → maximize profit if you buy first stock

# first_buy = max(first_buy, -price)


# (spending money, so negative)

# first_sell → maximize profit after selling first stock

# first_sell = max(first_sell, first_buy + price)


# second_buy → maximize profit if you buy second stock after first sell

# second_buy = max(second_buy, first_sell - price)


# second_sell → maximize profit after selling second stock

# second_sell = max(second_sell, second_buy + price)


# At the end, second_sell has the maximum profit with at most 2 transactions.
def max_profit(prices):
    first_buy = float("-inf") #Max profit after first buy (negative because you spent money)
    first_sell = 0  #Max profit after first sell
    second_buy = float("-inf")  #Max profit after second buy
    second_sell = 0  #Max profit after second sell

    for price in prices:
        first_buy = max(first_buy, -price)  #(spending money, so negative)
        first_sell = max(first_sell, first_buy + price)
        second_buy = max(second_buy, first_sell - price)
        second_sell = max(second_sell, second_buy + price)
    
    return second_sell

print(max_profit([3,3,5,0,0,3,1,4]))
print(max_profit([1,2,3,4,5]))
print(max_profit([7,6,4,3,1]))