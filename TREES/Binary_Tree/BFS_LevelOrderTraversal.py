# Level order traversal using stacks Recursion

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def LevelOrder(root,level,result):
    if not root:
        return
    
    if len(result) <= level:
        result.append([])
    result[level].append(root.data)
    LevelOrder(root.left,level+1,result)
    LevelOrder(root.right, level+1, result)

def levelOrder(root):
    result=[]
    LevelOrder(root,level=0,result=result)
    return result


root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.right.right = Node(4)
root.right.right.left = Node(6)
root.right.right.right = Node(5)

result=levelOrder(root)
for i in result:
    for j in i:
        print(j,end=" ")
    print("-",end=" ")