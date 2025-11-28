# Reverse an array in groups

def solution1(arr,k):
    for i in range(0,len(arr),k):
        arr[i:i+k] = arr[i:i+k][::-1]
    return arr

def reverseInGroups(arr, k):
    n = len(arr)
    for i in range(0, n, k):
        l, r = i, min(i+k-1, n-1)
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return arr


arr = [1,2,3,4,5,6,7,8]
print(solution1(arr,3))