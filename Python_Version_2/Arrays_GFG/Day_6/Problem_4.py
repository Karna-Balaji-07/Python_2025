# Product of array except self

def solutionn1(arr):
    zeros = 0
    index = -1
    prod = 1
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
            index = i
        else:
            prod *= arr[i]
        
    result = [0]*len(arr)
    if zeros == 0:
        for i in range(len(arr)):
            result[i] = prod // arr[i]
    elif zeros == 1:
        result[index] = prod

    return result

arr = [10, 3, 5, 6, 2]
print(solutionn1(arr))