# Insertion of a node at a specific position in the doubly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def insertion(head, data, position):
    new_node = Node(data)
    
    if position == 1:
        new_node.next = head
        if head is not None:
            head.prev = new_node
        head = new_node
        return head
    
    curr = head
    for _ in range(1, position-1):
        curr = curr.next
    new_node.prev = curr
    new_node.next = curr.next
    curr.next = new_node
    if new_node.next is not None:
        new_node.next.prev = new_node
    
    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next

    # Print the original list
print("Original Linked List: ", end="")
print_list(head)

    # Insert new node with data 3 at position 3
print("Inserting Node with data 3 at position 3: ", end="")
data = 3
pos = 3
head = insertion(head, data, pos)
    # Print the updated list
print_list(head)