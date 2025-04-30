# Find the node with the minimum value in the Binary search Tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def minimum1(root,arr):
    if root is None:
        return root
    
    minimum1(root.left,arr)
    arr.append(root.data)
    minimum1(root.right,arr)

def minimum_value(root):
    if root is None:
        return -1
    arr = []
    minimum1(root,arr)
    return arr[0]

def approach2(root):
    if root is None:
        return -1
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr.data

root = Node(5)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(3)
root.right.right = Node(7)
root.left.left.left = Node(1)

arr = minimum_value(root)
print(arr)
print(approach2(root))