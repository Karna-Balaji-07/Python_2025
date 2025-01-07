# Reorder arrays based on indices

def reorder(arr1,arr2):
    temp = {}
    n = len(arr1)
    for i in range(n):
        temp[arr2[i]] = arr1[i]
    sorts = dict(sorted(temp.items()))
    keys = []
    values = []
    for key,value in sorts.items():
        keys.append(key)
        values.append(value)
    return keys,values

def reorder2(arr1, arr2):
    n = len(arr1)
    temp = [0]*n
    for i in range(n):
        temp[arr2[i]] = arr1[i]
    arr1[:] = temp
    return arr1



arr1 = [50, 40, 70, 60, 90]
arr2 =  [3,  0,  4,  1,  2]
print(reorder(arr1,arr2))
print(reorder2(arr1,arr2))