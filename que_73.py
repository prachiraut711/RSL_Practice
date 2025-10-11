# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
# Example 2:
# Input: head = [1,2]
# Output: false

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPalindrome(head):

    def reverseList(head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def copiedList(head):
        if not head:  #imp test case
            return None
        
        new_head = Node(head.data)
        old_node = head.next
        new_node = new_head
        while old_node:
            new_node.next = Node(old_node.data)
            old_node = old_node.next
            new_node = new_node.next

        return new_head    #new_head return kel
    
    def isEqual(l1, l2):
        while l1 and l2:
            if l1.data != l2.data:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
    
    copied_List_of_original = copiedList(head)
    reversed_list = reverseList(copied_List_of_original)
    return isEqual(head, reversed_list)  #head bcz original list barobar reversed list compare karychiye

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    
    print(isPalindrome(head))   #isPalindrome is defined inside your Solution 

if __name__ == "__main__":
    main()


