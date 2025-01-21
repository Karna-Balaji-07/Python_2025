# Rotate Array

def rotate(arr,k):
    n = len(arr)
    k %= n
    temp = []
    temp.extend(arr[k:])
    temp.extend(arr[:k])
    arr[:] = temp
    return arr

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
k=3
print(rotate(arr,k))
