# Insertion in a binary search tree in recursive manner

class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None

def insert(root, key):
    if root is None:
        return Node(key)
    if root.data == key:
        return root
    if root.data < key:
        root.right = insert(root.right,key)
    elif root.data > key:
        root.left = insert(root.left,key)
    
    return root

def inorder(root):
    if root is None:
        return 0
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)


r = Node(30)
r = insert(r,20)
r = insert(r,40)
r = insert(r,50)
r = insert(r,10)
r = insert(r,70)
r = insert(r,80)
r = insert(r,90)

inorder(r)