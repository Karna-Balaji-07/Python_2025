# Intersection of two linked list

class Node:
    def  __init__(self,data):
        self.next = None
        self.data =  data 

def intersection(head1,head2):
    if head1 is None or head2 is None:
        return None
    temp,curr = head1,head2
    while temp != curr:
        if curr is not None:
            curr=curr.next                                               
        else:
            curr=head1
        if temp is not None:
            temp=temp.next
        else:
            temp = head2
    return temp