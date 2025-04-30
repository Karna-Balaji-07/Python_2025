# Check if the array is a subset of another array

def solution1(arr1,arr2):
    first = 0
    last = 0
    arr1.sort()
    arr2.sort()
    n,m = len(arr1),len(arr2)
    while first < n and last < m:
        if arr1[first] < arr2[last]:
            first += 1
        elif arr1[first] == arr2[last]:
            first += 1
            last += 1
        else:
            return False
    return last == len(arr2)

def solution2(arr1,arr2):
    arr = set(arr1)
    for i in arr2:
        if i not in arr:
            return False
    return True

a = [11, 1, 13, 21, 3, 7]
b = [11, 3, 7, 1]
print(solution2(a,b))

