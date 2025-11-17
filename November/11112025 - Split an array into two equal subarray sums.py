# Split an array into two equal subarray sums

def solution1(arr):
    n = len(arr)
    prefix = [0] * n
    suffix = [0] * n
    suffix[n-1] = arr[n-1]
    for i in range(n):
        prefix[i] = prefix[i-1] +  arr[i]
    for i in range(n-2,-1,-1):
        suffix[i] = arr[i] + suffix[i+1]

    result = []
    for i in range(1,n):
        if prefix[i-1] == suffix[i]:
            result.append(arr[:i])
            result.append(arr[i:])
    print(result)
arr = [1,2,3,4]
solution1(arr)