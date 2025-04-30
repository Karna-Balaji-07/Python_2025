# Removal of the first node of the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def removal(head):
    if head is None:
        return None
    temp = head
    head = head.next
    del temp
    return head

def print_list(curr):
    while curr:
        print(curr.data, end=" ")
        curr = curr.next

head = Node(3)
head.next = Node(12)
head.next.next = Node(15)
head.next.next.next = Node(18)
head = removal(head)
print_list(head)