# Product of array except self
from Python_Version_I.Stacks_Queues.Infix_to_Postfix import precedence


def solution1(arr):
    left = [1] * len(arr)
    right = [1] * len(arr)
    result = [0]*len(arr)

    for i in range(1, len(arr)):
        left[i] = arr[i-1] * left[i-1]
    for j in range(len(arr)-2,-1,-1):
        right[j] = arr[j+1] * right[j+1]

    for i in range(len(arr)):
        result[i] = left[i] * right[i]

    return result

def solution2(arr):
    zeros = 0
    index = -1
    product = 1
    for i in range(len(arr)):
        if arr[i] == 0:
            index = i
            zeros += 1

        else:
            product *= arr[i]
    result = [0] * len(arr)
    if zeros == 0:
        for i in range(len(arr)):
            result[i] = product // arr[i]

    elif zeros == 1:
        result[index] = product

    return result

arr = [10, 3, 5, 6, 2]
print(solution1(arr))