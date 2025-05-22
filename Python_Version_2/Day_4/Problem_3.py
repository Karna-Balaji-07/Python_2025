# Missing and repeating Numbers

def solution1(arr):
    dicts = {}
    missing = -1
    repeating = -1
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    for i in range(1,len(dicts)+2):
        if i not in dicts:
            missing = i
        if i in dicts and dicts[i] >= 2:
            repeating = i
    return [repeating,missing]
arr = [4,3,6,2,1,1]
print(solution1(arr))