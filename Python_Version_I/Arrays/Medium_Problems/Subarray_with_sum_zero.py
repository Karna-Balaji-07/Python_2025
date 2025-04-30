# Subarray with zero sum

def zerosum(arr):
    prefix = {}
    sums = 0
    length = 0
    n=len(arr)
    for i in range(n):
        sums+=arr[i]
        if sums ==0:
            length = i+1
        if sums in prefix:
            length = max(length, i-prefix[sums])
        else:
            prefix[sums] = i
    return length

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(zerosum(arr))