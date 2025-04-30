# merge k sorted linked list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

def solution1(arr):
    result = []
    for i in result:
        while i:
            result.append(i.data)
            i = i.next
    result.sort()
    head = node(arr[0])
    curr = head
    for i in arr[1:]:
        curr.next = node(i)
        curr= curr.next
    return head





