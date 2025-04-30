# Insertion before the given node in a linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def insertion(head, index, data):
    if head is None:
        return None
    if head.data == index:
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    prev = None
    curr = head
    while curr is not None and curr.data != index:
        prev = curr
        curr = curr.next
    
    if curr is not None:
        new_node = Node(data)
        prev.next = new_node
        new_node.next = prev.next
    
    return head

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data,end=" ")
        temp = temp.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
printLL(head)
head = insertion(head, 3,9)
printLL(head)