# depth of a full binary tree using preorder traversal


def depth(root, index, n):
    if index[0] >=  n or root[index[0]] == 'l':
        return 0
    
    index[0] += 1
    left = depth(root, index, n)

    index[0] += 1
    right = depth(root, index, n)

    max_depth =  max(left, right)+1
    return max_depth

s= "nlnnlll"
n = len(s) 
print(depth(s, [0], n)) 


