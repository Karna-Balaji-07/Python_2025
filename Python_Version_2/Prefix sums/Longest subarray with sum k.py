# Find the longest subarray with sum k

def solution1(arr,k):
    dicts = {}
    prefix = 0
    result = 0
    sums  = 0
    for i in range(len(arr)):
        prefix += arr[i]
        if prefix == k:
            result = max(result, i+1)
        if prefix - k in dicts:
            result = max(result, i - dicts[prefix-k])
        if prefix not in dicts:
            dicts[prefix] = i

    return result