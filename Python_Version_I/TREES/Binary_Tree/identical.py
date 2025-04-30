# if the two trees are identical

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def Identical(node,root):
    if node is None and root is None:
        return True
    if node is None or root is None:
        return False
    
    return (node.data == node.data and Identical(node.left,root.left) and Identical(node.right,root.right))

r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r2 = Node(1)
r2.left = Node(2)
r2.right = Node(3)
r2.left.left = Node(4)
print(Identical(r1,r2)) # True