# Symmetric tree

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def symmetric(root):
    if root is None:
        return True
    return mirror(root.left,root.right)

def mirror(root,node):
    if root is None and node is None:
        return True
    if root is None or node is None:
        return False
    return (root.data == node.data and mirror(root.left,node.right) and mirror(root.right, node.left))

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(symmetric(root)) # True
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(2)
root2.left.left = Node(3)
root2.left.right = Node(4)
root2.right.left = Node(4)
root2.right.right = Node(3)

print(symmetric(root2)) # True