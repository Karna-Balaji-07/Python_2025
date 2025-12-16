# Detect cycle in a graph

def solution1(head):
    s = set()
    temp = head
    while temp:
        if temp.data in s:
            return True
        s.add(temp.data)
        temp = temp.next
    return False

def solution2(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False