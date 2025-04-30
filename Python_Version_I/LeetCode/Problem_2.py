# Add two numbers

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def number(head):
    curr=head
    rem=0
    while curr is not None:
        value=curr.data
        rem=10*rem+value
        curr=curr.next
    return rem

def add(head1,head2):
    num1=number(head1)
    num2=number(head2)
    add=num1+num2
    head=None
    curr=None
    while add > 0:
        digit=add%10
        add //= 10
        newNode=Node(digit)
        if head is None:
            head=newNode
            curr=head
        else:
            curr.next=newNode
            curr=newNode

    return head


def add2(head1,head2):
    dummy=Node(0)
    curr=dummy
    rem=0
    while head1 or head2 or rem:
        num1=head1.data if head1 else 0
        num2=head2.data if head2 else 0

        total=num1+num2+rem
        digit=total%10
        rem=total//10

        curr.next=Node(digit)
        curr=curr.next

        if head1:
            head1=head1.next
        if head2:
            head2=head2.next
    
    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    

head=Node(2)
head.next=Node(4)
head.next.next=Node(3)

head2=Node(5)
head2.next=Node(6)
head2.next.next=Node(4)

result=add(head,head2)
print_linked_list(result)

ads=add2(head,head2)
print_linked_list(ads)
    
