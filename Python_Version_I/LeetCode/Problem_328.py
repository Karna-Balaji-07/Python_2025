# Odd even linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def OddEven(head):
    if not head or not head.next:
        return head
    odd=head
    even=head.next
    even_index=even

    while even and even.next:
        odd.next=even.next
        odd=odd.next
        even.next=odd.next
        even=even.next
    odd.next=even_index
    return head

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next=Node(6)
print_list(head)
head=OddEven(head)
print_list(head)
