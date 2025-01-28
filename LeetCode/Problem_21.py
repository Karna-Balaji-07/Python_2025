# Merge two sorted linked list

class Node:
    def  __init__(self,data):
        self.data=data
        self.next=None

def merge(head1,head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    head=Node()
    curr=head
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            curr.next=head1
            head1 = head1.next
        else:
            curr.next=head2
            head2=head2.next
        curr=curr.next
    if head1 is not None:
        curr.next=head1
    else:
        curr.next=head2
    return head.next
