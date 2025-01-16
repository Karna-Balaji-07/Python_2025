# Traversal in a single linked list

# Definition of node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseList(head):
    temp = head
    while temp is not None:
        print(temp.data,end="->")
        temp = temp.next
    print()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
traverseList(head)