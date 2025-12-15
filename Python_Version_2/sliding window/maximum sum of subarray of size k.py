# Find the maximum sum of subarray of size k

def solution1(arr,k):
    n = len(arr)
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] +arr[i]

    maxsum = 0
    for i in range(n-k+1):
        j = i+k-1
        curr = prefix[j+1] - prefix[i]
        maxsum = max(maxsum, curr)

    return maxsum

def solution2(arr,k):
    sums = sum(arr[:k])
    result = 0
    for i in range(k,len(arr)):
        sums += arr[i]-arr[i-k]
        result = max(sums, result)
    return result