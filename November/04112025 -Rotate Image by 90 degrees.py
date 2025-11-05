# Rotate image by 90 degrees

def solution(arr):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            arr[i][j],arr[j][i] = arr[j][i], arr[i][j]

    for i in range(n):
        arr[i].reverse()

    return arr