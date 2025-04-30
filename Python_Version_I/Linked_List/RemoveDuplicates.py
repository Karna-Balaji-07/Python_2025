# Remove duplicates from sorted linkedlist

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def duplicates(head):
    curr = head
    while curr is not None and curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data,end=" ")
        temp = temp.next
    print()

head = Node(20)
head.next = Node(30)
head.next.next = Node(30)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(60)
head = duplicates(head)
printLL(head)
