# Invert Binary Tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def invert(root):
    if root is None:
        return None
    
    root.left,root.right = root.right, root.left

    invert(root.left)
    invert(root.right)

    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Invert the binary tree
inverted_root = invert(root)

# Helper function to print the tree (in-order traversal)
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.data, end=' ')
        print_tree(root.right)

# Print the inverted tree
print_tree(inverted_root)

