# Reverse an array

def solution1(arr):
    arr[:] = arr[::-1]
    return arr

def solution2(arr):
    arr.reverse()
    return arr

def solution3(arr):
    arrs = reversed(arr)
    return arrs

def solution4(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1

    return arr

def solution5(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i],arr[n-i-1] = arr[i],arr[n-i-1]
    return arr

