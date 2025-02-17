# Disjoint Arrays

def solution1(arr1,arr2):
    arr = set(arr1)
    for i in arr2:
        if i in arr:
            return False
    return True

def solution2(arr1,arr2):
    first = 0
    last = 0
    arr1.sort()
    arr2.sort()
    n,m = len(arr1),len(arr2)
    while first < n and last < m:
        if arr1[first] < arr2[last]:
            first += 1
        elif arr1[first] == arr2[last]:
            return  False
        else:
            last += 1
    return True

a = [12, 34, 11, 9, 3]
b = [7, 2, 1, 3]
print(solution2(a,b))