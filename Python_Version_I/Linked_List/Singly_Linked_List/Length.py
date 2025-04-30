# Length of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    temp = head
    count = 0
    while temp is not None:
        count += 1
        temp = temp.next
    print(count)

head = Node(14)
head.next = Node(21)
head.next.next = Node(13)
head.next.next.next = Node(30)
head.next.next.next.next = Node(10)
length(head)