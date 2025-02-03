# Sorted Array to balanced binary search tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def balanced(arr,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    root = Node(arr[mid])
    root.left = balanced(arr,start,mid-1)
    root.right = balanced(arr,mid+1,end)
    return root

def balancedTree(arr):
    return balanced(arr,0,len(arr)-1)

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)

arr = [1, 2, 3, 4,5,6,7,8,9]
root = balancedTree(arr)
inorder(root)