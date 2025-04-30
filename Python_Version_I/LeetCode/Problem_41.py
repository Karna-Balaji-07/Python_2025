# FIrst missing positive number

def solution1(arr):
    arr.sort()
    result = 1
    for i in arr:
        if i == result:
            result += 1
        if i > result:
            break
    return result

def solution2(arr):
    n = len(arr)
    visited = [False]*n
    for i in range(n):
        if 0 < arr[i] <= n:
            visited[arr[i]-1] = True
    for i in range(1,n):
        if not visited[i-1]:
            return i
    return n+1

nums = [3,4,-1,1]
print(solution2(nums))
