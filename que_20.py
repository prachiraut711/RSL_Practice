# 21.print maximum count of 1's chain in array of numbers containing 0 and 1

# 🔹 Meaning:

# You are given an array (or list) that only contains 0s and 1s.
# You need to find the longest consecutive sequence (chain) of 1s in that array.

# 📌 Example 1
# Input:  [1, 1, 0, 1, 1, 1, 0, 1]


# First chain: 1, 1 → length = 2

# Second chain: 1, 1, 1 → length = 3

# Third chain: 1 → length = 1

# 👉 Maximum = 3

# Output: 3

# 📌 Example 2
# Input: [0, 0, 0, 0]


# There are no 1s at all.
# 👉 Maximum chain length = 0

# 📌 Example 3
# Input: [1, 1, 1, 1, 1]


# Only one chain of all 1s.
# 👉 Maximum = 5

# 📌 Algorithm (Step by Step)

# Initialize two counters:

# count = 0 → keeps track of current chain of 1s.

# max_count = 0 → stores the maximum chain length seen so far.

# Traverse the array element by element:

# If the element is 1:

# Increase count by 1.

# Update max_count = max(max_count, count).

# If the element is 0:

# Reset count = 0 (because chain breaks).

# After traversal, max_count will hold the answer.


#method 1
def max_count_chain(arr):
    count = 0
    max_count = 0
    for i in arr:
        if i == 1:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    return max_count

print(max_count_chain([1, 1, 0, 1, 1, 1, 0, 1]))
print(max_count_chain([1,1,1,1,1]))
print(max_count_chain([0, 0, 0, 0]))

#method 2
def max_count_chain(arr):
    count = 0
    max_count = 0
    for i in arr:
        if i == 1:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0
    return max_count

print(max_count_chain([1, 1, 0, 1, 1, 1, 0, 1]))
print(max_count_chain([1,1,1,1,1]))
print(max_count_chain([0, 0, 0, 0]))