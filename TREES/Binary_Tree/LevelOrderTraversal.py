# Iterative level order traversal using queues

from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def levelOrder(root):
    if not root:
        return []
    
    q = deque()
    result=[]

    q.append(root)
    currLevel=0

    while q:
        q_len = len(q)
        result.append([])

        for i in range(q_len):
            node=q.popleft()
            result[currLevel].append(node.data)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        currLevel +=1

    return result

root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.right.right = Node(4)
root.right.right.left = Node(6)
root.right.right.right = Node(5)

result= levelOrder(root)
for i in result:
    for j in i:
        print(j,end=" ")
    print("",end=" ")

