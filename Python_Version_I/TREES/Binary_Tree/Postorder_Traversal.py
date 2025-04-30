# Postorder traversal

class Node:
    def __init__(self,data):
        self.left=self.right=None
        self.data=data

def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
postorder(root)
