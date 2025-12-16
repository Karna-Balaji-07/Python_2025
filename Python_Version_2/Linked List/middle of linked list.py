# Find the middle of linked list

def solution(head):
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next

    mid = (length // 2)
    curr = head
    for i in range(mid):
        curr = curr.next
    return head.data

def solution2(head):
    slow= head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next

    return slow.data