# 55.Find the max distance between indexes of duplicate values from an array.
# We are asked:
# 👉 Find the maximum distance between indexes of duplicate values in an array.
# That means:
# Look at numbers that repeat (duplicates).
# Take the first position and the last position of that number.
# Find the difference in their indexes (last_index - first_index).
# Among all numbers, take the maximum such distance.
# 📌 Example 1
# arr = [1, 2, 3, 1, 2, 1]
# Step 1: Find duplicates and their positions.
# 1 occurs at indices [0, 3, 5]
# distance between first (0) and last (5) = 5
# 2 occurs at indices [1, 4]
# distance = 4 - 1 = 3
# 3 occurs at index [2] → no duplicate, ignore
# Step 2: Compare distances
# For 1 → 5
# For 2 → 3
# ✅ Max distance = 5 (between index 0 and 5, both are 1).

#) Optimal (one-pass, hash map) — recommended

# Create a dictionary first_index mapping value → its first index seen.
# Iterate i from 0 to n-1:
# If arr[i] not in first_index, set first_index[arr[i]] = i.
# Else compute dist = i - first_index[arr[i]]. If dist > max_dist, update max_dist and store the pair (first_index[arr[i]], i).
# Return max_dist (and optionally the index pair).
# Time: O(n), Space: O(k) (k = number of distinct values).

def max_duplicate_distance(arr):
    first_index = {}
    max_dist = -1   #By initializing max_dist = -1, we can detect array has no duplicates, then there is no valid distance to return and we return -1 to mean "no duplicate found."
    max_pair = (-1, -1)

    for i, val in enumerate(arr): # enumerate map index with value example here {0:1, 1:2, 3:3...}
        if val in first_index:
            dist = i - first_index[val]
            if dist > max_dist:
                max_dist = dist
                max_pair = (first_index[val], i)
        else:
            first_index[val] = i
    
    return max_dist, max_pair

print(max_duplicate_distance([1, 2, 3, 1, 2, 1]))
print(max_duplicate_distance([7,8,9]))



# 🔹 Brute force code (Python)  time: o(n^2) not recommended
print("__________________")
def max_duplicate_distance_bruteforce(arr):
    n = len(arr)
    max_dist = -1
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                dist = j - i
                if dist > max_dist:
                    max_dist = dist
    return max_dist

# Example
arr = [1, 2, 3, 1, 2, 1]
print(max_duplicate_distance_bruteforce(arr))  # Output: 5
