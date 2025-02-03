# Balance a Binary Search Tree

class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None


def inorder(root,arr):
    if root is None:
        return root
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)



def balanced(arr,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    root = Node(arr[mid])
    root.left = balanced(arr,start,mid-1)
    root.right = balanced(arr,mid+1,end)
    return root

def BST(root):
    arr = []
    inorder(root,arr)
    return balanced(arr,0,len(arr)-1)

# Function to print the tree (Inorder Traversal)
def inorder1(root):
    if root is None:
        return

    inorder1(root.left)
    print(root.data, end=' ')
    inorder1(root.right)


    
    # Constructing an unbalanced BST
    #        10
    #       /  \
    #      5    15
    #     /       \
    #    2         20
    #   /
    #  1

root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.right = Node(15)
root.right.right = Node(20)
balanced_root = BST(root)
inorder1(root)