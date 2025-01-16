# Removal of the last node of the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def removal(head):
    if head is None:
        return None
    if head.next is None:
        return None
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original list: ")
print_list(head)
    # Removing the last node
head = removal(head)

print("List after removing the last node: ")
print_list(head)