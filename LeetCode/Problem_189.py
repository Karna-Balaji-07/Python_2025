# Rotate array

def rotate1(arr,k):
    n=len(arr)
    result=[]
    for i in range(k,n):
        result.append(arr[i])
    for i in range(0,k):
        result.append(arr[i])
    return result

def rotate2(arr,k):
    n=len(arr)
    k %= n
    temp = arr[-k:]
    arr[k:] = arr[:-k]
    arr[:k] = temp
    return arr


nums = [-1,-100,3,99]
k = 2
print(rotate1(nums,k))
print(rotate2(nums,k))