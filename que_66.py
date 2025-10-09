# 38.Write a program for Maximum profit by buying and selling a share at most k times(***)
#188. Best Time to Buy and Sell Stock IV
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

def maxProfit(prices , k):
        if not prices:
            return 0
        
        n = len(prices)
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
        
        dp = [[0] * n for _ in range(k+1)]
        
        for t in range(1, k+1):
            max_diff = -prices[0]
            for i in range(1, n):
                dp[t][i] = max(dp[t][i-1], prices[i] + max_diff)
                max_diff = max(max_diff, dp[t-1][i-1] - prices[i])  # ✅ FIXED
                
        return dp[k][n-1]

print(maxProfit([3,2,6,5,0,3],2))
print(maxProfit([2,4,1], 2))
