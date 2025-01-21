# Linked list group reverse
'''
The idea here is that we first store all the elements of the linked list in an array.
We then reverse k where k<n from the array
then update the linked list

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_in_groups(head, key):
    if head is None or key <= 1:
        return head  # No need to reverse if the list is empty or key is <= 1.

    # Collect all node data into an array.
    arr = []
    curr = head
    while curr is not None:
        arr.append(curr.data)
        curr = curr.next

    # Reverse in groups of `key`.
    rev = []
    i = 0
    n = len(arr)
    while i < n:
        rev.extend(arr[i:i+key][::-1])  # Reverse each group.
        i += key

    # Reconstruct the linked list from `rev`.
    new_head = Node(rev[0])
    curr = new_head
    for val in rev[1:]:
        curr.next = Node(val)
        curr = curr.next

    return new_head

# Helper function to print the linked list.
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next

# Example Usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

key = 3
print("Original List:")
print_list(head)

new_head = reverse_in_groups(head, key)
print("\nReversed in Groups of 3:")
print_list(new_head)
