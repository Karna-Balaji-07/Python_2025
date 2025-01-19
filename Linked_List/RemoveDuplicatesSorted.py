# Remove duplicates from unsorted linkedlist


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def duplicates(head):
    if head is None:
        return None

    arr = set()
    curr= head
    arr.add(curr.data)
    while curr.next is not None:
        if curr.next.data in arr:
            curr.next = curr.next.next
        else:
            arr.add(curr.next.data)
            curr = curr.next
    return head

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data,end=" ")
        temp = temp.next
    print()

head = Node(20)
head.next = Node(40)
head.next.next = Node(40)
head.next.next.next = Node(30)
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(20)
head = duplicates(head)
printLL(head)