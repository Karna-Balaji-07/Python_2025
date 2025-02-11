# check if the given binarty tree is a heap

'''
Given a binary tree, check if it has heap property or not, Binary tree needs to fulfil the following two conditions for being a heap:

It should be a complete tree (i.e. all levels except the last should be full).
Every node’s value should be greater than or equal to its child node (considering max-heap).
'''
class Node:
    def __init__(self,data):
        self.key= data
        self.right = self.left = None

def countNodes(head):
    if head is None:
        return 0
    return 1+ countNodes(head.left)+countNodes(head.right)

def isCompleteUtil(root, index, NumberNodes):
    if root is None:
        return True
    if index >= NumberNodes:
        return False
    
    return isCompleteUtil(root.left, 2*index+1, NumberNodes) and isCompleteUtil(root.right, 2*index+2, NumberNodes)

def isHeapUtil(root):
    if root.left is None and root.right is None:
        return True
    
    if root.right is None:
        return root.key >= root.left.key
    else:
        if root.key >= root.left.key and root.key >= root.right.key:
            return isHeapUtil(root.left ) and isHeapUtil(root.right)
        else:
            return False
        
def isHeap(root):
    nodeCount = countNodes(root)
    index = 0
    if isCompleteUtil(root, index, nodeCount) and isHeapUtil(root):
        return True
    return False

def isHeap1(root):
    result = True

    if root is not None and root.left is None and root.right is not None:
        return False
    
    if root is not None and root.left is not None and root.left.key > root.key or root.right is not None and root.right.key > root.key:
        return False
    
    if root.left is not None:
        if root.left.left is not None or root.left.right is not None and root.right is None:
            return False
    
    if root.right is not None:
        if root.right.left is not None or root.right.right is not None and root.left is None:
            return False
    if root.left is not None:
        if root.left.left is None and root.left.right is None:
            if root.right is not None and root.right.left is not None and root.right.right is not None:
                return False
            
    if root is not None and root.left is not None:
        left = isHeap1(root.left)
        result = result and left
    if root is not None and root.right is not None:
        right = isHeap1(root.right)
        result = result and right

    return result


def isHeap2(root):
    queue = [root]
    flag = False
    while queue:
        temp = queue.pop(0)
        if temp.left:
            if flag or temp.left.key > temp.key:
                return False
            queue.append(temp.left)
        
        else:
            flag = True
        if temp.right:
            if flag or temp.right.key > temp.key:
                return flag
            queue.append(temp.right)
        else:
            flag = True

    return True


root = Node(10)
root.left = Node(9)
root.right = Node(8)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)

if isHeap(root):
    print("true")
else:
    print("false")
    