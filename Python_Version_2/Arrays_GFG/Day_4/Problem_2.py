# 1207. Unique number of occurrances

def solution1(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    arrs = list(dicts.values())
    return len(arrs) == len(set(arrs))

arr = [1,2]
print(solution1(arr))