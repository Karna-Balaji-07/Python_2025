# delete Nth node from the end of the given linked list

def solution1(head,n):
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next
    if n == length:
        return head.next
    index = length - n
    curr = head
    count = 1
    while curr:
        if index  == count:
            curr.next = curr.next.next
            break
        curr = curr.next
        count += 1

    return head

def solution2(head,n):
    fast = head
    slow = head
    for _ in range(n):
        fast = fast.next

    if fast is None:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head

