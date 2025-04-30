# Deletion of nodes in a doubly linked list

# Python Program to delete a node from the 
# beginning of Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Function to delete the first node (head) of the list
# and return the second node as the new head
def del_head(head):
  
    # If empty, return None
    if head is None:
        return None


    # Move head to the next node
    head = head.next

    # Set prev of the new head
    if head is not None:
        head.prev = None

    # Return new head
    return head

def del_last(head):
  
    # Corner cases
    if head is None:
        return None
    if head.next is None:
        return None

    # Traverse to the last node
    curr = head
    while curr.next is not None:
        curr = curr.next

    # Update the previous node's next pointer
    if curr.prev is not None:
        curr.prev.next = None

    # Return the updated head
    return head

def del_pos(head, pos):
    # If the list is empty
    if head is None:
        return head

    curr = head

    # Traverse to the node at the given position
    for i in range(1, pos):
        if curr is None:
            return head
        curr = curr.next

    # If the position is out of range
    if curr is None:
        return head

    # Update the previous node's next pointer
    if curr.prev is not None:
        curr.prev.next = curr.next

    # Update the next node's prev pointer
    if curr.next is not None:
        curr.next.prev = curr.prev

    # If the node to be deleted is the head node
    if head == curr:
        head = curr.next

    # Return the updated head
    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
    

if __name__ == "__main__":
  
	# Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    print("Original Linked List: ", end="")
    print_list(head)

    print("After Deletion at the beginning: ", end="")
    head = del_head(head)

    print_list(head)