# rearrange array to make arr[i] = i

def rearrange(arr):
    n = len(arr)
    result = [-1]*n
    arrs = []
    for i in arr:
        if i >= 0:
            arrs.append(i)
    arrs.sort()
    for i in range(n):
        if i in arrs:
            result[i] = i
    return result

def rearrange2(arr):
    i = 0
    while i < len(arr):
        if arr[i] != -1 and arr[i] != arr[arr[i]]:
            temp = arr[i]
            arr[i] = arr[arr[i]]
            arr[temp] = temp

        else:
            i += 1
    return arr

arr = [0,1,2,3,4,5]
print(rearrange2(arr))