# Sum of k smallest elements in binary search Tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def inorder(root,arr):
    if root is None:
        return root
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)

def sums(root,k):
    if root is None:
        return -1
    arr = []
    inorder(root,arr)
    add = sum(arr[:k])
    return add

def inorder1(root,k,ans):
    if root.left is not None:
        inorder1(root.left,k,ans)
    if k[0] > 0:
        ans += root.data
        k[0] -= 1
    else:
        return
    
    if root.right is not None:
        inorder1(root.right,k,ans)

def sumss(root,k):
    ans = [0]
    inorder1(root,[k],ans)
    return ans[0]

root = Node(8)
root.left = Node(7)
root.right = Node(10)
root.left.left = Node(2)
root.right.left = Node(9)
root.right.right = Node(13)
print(sums(root,3))