# Level order traversal of a binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def levels(root, level, result):
    if root is None:
        return
    if len(result) <= level:
        result.append([])
    result[level].append(root.data)
    levels(root.left,level+1,result)
    levels(root.right, level+1, result)

def level_order(root):
    result = []
    levels(root, 0, result)
    return result