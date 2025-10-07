# 322. Coin Change
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 
# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

# LeetCode’s general problem allows arbitrary coin denominations and amount, so it generally requires dynamic programming (DP)
# or BFS / memoization approaches, with time complexity typically O(\text{amount} \times \text{number_of_coins}) 

def coin_change(coins, amount):
    # dp[i] = minimum coins needed to make exactly amount i
    # initialize dp with a large sentinel value
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # zero coins needed to make amount 0

    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)
    
    
    if dp[amount] != float('inf'):
        return dp[amount]
    else:
        return -1

print(coin_change([1,2,5], 11))
print(coin_change([2], 3))
print(coin_change([1], 0))
    
# Line-by-line meaning

# dp = [float('inf')] * (amount + 1)
# Create an array sized amount+1 filled with a very large value (inf) meaning “not possible yet”.

# dp[0] = 0
# Base case: zero coins needed to make amount 0.

# for coin in coins:
# For each coin denomination, try to use that coin to improve the dp answers.

# for a in range(coin, amount + 1):
# For each target amount a that is at least the coin value, consider using this coin.

# dp[a] = min(dp[a], dp[a - coin] + 1)
# Two choices for dp[a]:

# Keep current best dp[a] (don’t use this coin).

# Use this coin once plus the best way to make a - coin (dp[a-coin] + 1).
# Choose the smaller of these.

# return dp[amount] if dp[amount] != float('inf') else -1
# If dp[amount] stayed inf → amount is impossible → return -1. Otherwise return minimum coins.

# Why this works (intuition)

# dp[a] is computed from smaller subproblems dp[a-coin]. Because we iterate amounts increasing from coin to amount, when we compute dp[a] using dp[a-coin], that dp[a-coin] already stores the minimal coins (possibly using the same coin multiple times). This is the standard unbounded knapsack / coin-change DP.

# Dry run example: coins = [1,2,5], amount = 11

# Initialize dp (indexes 0..11):

# dp = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

# Process coin = 1

# For a from 1 to 11: dp[a] = min(dp[a], dp[a-1] + 1) → using coin 1 we can make every a with a coins of 1:

# dp after coin=1:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Process coin = 2

# For a from 2 to 11:

# a=2: dp[2] = min(2, dp[0]+1=1) => 1

# a=3: dp[3] = min(3, dp[1]+1=2) => 2

# a=4: dp[4] = min(4, dp[2]+1=1+1=2) => 2

# a=5: dp[5] = min(5, dp[3]+1=2+1=3) => 3

# a=6: dp[6] = min(6, dp[4]+1=2+1=3) => 3

# a=7: dp[7] = min(7, dp[5]+1=3+1=4) => 4

# a=8: dp[8] = min(8, dp[6]+1=3+1=4) => 4

# a=9: dp[9] = min(9, dp[7]+1=4+1=5) => 5

# a=10: dp[10] = min(10, dp[8]+1=4+1=5) => 5

# a=11: dp[11] = min(11, dp[9]+1=5+1=6) => 6

# dp after coin=2:
# [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

# Process coin = 5

# For a from 5 to 11:

# a=5: dp[5] = min(3, dp[0]+1 = 1) => 1 (use one 5-coin)

# a=6: dp[6] = min(3, dp[1]+1 = 1+1 = 2) => 2

# a=7: dp[7] = min(4, dp[2]+1 = 1+1 = 2) => 2

# a=8: dp[8] = min(4, dp[3]+1 = 2+1 = 3) => 3

# a=9: dp[9] = min(5, dp[4]+1 = 2+1 = 3) => 3

# a=10: dp[10] = min(5, dp[5]+1 = 1+1 = 2) => 2 (two 5-coins)

# a=11: dp[11] = min(6, dp[6]+1 = 2+1 = 3) => 3 (two 5s + one 1)

# dp after coin=5 (final):
# [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]


# So dp[11] = 3 → minimum 3 coins (for example 5 + 5 + 1).

# Complexity

# Time: O(len(coins) * amount) — nested loops.

# Space: O(amount) for the dp array.
