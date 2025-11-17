# Longest subarray with sum k ( positives and negatives )

def solution1(arr,k):
    dicts = {}
    prefix = 0
    result = 0
    n = len(arr)
    for i in range(n):
        prefix += arr[i]
        if prefix == k:
            result = max(result, i+1)

        if prefix - k in dicts:
            result = max(result, i-dicts[prefix-k])

        if prefix not in dicts:
            dicts[prefix] = i

    return result


