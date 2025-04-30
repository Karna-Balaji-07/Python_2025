# Iterative inorder traversal

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):
    stack = []
    result = []
    curr = root

    while curr is not None or len(stack)>0:
        while curr is not None:
            stack.append(curr)
            curr=curr.left
        curr = stack.pop()
        result.append(curr.data)
        curr=curr.right

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
result=inorder(root)
print(result)