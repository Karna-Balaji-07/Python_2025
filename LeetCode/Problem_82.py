# Remove duplicates from sorted list II

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    arr = []
    curr = head
    while curr is not None:
        arr.append(curr.val)
        curr = curr.next
    dicts = {}
    for i in arr:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1
    result = list(filter(lambda x: dicts[x] == 1, arr))
    if not result:
        return None
    result = result[::-1]
    head = Node(result[0])
    curr = head
    for i in range(1,len(result)):
        curr.next = Node(result[i])
        curr = curr.next

    return head

def deleteDuplicates1(head):
    if head is None:
        return None
    dummy = Node(0)
    prev = dummy
    dummy.next = head
    while head is not None:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next

    return dummy.next

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(5)

printList(deleteDuplicates1(head)) # 1 2 5

