# Reverse Level order Traversal

from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.right=self.left=None

def reverseLevelOrder(root):
    stack = []
    q = deque([root])

    while q:
        curr = q.popleft()
        stack.append(curr)

        if curr.right:
            q.append(curr.right)
        if curr.left:
            q.append(curr.left)
    while stack:
        curr=stack.pop()
        print(curr.data,end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

reverseLevelOrder(root)
