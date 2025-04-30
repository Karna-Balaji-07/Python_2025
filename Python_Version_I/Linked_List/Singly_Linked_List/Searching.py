# Searching in a linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def searching(head, element):
    temp = head
    while temp is not None:
        if temp.data == element:
            return True
        temp = temp.next
    return False

head = Node(14)
head.next = Node(21)
head.next.next = Node(13)
head.next.next.next = Node(30)
head.next.next.next.next = Node(10)
element = 13
res = searching(head, element)
print(res)