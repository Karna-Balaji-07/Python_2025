# find the maximum average subarray

def solution1(arr,k):
    sums = sum(arr[:k])
    avg = sums // k

    for i in range(k, len(arr)):
        sums += arr[i] - arr[i-k]
        avg = max(avg, sums // k)

    return avg


