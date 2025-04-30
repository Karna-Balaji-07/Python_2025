# Same tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def same(root, node):
    if root is None and node is None:
        return True
    if root is None or node is None:
        return False
    
    return node.data == root.data and same(root.left,node.left) and same(root.right, node.right)

