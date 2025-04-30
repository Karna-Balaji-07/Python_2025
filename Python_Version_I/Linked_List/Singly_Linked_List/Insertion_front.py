# Insertion at the beginning/front of the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert_at_front(head, data):
    new_node = Node(data) # creating a new node 
    new_node.next = head # Pointing the node to the current head of the linked list
    return new_node # returning the new node as the head of the linked list

def printLL(head):
    curr = head
    while curr is not None:
        print(curr.data,end=" ")
        curr = curr.next
    print()

head = Node(12)
head.next = Node(23)
head.next.next = Node(31)
head.next.next.next = Node(34)
print("Before Insertion : ")
printLL(head)
head = insert_at_front(head,50)
print("After Insertion : ")
printLL(head)

