# Find the second largest Element in the Array

def second1(arr):
    arrs = list(set(arr))
    arrs.sort()
    return arrs[-2]

def second2(arr):
    maxi = float('-inf')
    maxis = float('-inf')
    for i in arr:
        if i > maxi:
            maxi = i

    for i in range(len(arr)):
        if arr[i] > maxis and arr[i] != maxi:
            maxis = arr[i]
    return maxi, maxis

arr = [12, 35, 1, 10, 34, 1]
print(second2(arr))