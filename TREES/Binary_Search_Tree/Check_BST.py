# check if the given binary tree is a binary search tree

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

def checkBST(root):
    if root is None:
        return -1
    arr = []
    inorder(root,arr)
    return arr

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

result = checkBST(root)
if result == sorted(result):
    print("True")
else:
    print("False")