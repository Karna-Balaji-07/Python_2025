# Insertion at specific position in the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insertion(head, pos, data):
    if pos < 1:
        return head
    if pos == 1:   # if position is at the beginning of the linked list
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    curr = head
    for _ in range(1,pos-1):
        if curr==None:
            break
        curr = curr.next

    if curr is None:
        return head
    
    new_node = Node(data)
    new_node.next = curr.next
    curr.next = new_node

    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

head = Node(3)
head.next = Node(5)
head.next.next = Node(8)
head.next.next.next = Node(10)
data = 12
pos = 3
head = insertion(head, pos, data)
print_list(head)