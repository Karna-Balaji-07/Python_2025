# Reverse Linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def reverse(head):
    curr=head
    prev=None
    while curr is not None:
        nextNode=curr.next
        curr.next=prev
        prev=curr
        curr=nextNode
    return prev

