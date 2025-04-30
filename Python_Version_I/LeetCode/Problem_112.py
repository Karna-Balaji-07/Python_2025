# Path sum

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def path_sum(root,target):
    if root is None:
        return False
    if not root.left and not root.right:
        return root.data == target
    lsum = path_sum(root.left,target-root.data)
    rsum = path_sum(root.right, target-root.data)
    return lsum or rsum

# Create a binary tree
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)

# Target sum
target_sum = 22

# Check if a path with the target sum exists
print(path_sum(root, target_sum))  # Output: True