# 58. Count of elements which are power of 2 in array.

# We need to count how many numbers in a given array are powers of 2.
# (A number is a power of 2 if it can be written as 2^k for some integer 𝑘 ≥ 0. Examples: 1, 2, 4, 8, 16, 32 …).

def count_powers_of_two(arr):
    count = 0
    for i in arr:
        if i > 0 and (i & i - 1) == 0:
            count += 1
    return count

print(count_powers_of_two([1, 2, 3, 4, 5, 8, 10, 16, 18, 32]))

#jar and operator karun 0 al ans then its power of 2 in and operaor 1  1 = 1, 0 0 = 0, 1 0 = 0, 0, 1 = 0

# Step 1: Recall the rule

# A number n is a power of 2 if:

# n > 0

# n & (n - 1) == 0

# 👉 Why?

# Powers of 2 in binary have exactly one bit set:

# 1 → 0001

# 2 → 0010

# 4 → 0100

# 8 → 1000

# If you subtract 1, all bits below that single 1 flip:

# 8 (1000) → 7 (0111)

# 4 (0100) → 3 (0011)

# So n & (n-1) becomes 0.

# Step 2: Walk through each element

# Array: [1, 2, 3, 4, 5, 8, 10, 16, 18, 32]

# 1 → binary 0001
# (1 & 0) == 0 ✅ → Power of 2

# 2 → binary 0010
# (2 & 1) = (10 & 01) = 0 ✅

# 3 → binary 0011
# (3 & 2) = (11 & 10) = 10 (not 0) ❌

# 4 → binary 0100
# (4 & 3) = (100 & 011) = 0 ✅

# 5 → binary 0101
# (5 & 4) = (101 & 100) = 100 (not 0) ❌

# 8 → binary 1000
# (8 & 7) = (1000 & 0111) = 0 ✅

# 10 → binary 1010
# (10 & 9) = (1010 & 1001) = 1000 (not 0) ❌

# 16 → binary 10000
# (16 & 15) = (10000 & 01111) = 0 ✅

# 18 → binary 10010
# (18 & 17) = (10010 & 10001) = 10000 (not 0) ❌

# 32 → binary 100000
# (32 & 31) = (100000 & 011111) = 0 ✅

# Step 3: Count ✅ marks

# Valid powers of 2 are:
# 1, 2, 4, 8, 16, 32

# 👉 Count = 6