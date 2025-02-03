# Find the node with maximum value in the BST

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def maximum(root):
    if root is None:
        return -1
    curr = root
    while curr.right is not None:
        curr = curr.right
    return curr.data


