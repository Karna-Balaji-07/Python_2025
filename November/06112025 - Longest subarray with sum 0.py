# Longest subarray with sum zero

def solution1(arr):
    dicts = {}
    prefix = 0
    maxlen = 0
    dicts[0] = -1
    for i in range(len(arr)):
        prefix += arr[i]
        if prefix in dicts:
            prev = dicts[prefix]
            length = i - prev
            maxlen =  max(maxlen, length)
        else:
            dicts[prefix] = i

    return maxlen

