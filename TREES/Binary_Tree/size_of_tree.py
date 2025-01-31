# size of a tree - returns the number of nodes in a binary tree

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def size(root):
    if root is None:
        return 0
    bleft = size(root.left)
    bright = size(root.right)
    return bleft + bright + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(size(root))