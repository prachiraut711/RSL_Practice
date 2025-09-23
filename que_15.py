# 18.count maximum profit in array having stocks prices at different hour

# This means:

# You are given an array of stock prices, where each element represents the price of a stock at a certain time (hour).

# You can buy once and sell once (buy must happen before sell).

# You need to find the maximum profit you can earn.

# If no profit is possible, return 0

def max_profit(arr):
    min_price = float("inf")  #min_price = infinity → ensures that any first price will replace it.
    max_profit = 0
    for i in arr:
        if i < min_price:
            min_price = i
        profit = i - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit

print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))


# Step-by-Step Example 1
# prices = [7, 1, 5, 3, 6, 4]

# Current price (p)	min_price	Action	profit	max_profit
# 7	inf → 7	min_price updated	-	0
# 1	7 → 1	min_price updated	-	0
# 5	1	calculate profit 5-1 = 4	4	4
# 3	1	calculate profit 3-1 = 2	2	4
# 6	1	calculate profit 6-1 = 5	5	5
# 4	1	calculate profit 4-1 = 3	3	5

# ✅ Maximum profit = 5 (buy at 1, sell at 6).

# Step-by-Step Example 2
# prices = [7, 6, 4, 3, 1]

# Current price (p)	min_price	Action	profit	max_profit
# 7	inf → 7	min_price updated	-	0
# 6	7 → 6	min_price updated	-	0
# 4	6 → 4	min_price updated	-	0
# 3	4 → 3	min_price updated	-	0
# 1	3 → 1	min_price updated	-	0

# ✅ Maximum profit = 0 (prices only decrease, no profitable transaction).

# Summary

# Always track the minimum price so far (best buying point).

# Calculate potential profit only if selling at a higher price than min_price.

# Update max_profit whenever a higher profit is found.

# Works in O(n) time with O(1) space.