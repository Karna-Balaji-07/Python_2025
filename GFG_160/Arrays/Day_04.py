# Rotate Array

def rotate(arr,k):
    n = len(arr)
    k %= n
    temp = []
    temp.extend(arr[k:])
    temp.extend(arr[:k])
    arr[:] = temp
    return arr

arr = [1,2,3,4,5,6,7]
k=3
print(rotate(arr,k))
