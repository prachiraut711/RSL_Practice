# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeTwoLists(l1, l2):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    if l1:
        curr.next = l1
    elif l2:
        curr.next = l2
    
    return dummy.next  # jar nusta dummy kel tar 0-1-1-2-3-4-4  zero pn ala asta mahnun dummy.next kel




