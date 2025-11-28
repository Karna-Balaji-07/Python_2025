# Rotate an array by d places to the left

def solution1(arr,d):
    n = len(arr)
    d %= n
    temp = [0]*n
    for i in range(n-d):
        temp[i] = arr[d+i]
    for i in range(d):
        temp[n-d+i] = arr[i]

    arr[:] = temp
    return arr

def solution2(arr,d):
    d %= len(arr)
    arr[:] = arr[d:] + arr[:d]
    return arr

def solution3(arr,d):
    n = len(arr)
    d  %= n
    arr[:d] = arr[:d][::-1]
    arr[d:] = arr[d:][::-1]
    arr[:] = arr[::-1]
    return arr

arr = [1,2,3,4,5,6]
print(solution3(arr,2))