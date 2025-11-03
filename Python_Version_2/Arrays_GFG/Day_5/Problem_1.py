# Maximum Product Subarray

def solution1(arr):
    n = len(arr)
    currmax = arr[0]
    currmin = arr[0]
    maxprod = arr[0]
    for i in range(1,n):
        temp = max(arr[i], currmax * arr[i], currmin * arr[i])
        currmin = min(arr[i], arr[i]*currmax, arr[i]*currmin)
        currmax = temp
        maxprod = max(maxprod,currmax)
    return maxprod

def solution2(arr):
    n = len(arr)
    left = 1
    right = 1
    maxprod = float('-inf')
    for i in range(n):
        if left == 0:
            left = 1
        if right == 0:
            right = 1
        left *= arr[i]
        j = n-i-1
        right *= arr[j]
        maxprod = max(maxprod, right, left)
    return maxprod

arr  = [-2, 6, -3, -10, 0, 2]
print(solution2(arr))