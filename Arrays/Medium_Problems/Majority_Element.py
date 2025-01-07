# Majority Element

def majority1(arr):
    n = len(arr)
    dict = {}
    for i in range(n):
        if arr[i] not in dict:
            dict[arr[i]] = arr.count(arr[i])
    for key,value in dict.items():
        if value > n//2:
            return key
    
    return -1

def majority2(arr):
    n = len(arr)
    arrs = list(set(arr))
    for i in arrs:
        if arr.count(i) > n//2:
            return i
    return -1

def majority3(arr):
    n = len(arr)
    count = 1
    arr.sort()
    if n == 1:
        return arr[0]
    for i in range(1,n):
        if arr[i-1] == arr[i]:
            count += 1
        else:
            if count > n//2:
                return arr[i-1]
            count = 1
    if count > n//2:
        return arr[-1]
    return -1

arr =  [1,3,2,3,3]
print(majority1(arr))
print(majority2(arr))
print(majority3(arr))