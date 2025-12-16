# Nerge two sorted linked list

def solution1(head1, head2):
    arr = []
    temp = head1
    while temp:
        arr.append(temp.data)
        temp = temp.next
    cur = head2
    while cur:
        arr.append(cur.data)
        cur = cur.next

    arr.sort()
    dummy= Node(-1)
    curr = dummy
    for i in arr:
        curr.next = Node(i)
        curr = curr.next
    return dummy.next

def solution2(head1, head2):
    dummy = Node(-1)
    head = dummy
    temp = head1
    curr =head2
    while temp and curr:
        if curr.data < temp.data:
            head.next = curr.data
            curr = curr.next
        else:
            head.next = temp.data
            temp = temp.next
        head = head.next

    if temp is not None:
        head.next = temp
    else:
        head.next = curr

    return dummy.next
