# Floyds Cycle Finding algorithm

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def cycle(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

head = Node(1)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = head.next

result = cycle(head)
print(result)