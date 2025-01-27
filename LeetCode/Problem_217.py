# Contains duplicates

def duplicates1(arr):
    n=len(arr)
    if n <=1:
        return False
    dicts={}
    for i in arr:
        dicts[i] = arr.count(i)
    for value in dicts.values():
        if value > 1:
            return True
    return False

def duplicates2(arr):
    for i in arr:
        if arr.count(i) > 1:
            return True
    return False

def duplicates3(arr):
    dicts={}
    for i in arr:
        if i in dicts:
            return True
        else:
            dicts[i]=1
    return False

arr=[1,2,3,5]
print(duplicates1(arr))
print(duplicates2(arr))
print(duplicates3(arr))    