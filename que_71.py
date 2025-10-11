# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
# Input: head = [1], n = 1
# Output: []
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
# Given a list like:
# Index from front:   1 → 2 → 3 → 4 → 5  
# Index from end:     5 ← 4 ← 3 ← 2 ← 1
# So:
# If n = 2, you remove 4 (the 2nd node from the end).
# If n = 1, you remove 5 (the last node).
# If n = 5, you remove 1 (the first node).

#method 1 by creating dummy
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeNthFromEnd(head, n):
    dummy = Node(0)
    dummy.next = head  #this is dummy head node withvalue 0 and next will be head
    slow = dummy
    fast = dummy

    for _ in range(n + 1):
        fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    
    return dummy.next #which is head

def print_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

    
def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)

    head = removeNthFromEnd(head, 2)
    print(print_list(head))

if __name__ == "__main__":
    main()

print("___")
#method2 by not using dummy but use edge case
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeNthFromEnd(head, n):
    fast = head
    slow = head

    for _ in range(n):
        fast = fast.next

    if fast is None:
        return head.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    
    return head

def print_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

    
def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)

    head = removeNthFromEnd(head, 2)
    print(print_list(head))

if __name__ == "__main__":
    main()


