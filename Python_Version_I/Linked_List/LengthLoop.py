# Length of the loop


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def count(head):
    counts = 0
    curr = head
    while curr.next is not head:
        counts += 1
        curr = curr.next
    return counts


def length(head,index):
    
    slow = head
    fast = head
    while fast and fast.next and slow:
        slow=slow.next
        fast = fast.next.next
        if slow == fast:
            return count(slow)
    return 0






