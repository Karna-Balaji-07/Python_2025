# Addition of two matrics 

def addition(matA, matB):
    a = len(matA)
    b = len(matA[0])
    result = [[0]*b for _ in range(a)]
    for i in range(a):
        for j in range(b):
            result[i][j] = matA[i][j] + matB[i][j]
    return result

A = [ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ]
B = [ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ]
print(addition(A,B))