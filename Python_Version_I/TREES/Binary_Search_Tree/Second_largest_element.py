# Find the second largest element in BST

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def inorder(root,arr):
    if root is None:
        return root
    
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)

def second(root):
    if root is None:
        return -1
    arr = []
    inorder(root,arr)
    return arr

root = Node(7)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(3)
root.left.right = Node(5)

result = second(root)
print(result[-2])
