# Floor in binary search tree

'''
Given a Binary Search Tree and a number x, the task is to find the floor of x in the given BST,
 where floor means the greatest value node of the BST which is smaller than or equal to x.
   if x is smaller than the smallest node of BST then return -1.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None

def floor1(root,key):
    if root is None:
        return -1
    
    if root.data == key:
        return root.data
    
    if root.data > key:
        return floor1(root.left,key)
    floor_value = floor1(root.right,key)
    return floor_value if floor_value <= key and floor_value != -1 else root.data

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(30)

x = 14
print(floor1(root, x))