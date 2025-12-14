# Product of array except self

def solution1(arr):
    prefix = [1] * len(arr)
    suffix = [1] * len(arr)
    result = [0] * len(arr)
    for i in range(1,len(arr)):
        prefix[i-1] = prefix[i-1] * arr[i-1]
    for i in range(len(arr)-2,-1,-1):
        suffix[i+1] = suffix[i+1] * arr[i+1]

    for i in range(len(arr)):
        result[i] = prefix[i] * suffix[i]
    return result

def solution2(arr):
    zeros = 0
    index  = -1
    prod = 1
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
            index = i
        else:
            prod *= arr[i]
    result = [0] * len(arr)
    if zeros == 0:
        for i in range(len(arr)):
            result[i] = prod // arr[i]

    elif zeros == 1:
        result[index] = prod

    return result
