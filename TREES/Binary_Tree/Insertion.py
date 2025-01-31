# Insertion in binary tree in level order manner

from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def insert(root,data):
    q = deque()
    if root is None:
        root = Node(data)
        return root
    
    q.append(root)
    while q:
        curr = q.popleft()

        if curr.left is not None:
            q.append(curr.left)
        else:
            curr.left = Node(data)
            return root 
        
        if curr.right is not None:
            q.append(curr.right)
        else:
            curr.right = Node(data)
            return root
        
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

root = Node(10)
root.left = Node(11)
root.right = Node(9)
root.left.left = Node(7)
root.right.left = Node(15)
root.right.right = Node(8)

key = 12
root = insert(root, key)
inorder(root)