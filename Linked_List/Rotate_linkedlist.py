# Rotate linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def rotate1(head,k):
    if k ==0 or head is None:
        return head
    
    for _ in range(k):
        curr = head
        while curr.next is not None:
            curr = curr.next
        
        curr.next = head
        curr = curr.next
        head = head.next
        curr.next = None
    return head

def rotate2(head,k):
    if k == 0 or head is None:
        return head
    curr = head
    length = 1
    while curr.next is not None:
        curr = curr.next
        length += 1

    k %= length
    if k == 0:
        return head

    curr.next = head
    curr = head
    for _ in range(1,k):
        curr = curr.next
    newHead = curr.next
    curr.next = None
    return newHead



def printLL(head):
    curr = head
    while curr is not None:
        print(curr.data,end=" ")
        curr = curr.next
    print()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

head = rotate2(head, 6)
printLL(head)