# Subtraction of two matrices

def subtraction(arr1,arr2):
    a = len(arr1)
    b = len(arr1[0])
    result = [[0]*b for _ in range(a)]
    for i in range(a):
        for j in range(b):
            result[i][j] = arr1[i][j] - arr2[i][j]
    return result

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[1, 1, 1], [1, 1, 1]]
print(subtraction(m1,m2))