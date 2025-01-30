# recursive inorder Traversal

class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
inorder(root)