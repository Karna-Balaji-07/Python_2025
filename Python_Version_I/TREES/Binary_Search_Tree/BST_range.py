# Print all the BST keys in the given range

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def inorder(root,n,m,arr):
    if root is None:
        return root
    inorder(root.left,n,m,arr)
    if root.data >=n and root.data <= m:
        arr.append(root.data)
    inorder(root.right,n,m,arr)

def prints(root,n,m):
    arr = []
    if root is None:
        return -1
    inorder(root,n,m,arr)
    return arr

root = Node(22)
root.left = Node(12)
root.right = Node(30)
root.left.left = Node(8)
root.left.right = Node(20)
n1, n2 = 10, 22
print(prints(root,n1,n2))