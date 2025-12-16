# Find the intersection point of two linked lists

def solution(head1, head2):
    temp = head1
    curr = head2
    while temp != curr:
        temp = temp.next if temp else head2
        curr = curr.next if curr else head1


    return temp.data if temp else -1

