# Insertion at the end of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion(head, data):
    new_node = Node(data)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node
    return head

def print_list(node):

    while node:
        print(node.data, end=" ")
        node = node.next
head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)
head = insertion(head, 1)
print_list(head)