# Reverse an array usiing recursion

def solution1(left, right, arr):
    if left >= right:
        return
    arr[left],arr[right] = arr[right], arr[left]
    solution1(left+1, right-1, arr)

def solution2(i,arr):
    n = len(arr)
    if i >= n//2:
        return
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    solution2(i+1,arr)
    