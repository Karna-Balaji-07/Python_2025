def dup(arr):
    n = len(arr)
    count = 1
    temp = []
    temp.append(arr[0])
    for i in range(1,n):
        if arr[i-1] != arr[i]:
            count += 1
            temp.append(arr[i])
    arr = temp

    return len(arr), arr

def dup2(arr):
    n = len(arr)
    index = 1
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            arr[index] = arr[i]
            index += 1
    return index, arr

arr = [32 ,40 ,43 ,60 ,72 ,78 ,82 ,82, 82, 99]
print(dup(arr))
print(dup2(arr))