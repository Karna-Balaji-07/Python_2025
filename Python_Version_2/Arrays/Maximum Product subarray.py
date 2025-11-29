# Find the maximum product of a subarray

def solution1(arr):
    n = len(arr)
    maxprod = arr[0]
    minprod = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        temp = max(arr[i], arr[i]*minprod, arr[i]*maxprod)
        minprod = min(arr[i], arr[i]*minprod, arr[i]*maxprod)
        maxprod = temp
        result = max(maxprod, minprod, result)

    return result

def solution2(arr):
    n = len(arr)
    left =  1
    right = 1
    result = 0
    for i in range(n):
        if left == 0:
            left = 1
        if right == 0:
            right = 1

        left *= arr[i]
        j = n-i-1
        right *= arr[j]
        result = max(result, left, right)

    return result

