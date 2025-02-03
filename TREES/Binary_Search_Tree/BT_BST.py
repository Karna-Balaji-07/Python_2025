# Conversion of binary tree to binary search tree

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

def sorted_arr(root):
    if root is None:
        return -1
    arr = []
    inorder(root,arr)
    arr = sorted(arr)
    return arr

def BST(arr,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    root = Node(arr[mid])
    root.left = BST(arr,start,mid-1)
    root.right = BST(arr,mid+1,end)
    return root

def bst(arr):
    arr = sorted_arr(root)
    return BST(arr,0,len(arr)-1)

def print_bst(root):
    if root is None:
        return
    print_bst(root.left)
    print(root.data, end=" ")
    print_bst(root.right)

# Example usage
if __name__ == "__main__":
    # Construct the binary tree
    root = Node(10)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(4)

    # Convert the binary tree to a BST
    bst_root = bst(root)

    # Print the BST (inorder traversal should print sorted values)
    print("BST (Inorder Traversal):")
    print_bst(bst_root)