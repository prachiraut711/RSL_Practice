# 67. Dutch national flag

# 🧩 Problem (Dutch National Flag)
# Given an array containing only three types of elements (say 0, 1, 2), sort the array in a single pass so that:
# All 0s come first
# Then all 1s
# Then all 2s
# This is like sorting red, white, and blue balls, hence the name Dutch National Flag.
# Example
# arr = [2, 0, 2, 1, 1, 0]
# After sorting:

# [0, 0, 1, 1, 2, 2]

# 🧠 Algorithm (Three Pointers)

# We use three pointers:

# low → boundary for 0s

# mid → current element we are checking

# high → boundary for 2s

# Steps

# Initialize:

# low = 0, mid = 0, high = len(arr) - 1
# While mid <= high:

# If arr[mid] == 0:

# Swap arr[low] and arr[mid]

# Increment low and mid

# Else if arr[mid] == 1:

# Just increment mid

# Else if arr[mid] == 2:

# Swap arr[mid] and arr[high]

# Decrement high (don’t increment mid yet because swapped value needs checking)

# Stop when mid > high.

# Array is sorted in-place in one pass.

# ✅ Why It Works

# low keeps track of 0s boundary → everything left of low is 0.

# high keeps track of 2s boundary → everything right of high is 2.

# mid scans the array and moves 1s in the middle automatically.

# Time Complexity = O(n)
# Space Complexity = O(1) (in-place)

def dutch_national_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else: #arr[mid] == 2 
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print(dutch_national_flag([2, 0, 2, 1, 1, 0]))