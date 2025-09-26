# 287. Find the Duplicate Number
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3


# Think of the array as a linked list:

# Each index i points to nums[i].

# Because there is a duplicate, eventually the pointers will form a cycle.

# Using Floyd’s Cycle Detection algorithm, we can detect the cycle and find the starting point, which is the duplicate number.
 
#here wantO(n) time complexity, O(1) space complexity and arry should not modified
def duplicateNum(nums):
    #Phase 1: Detect the cycle
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    #Find the entry point (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

print(duplicateNum([1,3,4,2,2]))
print(duplicateNum([3,1,3,4,2]))
print(duplicateNum([3,3,3,3,3]))





# Step-by-step explanation
# Phase 1: Detect the cycle
# slow = nums[0]
# fast = nums[0]
# while True:
#     slow = nums[slow]
#     fast = nums[nums[fast]]
#     if slow == fast:
#         break


# We initialize two pointers: slow and fast at the start (nums[0]).

# We move slow one step at a time: slow = nums[slow].

# We move fast two steps at a time: fast = nums[nums[fast]].

# If there is a duplicate, the “linked list” will have a cycle, and eventually slow and fast will meet inside the cycle.

# Why this works:

# Imagine the array as a chain of numbers: each number points to another index.

# Since one number is repeated, at least two indices point to the same number → forming a loop.

# Using the Tortoise and Hare method, the two pointers will eventually meet inside this loop.

# Phase 2: Find the entry point (duplicate number)
# slow = nums[0]
# while slow != fast:
#     slow = nums[slow]
#     fast = nums[fast]


# After detecting the cycle, we reset slow to the start (nums[0]), while fast stays at the meeting point.

# Move both slow and fast one step at a time.

# The point where they meet again is the start of the cycle, which corresponds to the duplicate number.

# Why this works:

# Let the distance from start to the cycle entry be x, and the distance from cycle entry to meeting point be y.

# Let the cycle length be C.

# When they meet, fast has traveled twice as far as slow: 2*(x+y) = x+y + k*C → simplifying gives x = k*C - y.

# Moving slow from start and fast from meeting point one step at a time guarantees they meet at the entry of the cycle → duplicate number.

# Return the result
# return slow


# At this point, slow (or fast) is pointing to the duplicate number.

# Example walkthrough
# Input: [1,3,4,2,2]

# Phase 1 (Cycle detection)

# Step	slow	fast
# Start	1	1
# 1	nums[1]=3	nums[nums[1]]=nums[3]=2
# 2	nums[3]=2	nums[nums[2]]=nums[4]=2

# slow == fast == 2 → meeting point detected.

# Phase 2 (Find entry point)

# Step	slow	fast
# Reset slow = nums[0] = 1	1	2
# Move both 1 step	nums[1]=3	nums[2]=4
# Move both 1 step	nums[3]=2	nums[4]=2

# They meet at 2 → duplicate number found.

# ✅ Key Points

# No modification: We only traverse the array using indices.

# O(1) extra space: Only two pointers are used.

# Time complexity: O(n) → linear traversal to detect and locate cycle.

# Why it works: The array acts like a linked list with a cycle due to the duplicate number.