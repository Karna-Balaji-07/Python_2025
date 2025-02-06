# Construct a binary tree from inorder and preorder traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.right=self.left= None

def BT(inorder, preorder):
    if not inorder or not preorder:
        return None
    
    root_data = preorder.pop(0)
    root = Node(root_data)

    inorder_index = inorder.index(root_data)
    root.left = BT(inorder[:inorder_index],preorder)
    root.right = BT(inorder[inorder_index+1:],preorder)

    return root

# Function to print inorder traversal of the tree (for validation)
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)

# Example Usage
preorder = [3, 9, 20, 15, 7]  # Root -> Left -> Right
inorder = [9, 3, 15, 20, 7]   # Left -> Root -> Right

root = BT(preorder, inorder)

print("Constructed Tree Inorder Traversal:")
inorder_traversal(root)  # Should print the same inorder sequence