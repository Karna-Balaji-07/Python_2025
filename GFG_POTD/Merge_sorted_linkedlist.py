# merge two sorted linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def merge(head1,head2):
    temp = Node(-1)
    curr = temp
    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next= head2
            head2 = head2.next
        curr = curr.next
    if head1 is not None:
        curr.next=head1
    else:
        curr.next = head2
    return temp.next

def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

head1 = Node(5)
head1.next = Node(10)
head1.next.next = Node(15)
head1.next.next.next = Node(40)

    # Second linked list: 2 -> 3 -> 20
head2 = Node(2)
head2.next = Node(3)
head2.next.next = Node(20)
res = merge(head1, head2)
printList(res)  