# Middle of the linked list

class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

def middle(head):
    count=0
    curr=head
    arr=[]
    while curr is not None:
        arr.append(curr.data)
        curr = curr.next
    count = len(arr)
    mid = count//2
    return arr[mid]

head = Node(20)
head.next = Node(30)
head.next.next = Node(40)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(70)
print(middle(head))


