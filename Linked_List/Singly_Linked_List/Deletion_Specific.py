# Removal of the node at specific position in the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def removal(head,position):
    if head is None or position < 1 :
        return None
    
    if position == 1:
        temp = head
        head = head.next
        del temp
        return head
    
    curr = head
    for _ in range(1,position-1):
        if curr is not None:
            curr = curr.next

    if curr is None and curr.next is None:
        return head
    temp = curr.next
    curr.next = curr.next.next
    del temp
    return head

def printList(head):
    while head:
        print(f"{head.data} -> ", end="")
        head = head.next
    print("None")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

    # Print original list
print("Original list: ", end="")
printList(head)

    # Deleting node at position 2
position = 2
head = removal(head, position)

    # Print list after deletion
print("List after deletion: ", end="")
printList(head)