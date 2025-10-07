# 47.Minimum Profit/Buy and sell stocks(121. Best Time to Buy and Sell Stock)
# You are given an array prices where prices[i] is the price of a stock on day i.
# You can buy once and sell once later.

# Find the maximum profit you can achieve.
# If you cannot make any profit, return 0.

# 🧠 Example:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5


# 👉 Explanation:

# Buy at price = 1

# Sell at price = 6

# Profit = 6 - 1 = 5

# ⚙️ Algorithm (Greedy – O(N) time, O(1) space)

# Initialize:

# min_price = ∞ → smallest price seen so far

# max_profit = 0

# Loop through each price:

# If current price < min_price → update min_price

# Else → calculate profit = current_price - min_price

# If profit > max_profit → update max_profit

# Return max_profit

def maxProfit(prices):
    min_price = float('inf')
    max_price = 0

    for i in prices:
        if i < min_price:
            min_price = i

        profit = i - min_price

        if profit > max_price:
            max_price = profit

    return max_price

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7,6,4,3,1]))