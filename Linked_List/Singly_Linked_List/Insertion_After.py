# Insertion after a given node in the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insertion(head, index, element):
    temp = head
    while temp is not None:
        if temp.data == index:
            break
        temp = temp.next
    if temp is None:
        print("Node not found")
        return head
    new_node = Node(element)
    new_node.next = temp.next
    temp.next = new_node
    return head

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data,end=" ")
        temp = temp.next
    print()

head = Node(20)
head.next = Node(30)
head.next.next = Node(40)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
print("Before Insertion : ")
printLL(head)
print("After Insertion : ")
head = insertion(head, 30,35)
printLL(head)