# Sum of a binary tree - checks whether the sum of the left subtree and right subtree is equal to the root node

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False

def isSumTree(root):
    if root is None or isLeaf(root):
        return True
    if isSumTree(root.left) and isSumTree(root.right):
        if root.left is None:
            ls = 0
        elif isLeaf(root.left):
            ls = root.left.data
        else:
            ls = 2 * root.left.data

        if root.right is None:
            rs = 0
        elif isLeaf(root.right):
            rs = root.right.data
        else:
            rs = 2*root.right.data
        return root.data == ls+rs
    return False

def sum2(node):
    if node is None:
        return 0
    if node.left is None or node.right is None:
        return node.data
    
    ls = sum2(node.left)
    if ls == -1:
        return -1
    
    rs = sum2(node.right)
    if rs == -1:
        return -1
    
    if ls + rs == node.data:
        return ls+rs+node.data
    else:
        return -1

root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)

print(isSumTree(root)) # True
