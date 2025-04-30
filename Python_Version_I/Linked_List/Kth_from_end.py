# Kth from the end of the linked list

class Node:
    def __init__(self,data):
        self.next=None
        self.data=data

def end(head,k):
    curr = head
    prev = None
    count=0
    while curr is not None:
        nextNode = curr.next
        curr.next =  prev
        prev = curr
        curr = nextNode
        count+=1
    if count < k:
        return -1
    else:
        for _ in range(k-1):
            prev = prev.next
        return prev.data

head = Node(20)
head.next = Node(30)
head.next.next = Node(40)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
print(end(head,7))

