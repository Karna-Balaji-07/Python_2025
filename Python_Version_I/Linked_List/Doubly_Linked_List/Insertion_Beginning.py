# Insertion at the front of the double linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def insertion(head,data):
    new_node = Node(data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data,end=" <-> ")
        temp = temp.next
    print("None")

head = Node(2)
head.next = Node(3)
head.next.prev = head
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.prev = head.next
head.next.next.next.prev = head.next.next
printLL(head)

head = insertion(head,1)
printLL(head)