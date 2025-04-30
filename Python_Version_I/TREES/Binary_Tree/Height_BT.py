# Height or the maximum depth of a binary tree

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None   

def height1(root):
    if root is None:
        return -1
    lheight = height1(root.left)
    rheight = height1(root.right)
    height = max(lheight,rheight)+1
    return height


from collections import deque
def height2(root):
    if not root:
        return 0
    height = 0
    q = deque()
    q.append(root)
    q.append(None)
    while q:
        curr = q.popleft()
        if curr is None:
            height += 1
            if q : 
                q.append(None)
        else:
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return height -1

def height3(root):
    if root is None:
        return 0
    q= deque([root])
    height=0
    while q:
        q_len = len(q)
        for i in range(q_len):
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        height +=1
    return height -1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(height1(root))
print(height2(root))
print(height3(root))
