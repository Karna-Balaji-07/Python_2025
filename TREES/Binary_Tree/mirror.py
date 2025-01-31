# Mirror tree

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def mirror(root,node):
    if root is None and node is None:
        return True
    if root is None or node is None:
        return False
    return (root.data == node.data and mirror(root.left,node.right) and mirror(root.right, node.left))

root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)
root1.right.left = Node(5)
root1.right.right = Node(4)
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

print(mirror(root1,root2)) # True