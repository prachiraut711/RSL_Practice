# Given an integer array, find a pair with the given sum in it.

# 🧩 Problem
# Given an integer array arr and a target sum target, find any pair (a, b) in the array such that a + b = target.
# Example
# arr = [1, 4, 5, 3, 2]
# target = 7
# Pairs with sum 7: (4, 3) or (5, 2)
# Output: any one pair → e.g., (4, 3)

# 🧠 Algorithm (Using Map / HashSet)

# Create an empty set to store numbers seen so far.

# Iterate through the array:

# Let current element = num.

# Compute needed = target - num.

# If needed is in the set → we found a pair (num, needed)

# Else → add num to the set.

# If no pair is found → return None.


def find_pair_with_sum(arr, target):
    seen = set()
    pairs = []
    for num in arr:
        needed = target - num
        if needed in seen:
            pairs.append((num, needed))
        else:
            seen.add(num)
    return pairs

print(find_pair_with_sum([1,4,5,3,2], 7))


# 🔹 Why needed = target - num?

# We are trying to find two numbers that sum up to the target:
# a+b=target
# Suppose we are currently at number num (say a = num).
# Then the other number b that would complete the pair is:
# b = target−a
# ✅ That’s exactly what we call needed in the code:
# needed = target - num
# If needed is already in the set of numbers we have seen, it means we found a pair (needed, num) that sums to target.
# Otherwise, we add num to the set and continue.
# 🔹 Example
# arr = [1, 4, 5, 3, 2]
# target = 7
# Step by step:
# Current num = 1 → needed = 7 - 1 = 6 → 6 not in set → add 1
# Set = {1}

# Current num = 4 → needed = 7 - 4 = 3 → 3 not in set → add 4
# Set = {1, 4}

# Current num = 5 → needed = 7 - 5 = 2 → 2 not in set → add 5
# Set = {1, 4, 5}

# Current num = 3 → needed = 7 - 3 = 4 → 4 is in set!
# ✅ Found a pair → (4, 3)

# 🔹 Key Idea

# needed = target - num is mathematical logic to figure out what number would complete the pair.
# Without this, you’d have to check every other number in the array (O(n²) brute force), which is slower.
