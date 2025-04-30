# Rearrange to make arr[i] = i

def rearrange(arr):
    n = len(arr)
    arr.sort()
    temp = [-1]*n
    for i in arr:
        if 0 <= i <= n:
            temp[i] = i
    arr[:] = temp
    return arr

def rearrange2(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] != -1 and arr[i] != arr[arr[i]]:
            arr[i],arr[arr[i]] = arr[arr[i]],arr[i]
        else:
            i+=1
    return arr
    

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(rearrange(arr))
print(rearrange2(arr))