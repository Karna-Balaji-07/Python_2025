# cells with odd values in matrix

def matrix(n,m,indices):
    arr = [[0]*m for _ in range(n)]
    for index in indices:
        row, col = index
        for i in range(m):
            arr[row][i] += 1
        for i in range(n):
            arr[i][col] += 1
    return arr

n = 2
m = 2
indices = [[1,1],[0,0]]
print(matrix(n,m,indices))