# Chocolate distribution problem

def solution1(arr,m):
    mindiff = float('inf')
    n = len(arr)
    arr.sort()
    for i in range(n-m+1):
        diff = arr[i+m-1] - arr[i]
        if mindiff > diff:
            mindiff = diff
    return mindiff

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
print(solution1(arr,m))