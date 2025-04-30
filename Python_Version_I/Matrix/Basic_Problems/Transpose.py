# Transpose of a matrix

def transpose(arr):
    n = len(arr)
    m = len(arr[0])
    temp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[j][i]
    return temp

mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
print(transpose(mat))