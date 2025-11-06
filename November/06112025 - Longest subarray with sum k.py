# Longest subarray with sum k

def solution1(arr,k):
    dicts = {}
    prefix = 0
    maxlen = 0
    for i in range(len(arr)):
        prefix += arr[i]
        if prefix == k:
            maxlen = i+1

        elif (prefix-k) in dicts:
            maxlen = max(maxlen, i-dicts[prefix-k])
        if (prefix-k) not in dicts:
            dicts[prefix] = i

    return maxlen

    