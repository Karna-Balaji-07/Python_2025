# Add numbered linked list 

'''
Given the head of two singly linked lists num1 and num2 representing two non-negative integers. 
The task is to return the head of the linked list representing the sum of these two numbers.

For example, num1 represented by the linked list : 1 -> 9 -> 0, similarly num2 represented by the linked list: 2 -> 5.
 Sum of these two numbers is represented by 2 -> 1 -> 5.

'''
class Node:
    def __init__(self,data):
        self.next = None
        self.data= data

def addition(head1,head2):
    x=0
    curr = head1
    while curr is not None:
        x = x*10 + curr.data
        curr = curr.next
    y=0
    curr = head2
    while curr is not None:
        y = y*10+curr.data
        curr=curr.next
    num1 = x
    num2 = y
    add = num1+num2
    if add==0:
        return Node(0)
    head = None
    while add  >  0:
        digit = add % 10
        newNode = Node(digit)
        newNode.next = head
        head= newNode
        add //=10
    return head

#------------------------------------------------------------------------------------------------------------------#

def reverse(head):
    prev = None
    curr = head
    while curr:
        newNode=curr.next
        curr.next= prev
        prev = curr
        curr = newNode
    return prev

def trimLeadingZeros(head):
    while head and head.data == 0:
        head = head.next
    return head

def countNodes(head):
    length = 0
    curr = head
    while curr is not None:
        length += 1
        curr = curr.next
    return length

def addition2(head1,head2):
    head1 = trimLeadingZeros (head1)
    head2 = trimLeadingZeros(head2)
    len1 =  countNodes (head1)
    len2 = countNodes(head2)
    if len1 < len2:
        return addition2(head2,head1)
    carry=0
    head1 = reverse(head1)
    head2 = reverse(head2)
    result = head1
    while head2 is not None or carry!=0:
        head1.data += carry
        if head2 is not None:
            head1.data += head2.data
            head2 = head2.next
        carry=head1.data//10
        head1.data=head1.data%10

        if head1.next is None and carry!=0:
            head1.next = Node(0)
        head1=head1.next
    return reverse(result)

     
             

def printLL(head):
    curr = head
    while curr is not None:
        print(curr.data,end=" ")
        curr = curr.next
    print()

head1 = Node(4)
head1.next = Node(5)
head2 = Node(3)
head2.next= Node(4)
head2.next.next = Node(5)
head = addition(head1,head2)
printLL(head)
head =addition2(head1,head2)
printLL(head)