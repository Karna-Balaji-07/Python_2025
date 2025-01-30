# Array implementation of binary Tree

'''
 Case 1: (0—n-1) 
if (say)father=p; 
then left_son=(2*p)+1; 
and right_son=(2*p)+2;

Case 2: 1—n
if (say)father=p; 
then left_son=(2*p); 
and right_son=(2*p)+1; 

'''

tree = [None] * 10

def root(key):
    if tree[0] != None:
        print("Root node already has value")
    else:
        tree[0]=key

def left_node(key,parent):
    if tree[parent] == None:
        print("Cannot set left node here without parent node present")
    else:
        tree[(2*parent)+1]=key

def right_node(key,parent):
    if tree[parent] == None:
        print("Cannot set right node here without parent node")
    else:
        tree[(2*parent)+2]=key

def print_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i],end=" ")
        else:
            print("-",end=" ")
    print()


root('A')
left_node('B',0)
right_node('C',0)
left_node('D',1)
left_node('F',2)
right_node('G',2)
print_tree()
