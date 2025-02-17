# Check if both the arrays are equal

def solution2(arr1,arr2):
    arr1.sort()
    arr2.sort()
    first = 0
    last = 0
    n,m = len(arr1),len(arr2)
    while first < n and last < m:
        if arr1[first] == arr2[last]:
            first += 1
            last += 1
        else:
            return False
    return True

def solution1(arr1,arr2):
    n,m = len(arr1),len(arr2)
    if n != m:
        return False
    
    dicts = {}
    for i in arr1:
        dicts[i] = dicts.get(i,0)+1
    for i in b:
        if i not in dicts:
            return False
        if dicts[i] == 0:
            return False
        
        dicts[i] -= 1
    return True

a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 1, 1]
print(solution1(a,b))