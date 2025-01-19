# Find the first node of the loop in a linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def firstNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

head = Node(10)
head.next = Node(15)
head.next.next = Node(4)
head.next.next.next = Node(20)
head.next.next.next.next = head

loopNode = firstNode(head)
print(loopNode.data)
