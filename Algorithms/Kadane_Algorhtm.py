# Kadane's Algorithm 

def subarray(arr):
    sums =arr[0]
    maxs = arr[0]
    n = len(arr)
    for i in range(1,n):
        sums = max(arr[i],sums+arr[i])
        maxs = max(sums, maxs)
    return maxs

arr =  [2, 3, -8, 7, -1, 2, 3]
print(subarray(arr))