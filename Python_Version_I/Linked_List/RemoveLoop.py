# Remove Loop in a linked list

class Node:
    def __init__(self,data):
        self.next=None
        self.data = data

def remove(head):
    if head is None and head.next is None:
        return 
    slow = head
    fast=head
    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow=head
        while slow != fast:
            slow=slow.next
            fast=fast.next
        while fast.next !=slow:
            slow=slow.next
            fast=fast.next
        fast.next=None 
    return head

