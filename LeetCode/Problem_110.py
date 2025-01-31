# Balanced binary Tree

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def balanced(root):
    if root is None:
        return True
    lheight = balanced(root.left)
    rheight = balanced(root.right)
    if lheight == -1 or rheight == -1:
        return -1
    if abs(lheight-rheight) > 1:
        return -1
    return 1 + max(lheight,rheight)

def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp = Node(arr[i]) if arr[i] is not None else None
        root = temp
        if temp is not None:
            root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
            root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root

arr = [1, 2, 2, 3, 3, None, None, 4, 4]
n = len(arr)
root = insertLevelOrder(arr, None, 0, n)

if balanced(root) != -1:
    print("The tree is balanced")
else:
    print("The tree is not balanced")