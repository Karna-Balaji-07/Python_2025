# Check if the linked list is circular linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def circular(head):
    slow = head
    fast = head.next
    while fast  and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False