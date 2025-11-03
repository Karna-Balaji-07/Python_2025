# Equilibirum Index

def solution1(arr):
    n = len(arr)
    i = 0
    j = n-1
    left = 0
    right = 0
    for i in range(1,n):
        left = sum(arr[:i])
        right = sum(arr[i+1:])
        if left == right:
            return i
    return -1

def solution2(arr):
    prefix = 0
    total = sum(arr)
    for pivot in range(len(arr)):
        suffix = total - prefix - arr[pivot]
        if suffix == prefix:
            return pivot
        prefix += arr[pivot]

    return -1


arr = [1,2,0,3]
print(solution2(arr))