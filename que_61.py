#65. Minimum coins required of 2 & 5 to get N sum value O(1)

# You have coins of 2 and 5 denominations.
# You need to make a total sum of N.
# Find the minimum number of coins required to get that sum.
# You must do it in O(1) time — i.e., without using loops.

# Logic / Algorithm

# Let’s think in a greedy way 👇

# Always use maximum 5-value coins first, because they reduce the count faster.

# If the remaining amount cannot be made using 2-value coins (i.e., remainder is 1 or 3),
# then reduce one 5-coin and try again.

# Algorithm:

# 1️⃣ Let five = N // 5 (maximum 5-coins possible)
# 2️⃣ Let rem = N % 5 (remaining amount)

# Now check:

# If rem % 2 == 0 → directly possible using 2-value coins
# ✅ → ans = five + rem // 2

# Else → reduce one 5-coin (five -= 1), and check again
# 🔁 → new rem = N - 5 * five
# If that’s even, compute total again.

# If not possible at all (like N = 1 or 3), return -1

# 🧮 Example

# 👉 N = 18

# five = 18 // 5 = 3

# rem = 18 % 5 = 3 → not even

# Reduce one 5-coin → five = 2, new rem = 18 - 5*2 = 8
# ✅ now even

# twos = 8 // 2 = 4

# ✅ Total = 2 + 4 = 6 coins

def min_coins(N):
    if N in [1, 3]:   # Not possible to make
        return -1
    
    five = N // 5
    rem = N % 5
    if rem % 2 == 0:
        return five + rem // 2
    else:
        five -= 1
        rem = N - (5 * five)
        return five + rem  // 2

# Example
print(min_coins(18))  # Output: 6
print(min_coins(11))  # Output: 3 (5 + 2 + 2)
print(min_coins(7))   # Output: 2 (5 + 2)
print(min_coins(3))   # Output: -1 (not possible)

