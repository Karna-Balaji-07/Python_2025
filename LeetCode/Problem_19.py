# Remove nth node from the end of the linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def counts(head):
    count=0
    curr=head
    while curr is not None:
        count+=1
        curr=curr.next
    return count

def remove(head,n):
    lengths=counts(head)
    if n > lengths or n <=0:
        return head
    if n==lengths:
        return head.next
    index=lengths-n
    curr=head

    for i in range(index-1):
        curr=curr.next
    curr.next=curr.next.next
    return head

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print_list(head)
head=remove(head,2)
print_list(head)
