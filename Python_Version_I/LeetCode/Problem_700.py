# Search in a binary search tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def searchs(root, target):
    if root is None:
        return None
    
    if target < root.data:
        return searchs(root.left,target)
    elif target > root.data:
        return searchs(root.right,target)
    return root

def inorder(root):
    if root is None:
        return 
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)

# Create a BST
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)

# Search for a value
target = 2
result = searchs(root, target)

if result:
    print(f"Found: {result.data}")
    inorder(result)
else:
    print("Not Found")
    
