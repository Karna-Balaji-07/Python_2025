# Reverse a linked list

def solution1(head):
    curr = head
    prev = None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

def solution2(head):
    if head is None and head.next is None:
        return head
    rest = solution2(head.next)
    head.next.next = head
    head.next = None
    return rest

def solution3(head):
    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next

    head = temp
    while stack:
        temp.next = stack.pop()
        temp = temp.next

    temp.next = None

    return head