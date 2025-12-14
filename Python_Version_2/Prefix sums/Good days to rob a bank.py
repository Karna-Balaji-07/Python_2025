# Find the good days to rob a bank

def solution(arr,time):
    n = len(arr)
    decreasing = [0] * n
    increasing = [0] * n

    for i in range(1, n):
        if arr[i] <= arr[i-1]:
            decreasing[i] = decreasing[i-1] + 1

    for i in range(n-2,-1,-1):
        if arr[i+1] >= arr[i]:
            increasing[i] = increasing[i+1]+1

    result = []
    for i in range(n):
        if decreasing[i] >= time and increasing[i]>= time:
            result.append(i)
    return result

security = [5,3,3,3,5,6,2]; time = 2
print(solution(security,time))