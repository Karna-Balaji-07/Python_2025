# Union of arrays with duplicates

def union(arr1,arr2):
    sets = set()
    for i in arr1:
        sets.add(i)
    for i in arr2:
        sets.add(i)
    arrs = list(sets)
    return len(arrs)


a = [1, 2, 3, 4, 5]
b = [1, 2, 3]
print(union(a,b))