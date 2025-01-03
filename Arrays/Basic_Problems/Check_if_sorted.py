# To check if the array is sorted or not

def sorted1(arr):
    arrs = []
    arrs.extend(arr)
    arr.sort()
    if arrs == arr:
        return  True
    else :
        return False

def sorted2(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            return False
    return True

arr = [90, 80, 100, 70, 40, 30]
print(sorted1(arr))
print(sorted2(arr))