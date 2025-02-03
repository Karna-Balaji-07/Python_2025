# Insertion in a binary search tree in iterative manner

class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None

def insert(root,key):
    temp = Node(key)
    if root is None:
        return temp
    
    parent = None
    curr = root
    while curr is not None:
        parent = curr
        if curr.data > key:
            curr = curr.left
        elif curr.data < key:
            curr = curr.right
        else:
            return root
    
    if parent.data > key:
        parent.left = temp
    elif parent.data < key:
        parent.right = temp
    
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Creating the following BST
#      50
#     /  \
#    30   70
#   / \   / \
#  20 40 60 80
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inorder traversal of the BST
inorder(r)