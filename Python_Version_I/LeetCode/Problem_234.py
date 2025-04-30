# Palindrome linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def palindrome(head):
    arr=[]
    curr=head
    while curr is not None:
        arr.append(curr.data)
        curr=curr.next
    s = ""
    s="".join(arr)
    arrs="".join(reversed(s))

    return arrs==s

def palindrome1(head):
    fast=head
    slow=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    prev=None
    curr=slow
    while curr:
        nextNode=curr.next
        curr.next=prev
        prev=curr
        curr=nextNode
    first,second=head, prev
    while second:
        if first.data!=second.data:
            return False
        first=first.next
        second=second.next
    return True
    

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next

# Example usage
head = Node('A')
head.next = Node('A')
head.next.next = Node('B')
head.next.next.next = Node('A')
head.next.next.next.next = Node('A')
print_list(head)
result=palindrome(head)
print(result)
