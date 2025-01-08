# Prefix sum array

def prefix1(arr,n,prefix):
    prefix[0] = arr[0]
    for i in range(1,n):
        prefix[i] = arr[i] + prefix[i-1]
    return prefix


arr = [10, 4, 16, 20]
n = len(arr)
prefix = [0]*n
print(prefix1(arr,n,prefix))