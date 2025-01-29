# Reorder linked list

class Node:
    def __init__(self,data):
        self.next=None
        self.data=data

def reorder(head):
    if not head or not head.next:
        return head
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    prev=None
    curr=head
    while curr is not None:
        newNode=curr.next
        curr.next=prev
        prev=curr
        curr=newNode
    
    first,second=head,prev
    while second.next:
        temp1=first.next
        temp2=second.next
        first.next=second
        second.next=temp1
        first=temp1
        second=temp2

    return head