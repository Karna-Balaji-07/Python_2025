# Rotten oranges

def safe(i,j,n,m):
    return 0 <= i < n and 0 <= j < m
def dfs(arr,i,j,time):
    n = len(arr)
    m = len(arr[0])
    arr[i][j] = time
    directions = [[0,1],[1,0],[0,-1],[-1,0]]

    for dir in directions:
        x = i + dir[0]
        y = j + dir[1]

        if safe(x,y,n,m) and arr[x][y] == 1 or arr[x][y] > time+1:
            dfs(arr,x,y,time+1)

def rotten(arr):
    n = len(arr)
    m = len(arr[0])
    Time = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                dfs(arr,i,j,2)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                return -1
            Time = max(Time, arr[i][j]- 2)

    return Time


# BFS
from collections import deque
def BFS(arr):
    n = len(arr)
    m = len(arr[0])
    directions = [[0,1],[1,0],[-1,0],[0,-1]]
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i,j))
    time = 0
    while q:
        time += 1
        for i in range(len(q)):
            i,j = q.popleft()
            for dir in directions:
                x = i + dir[0]
                y = j + dir[1]
                if safe(x,y,n,m) and arr[x][y] == 1:
                    arr[x][y] = 2
                    q.append((x,y))

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                return -1

    return max(0,time-1)
