# Maximum depth of the binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def max_depth(root):
    if root is None:
        return 0
    lheight = max_depth(root.left)
    rheight = max_depth(root.right)
    return max(lheight+rheight)+1

from collections import deque

def max_depth(root):
    q = deque([root])
    height = 0
    while q:
        q_len = len(q)
        for i in range(q_len):
            curr = q.popleft()
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        height += 1
    return height


        