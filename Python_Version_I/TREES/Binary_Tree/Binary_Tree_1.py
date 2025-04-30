class Node:
    def __init__(self,data):
        self.data =  data
        self.right=None
        self.left = None

firstNode=Node(10)
secondNode=Node(20)
thirdNode=Node(30)
fourthNode=Node(40)

firstNode.left=secondNode
firstNode.right =thirdNode
secondNode.left=fourthNode
