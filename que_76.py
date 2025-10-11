# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False # here print nahi kel bcz pos is provided by leetcode backend so we just have to write code
# you dont give pos as parametee

# ✅ What is pos in the LeetCode problem?
# pos is just used in the problem description to tell where the cycle starts when testing your code.

# It's not an input to your function — you don’t need it and don’t use it.

# It is only used internally by LeetCode to build the test linked list with a cycle.
# 🔍 So how does your code detect it without pos?
# Your code doesn't care about pos.
# It just checks if a node is visited again by using the fast and slow pointer technique.

# Using Floyd’s Cycle Detection:
# If there is a cycle, fast and slow will eventually meet

# If not, fast will reach None

# It doesn’t need to know where the cycle starts, only whether a cycle exists.




# 🧠 Problem Summary – Detect a Cycle in Linked List
# You are given the head of a linked list. You have to detect if there is a cycle in it.
# A cycle exists if any node’s next pointer eventually points back to a previous node instead of None.
# You need to return True if a cycle exists, else False.
# ✅ Example
# Example 1:
# Input: head = [3, 2, 0, -4], pos = 1

# Visual Representation:
#    3 → 2 → 0 → -4
#         ↑       ↓
#         ←←←←←←←←

# Here, `-4.next` points back to node `2` (index 1), so there's a cycle.

# Output: True
# Example 2:

# Input: head = [1], pos = -1

# There’s only one node, and its `.next` is None. No cycle.

# Output: False
# 🔁 Algorithm: Floyd's Cycle Detection (Tortoise & Hare)
# This is the most efficient and classic way to detect a cycle:

# ✅ Idea:
# Use two pointers:

# slow moves one step at a time

# fast moves two steps at a time

# If there is a cycle:

# fast will eventually meet slow inside the loop (like runners on a circular track).

# If there’s no cycle:

# fast will reach the end (None) before slow.

# 🧮 Algorithm Steps:
# Initialize slow = head and fast = head

# While fast and fast.next are not None:

# Move slow by one (slow = slow.next)

# Move fast by two (fast = fast.next.next)

# If slow == fast, return True (cycle detected)

# If loop ends, return False (no cycle)




#  ✅ Given Input:
# Linked List: [3, 2, 0, -4]
# Cycle: -4 → 2 (i.e., tail connects to node at pos = 1, value 2)

# So the structure is:
# 3 → 2 → 0 → -4
#      ↑       ↓
#      ←←←←←←←←
# Let’s walk through each iteration in detail:

# 🔢 Initialization:

# slow = head  # Node with val = 3
# fast = head  # Node with val = 3
# 🔁 Iteration 1:

# slow = slow.next        # slow moves to 2
# fast = fast.next.next   # fast moves to 0
# slow is now at value 2

# fast is now at value 0

# ✅ slow != fast → continue

# 🔁 Iteration 2:
# slow = slow.next        # slow moves to 0
# fast = fast.next.next   # fast moves to 2
# slow is now at value 0

# fast goes: 0 → -4 → 2 → so fast is now at 2

# ✅ slow != fast → continue

# 🔁 Iteration 3:

# slow = slow.next        # slow moves to -4
# fast = fast.next.next   # fast moves to 0
# slow is at -4

# fast goes: 2 → 0 → -4 → so fast is now at -4

# ✅ slow == fast 🎉
# They meet at -4, so a cycle is detected!

# ✅ Final Answer:
# return True