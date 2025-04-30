# Reversal of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    curr = head
    prev = None
    while curr is not None:
        nextNode = curr.next # Storing the nextNode
        curr.next = prev # pointing the next of curr to prev
        prev = curr # Moving pointers to one position ahead
        curr = nextNode
    return prev

def reverseLists(head):
    if head is None or head.next is None:
        return head

    rest = reverseList(head.next)
    head.next.next = head
    head.next = None
    return rest

def reverseList(head):
      
    
    stack = []
    temp = head
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next
    head = temp

    while stack:
        temp.next = stack.pop()
        temp = temp.next
    temp.next = None
  
    return head


def printList(node):
    while node is not None:
        print(f" {node.data}", end="")
        node = node.next
    print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Given Linked list:", end="")
printList(head)
head = reverseList(head)

print("Reversed Linked List:", end="")
printList(head)


