# find the maximum and minimum in a binary tree

class newNode:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def maxs(root):
    if root is None:
        return float('-inf')
    maxval = root.data
    lmax = maxs(root.left)
    rmax = maxs(root.right)
    lmax = max(lmax,maxval)
    rmax = max(maxval,rmax)
    maxi = max(lmax,rmax)

    return maxi

root = newNode(2)
root.left = newNode(7)
root.right = newNode(5)
root.left.right = newNode(6)
root.left.right.left = newNode(1)
root.left.right.right = newNode(11)
root.right.right = newNode(9)
root.right.right.left = newNode(4)
print(maxs(root))